# 基于 YOLOv8 的足球分析系统

本项目利用 [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) 深度学习框架，实现对足球比赛视频或图像中的关键元素进行检测和分析。

## 🌟 主要功能

-   **球员检测**: 实时检测和识别人场上的所有球员。
-   **足球检测**: 精确跟踪足球在场上的位置。
-   **球场关键点检测**: 识别足球场的关键几何点（如角点、球门区域等），用于后续的场地重建和战术分析。

## 🛠️ 技术栈

-   **Python 3.8+**
-   **PyTorch**
-   **Ultralytics YOLOv8**: 用于目标检测和姿态估计的核心框架。
-   **Roboflow**: 用于数据集的托管和版本管理。
-   **OpenCV**: 用于图像处理。

## 🚀 环境搭建

### 1. 克隆仓库

```bash
git clone <your-repository-url> 
cd llm-captcha-bypas
```

### 2. 安装依赖

建议在虚拟环境中安装项目依赖，以避免与其他项目产生冲突。

```bash
# 创建并激活虚拟环境 (以 venv 为例)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖
pip install ultralytics roboflow ipython opencv-python
```

### 3. 设置环境变量

为了从 Roboflow 下载数据集，您需要设置 API 密钥。请登录您的 Roboflow 账户获取密钥。

**Windows (PowerShell):**

```powershell
$env:ROBOFLOW_API_KEY="YOUR_API_KEY"
```

**macOS/Linux:**

```bash
export ROBOFLOW_API_KEY="YOUR_API_KEY"
```

> **注意**: 将 `YOUR_API_KEY` 替换为您自己的 Roboflow API 密钥。

## 📦 数据集

本项目使用的数据集托管在 Roboflow Universe 上。当您首次运行训练脚本时，程序会自动检查本地 `datasets` 目录。如果数据集不存在，它将自动从 Roboflow 下载。

-   **球员检测**: [football-players-detection](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc)
-   **足球检测**: [football-ball-detection](https://universe.roboflow.com/roboflow-jvuqo/football-ball-detection-rejhg)
-   **球场检测**: [football-field-detection](https://universe.roboflow.com/roboflow-jvuqo/football-field-detection-f07vi)

## 🏋️ 模型训练

您可以分别运行以下脚本来训练不同的模型。训练结果（包括权重文件和可视化图表）将保存在 `runs/` 目录下。

### 1. 训练球员检测模型

```bash
python trains/train_player_detector.py
```

-   **模型**: `yolov8x.pt`
-   **结果目录**: `runs/player/detect/train/`

### 2. 训练足球检测模型

```bash
python trains/train_ball_detector.py
```

-   **模型**: `yolov8x.pt`
-   **结果目录**: `runs/ball/detect/train/`

### 3. 训练球场关键点检测模型

```bash
python trains/train_pitch_keypoint_detector.py
```

-   **模型**: `yolov8x-pose.pt`
-   **结果目录**: `runs/pitch/pose/train/`

## 📊 查看结果

训练完成后，脚本会自动验证模型性能，并将训练过程中的图表（如 `results.png`、`confusion_matrix.png`）和预测示例（`val_batch0_pred.jpg`）保存在对应的结果目录中。

如果您在 Jupyter 环境中运行，脚本会尝试直接显示这些图像。

## 📜 许可证

本项目采用 [MIT License](LICENSE) 开源。
