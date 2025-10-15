import os
from roboflow import Roboflow
from IPython.display import Image

# 获取当前工作目录
HOME = os.getcwd()
print(HOME)

# 创建 datasets 文件夹
datasets_dir = os.path.join(HOME, 'datasets')
os.makedirs(datasets_dir, exist_ok=True)

# 设置 Roboflow API 密钥
ROBOFLOW_API_KEY = os.getenv('ROBOFLOW_API_KEY')  # 确保在环境变量中设置了 API 密钥
rf = Roboflow(api_key=ROBOFLOW_API_KEY)

# 获取项目和版本信息
project = rf.workspace("roboflow-jvuqo").project("football-ball-detection-rejhg")
version = project.version(2)
dataset = version.download("yolov8")

# 修改数据集配置文件路径
data_yaml_path = os.path.join(dataset.location, 'data.yaml')
with open(data_yaml_path, 'r') as file:
    data_yaml = file.readlines()

# 更新 YAML 文件的路径配置
data_yaml = [line.replace("train: ", "train: ../train/images") if "train: " in line else line for line in data_yaml]
data_yaml = [line.replace("val: ", "val: ../valid/images") if "val: " in line else line for line in data_yaml]

# 写回更新后的 YAML 文件
with open(data_yaml_path, 'w') as file:
    file.writelines(data_yaml)

# 训练 YOLO 模型
os.system(f"yolo task=detect mode=train model=yolov8x.pt data={data_yaml_path} batch=12 epochs=50 imgsz=1280 plots=True")

# 查看训练结果
train_results_dir = os.path.join(HOME, 'runs/detect/train/')
os.system(f"ls {train_results_dir}")

# 显示混淆矩阵、训练结果图像、预测图像
Image(filename=os.path.join(train_results_dir, 'confusion_matrix.png'), width=600)
Image(filename=os.path.join(train_results_dir, 'results.png'), width=600)
Image(filename=os.path.join(train_results_dir, 'val_batch0_pred.jpg'), width=600)

# 验证模型
os.system(f"yolo task=detect mode=val model={os.path.join(HOME, 'runs/detect/train/weights/best.pt')} data={data_yaml_path} imgsz=1280")

# 部署模型
project.version(dataset.version).deploy(model_type="yolov8", model_path=os.path.join(HOME, 'runs/detect/train/'))
