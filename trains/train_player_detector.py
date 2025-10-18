import os
from ultralytics import YOLO
from IPython.display import Image

def main():
    HOME = os.getcwd()
    print("当前工作目录:", HOME)

    datasets_dir = os.path.join(HOME, 'datasets', 'football-players-detection-10')
    data_yaml_path = os.path.join(datasets_dir, 'data.yaml')

    if not os.path.exists(datasets_dir):
        os.makedirs(datasets_dir, exist_ok=True)
        from roboflow import Roboflow
        ROBOFLOW_API_KEY = os.getenv('ROBOFLOW_API_KEY')  
        rf = Roboflow(api_key=ROBOFLOW_API_KEY)
        project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
        version = project.version(10)
        dataset = version.download("yolov8", location=datasets_dir)
        print("数据集下载路径:", dataset.location)
    else:
        print("数据集目录已存在，跳过下载。")

    model = YOLO("yolov8x.pt")  # large

    model.train(
        data=data_yaml_path,
        epochs=50,
        batch=6,
        imgsz=1280,
        plots=True,  # 自动生成训练曲线和混淆矩阵
        project=os.path.join(HOME, "runs/player/detect"),
        name="train"
    )

    train_results_dir = os.path.join(HOME, "runs/player/detect/train")
    print("训练结果目录:", train_results_dir)

    Image(filename=os.path.join(train_results_dir, 'confusion_matrix.png'), width=600)
    Image(filename=os.path.join(train_results_dir, 'results.png'), width=600)
    Image(filename=os.path.join(train_results_dir, 'val_batch0_pred.jpg'), width=600)

    best_model_path = os.path.join(train_results_dir, 'weights', 'best.pt')
    metrics = YOLO(best_model_path).val(data=data_yaml_path, imgsz=1280)
    print(metrics)

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # Windows 多进程安全启动
    main()