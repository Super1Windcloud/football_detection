# import os
# from roboflow import Roboflow
# from IPython.display import Image
#
# # 获取当前工作目录
# HOME = os.getcwd()
# print(HOME)
#
# # 安装所需库
# os.system('pip install -q ultralytics roboflow')
#
# # 创建 datasets 文件夹
# datasets_dir = os.path.join(HOME, 'datasets')
# os.makedirs(datasets_dir, exist_ok=True)
#
# # 设置 Roboflow API 密钥
# ROBOFLOW_API_KEY = os.getenv('ROBOFLOW_API_KEY')  # 确保在环境变量中设置了 API 密钥
# rf = Roboflow(api_key=ROBOFLOW_API_KEY)
#
# # 获取项目和版本信息
# project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
# version = project.version(10)
# dataset = version.download("yolov8")
#
# # 修改数据集配置文件路径
# data_yaml_path = os.path.join(dataset.location, 'data.yaml')
# with open(data_yaml_path, 'r') as file:
#     data_yaml = file.readlines()
#
# # 更新 YAML 文件的路径配置
# data_yaml = [line.replace("train: ", "train: ../train/images") if "train: " in line else line for line in data_yaml]
# data_yaml = [line.replace("val: ", "val: ../valid/images") if "val: " in line else line for line in data_yaml]
#
# # 写回更新后的 YAML 文件
# with open(data_yaml_path, 'w') as file:
#     file.writelines(data_yaml)
#
# # 训练 YOLO 模型（detect任务）
# os.system(f"yolo task=detect mode=train model=yolov8x.pt data={data_yaml_path} batch=6 epochs=50 imgsz=1280 plots=True")
#
# # 查看训练结果
# train_results_dir = os.path.join(HOME, 'runs/detect/train/')
# os.system(f"ls {train_results_dir}")
#
# # 显示训练结果图像
# Image(filename=os.path.join(train_results_dir, 'confusion_matrix.png'), width=600)
# Image(filename=os.path.join(train_results_dir, 'results.png'), width=600)
# Image(filename=os.path.join(train_results_dir, 'val_batch0_pred.jpg'), width=600)
#
# # 验证模型
# os.system(f"yolo task=detect mode=val model={os.path.join(HOME, 'runs/detect/train/weights/best.pt')} data={data_yaml_path} imgsz=1280")
#
# # 部署模型
# project.version(dataset.version).deploy(model_type="yolov8", model_path=os.path.join(HOME, 'runs/detect/train/'))

import os
from roboflow import Roboflow
from ultralytics import YOLO
from IPython.display import Image


HOME = os.getcwd()
print("当前工作目录:", HOME)

datasets_dir = os.path.join(HOME, 'datasets')
os.makedirs(datasets_dir, exist_ok=True)

ROBOFLOW_API_KEY = os.getenv('ROBOFLOW_API_KEY')  # 确保在环境变量中设置了 API 密钥
rf = Roboflow(api_key=ROBOFLOW_API_KEY)

project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
version = project.version(10)
dataset = version.download("yolov8")


data_yaml_path = os.path.join(dataset.location, 'data.yaml')
with open(data_yaml_path, 'r') as f:
    data_yaml = f.readlines()

data_yaml = [line.replace("train: ", "train: ../train/images") if "train: " in line else line for line in data_yaml]
data_yaml = [line.replace("val: ", "val: ../valid/images") if "val: " in line else line for line in data_yaml]

with open(data_yaml_path, 'w') as f:
    f.writelines(data_yaml)

model = YOLO("yolov8x.pt") # large


model.train(
    data=data_yaml_path,
    epochs=50,
    batch=6,
    imgsz=1280,
    plots=True,        # 自动生成训练曲线和混淆矩阵
    project=os.path.join(HOME, "runs/detect"),  # 输出目录
    name="train"
)

train_results_dir = os.path.join(HOME, "runs/detect/train")
print("训练结果目录:", train_results_dir)


Image(filename=os.path.join(train_results_dir, 'confusion_matrix.png'), width=600)
Image(filename=os.path.join(train_results_dir, 'results.png'), width=600)
Image(filename=os.path.join(train_results_dir, 'val_batch0_pred.jpg'), width=600)


best_model_path = os.path.join(train_results_dir, 'weights', 'best.pt')
metrics = YOLO(best_model_path).val(
    data=data_yaml_path,
    imgsz=1280
)
print(metrics)


project.version(dataset.version).deploy(
    model_type="yolov8",
    model_path=train_results_dir
)

