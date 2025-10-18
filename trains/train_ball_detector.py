import os
from ultralytics import YOLO
import multiprocessing

def main():
    from IPython.display import Image, display

    HOME = os.getcwd()
    print(f"当前工作目录: {HOME}")

    datasets_dir = os.path.join(HOME, 'datasets\\football-ball-detection-2')

    if not os.path.exists(datasets_dir) or not os.listdir(datasets_dir):
        print("数据集不存在或为空，开始下载...")
        os.makedirs(datasets_dir, exist_ok=True)
        from roboflow import Roboflow
        ROBOFLOW_API_KEY = os.getenv('ROBOFLOW_API_KEY')
        if not ROBOFLOW_API_KEY:
            raise ValueError("请在环境变量中设置 ROBOFLOW_API_KEY")

        rf = Roboflow(api_key=ROBOFLOW_API_KEY)
        project = rf.workspace("roboflow-jvuqo").project("football-ball-detection-rejhg")
        version = project.version(2)
        dataset = version.download("yolov8", location=datasets_dir)
        print(f"数据集下载位置: {dataset.location}")
    else:
        print("数据集已存在，跳过下载。")
        print(f"使用现有数据集: {datasets_dir}")


    data_yaml_path = os.path.join(datasets_dir, 'data.yaml')

    
  
    model = YOLO("yolov8x.pt") 

  
    model.train(
        data=data_yaml_path,
        epochs=50,
        batch=12,
        imgsz=1280,
        plots=True,
        name="train"
    )

 
    train_results_dir = os.path.join(HOME, 'runs/ball/detect/train/')

    for img_name in ['confusion_matrix.png', 'results.png', 'val_batch0_pred.jpg']:
        img_path = os.path.join(train_results_dir, img_name)
        if os.path.exists(img_path):
            display(Image(filename=img_path, width=600))
        else:
            print(f"{img_name} 不存在")

    
    best_model_path = os.path.join(train_results_dir, 'weights/best.pt')
    model.val(data=data_yaml_path, imgsz=1280, model=best_model_path)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()



