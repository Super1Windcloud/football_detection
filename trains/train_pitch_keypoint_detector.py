import os
from ultralytics import YOLO
import multiprocessing

def main():
    from IPython.display import Image, display

    HOME = os.getcwd()
    print(f"当前工作目录: {HOME}")

    datasets_dir = os.path.join(HOME, 'datasets\\football-field-detection-12')

    if not os.path.exists(datasets_dir) or not os.listdir(datasets_dir):
        print("数据集不存在或为空，开始下载...")
        os.makedirs(datasets_dir, exist_ok=True)
        from roboflow import Roboflow
        ROBOFLOW_API_KEY = os.getenv('ROBOFLOW_API_KEY')
        if not ROBOFLOW_API_KEY:
            raise ValueError("请在环境变量中设置 ROBOFLOW_API_KEY")

        rf = Roboflow(api_key=ROBOFLOW_API_KEY)
        project = rf.workspace("roboflow-jvuqo").project("football-field-detection-f07vi")
        version = project.version(12)
        version.download("yolov8", location=datasets_dir) 
    else:
        print("数据集已存在，跳过下载。")


    data_yaml_path = os.path.join(datasets_dir, 'data.yaml')


    model = YOLO("yolov8x-pose.pt")  
    model.train(
        task="pose",
        data=data_yaml_path,
        epochs=100,
        batch=16,
        imgsz=640,
        mosaic=0.0,
        plots=True,
        name="train"
    )

    train_results_dir = os.path.join(HOME, 'runs/pitch/pose/train/')

    for img_name in ['results.png', 'val_batch0_pred.jpg']:
        img_path = os.path.join(train_results_dir, img_name)
        if os.path.exists(img_path):
            display(Image(filename=img_path, width=600))
        else:
            print(f"{img_name} 不存在")

    best_model_path = os.path.join(train_results_dir, 'weights/best.pt')
    model.val(task="pose", data=data_yaml_path, imgsz=640, model=best_model_path)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()

