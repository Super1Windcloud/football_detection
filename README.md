# 基于 YOLOv8 的足球分析系统

本项目利用 [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) 深度学习框架，实现对足球比赛视频或图像中的关键元素进行检测和分析。

## 🌟 主要功能

- **球场检测**: 识别足球场的关键几何点（如角点、球门区域等），用于后续的场地重建和战术分析
- **球员检测**: 实时检测和识别场上的所有球员
- **足球检测**: 精确跟踪足球在场上的位置
- **球员追踪**: 跨帧追踪球员的移动轨迹
- **队伍分类**: 自动识别不同队伍的球员
- **雷达视图**: 生成战术分析的雷达图

## 🛠️ 技术栈

- **Python 3.12+**
- **uv**: 现代 Python 包管理器
- **PyTorch**: 深度学习框架
- **Ultralytics YOLOv8**: 用于目标检测和姿态估计的核心框架
- **Supervision**: 计算机视觉工具库
- **OpenCV**: 图像处理
- **Just**: 命令运行器

## 🚀 快速开始

### 1. 安装依赖

确保您已安装 [uv](https://docs.astral.sh/uv/) 和 [just](https://github.com/casey/just)：

```bash
# 安装 uv (如果尚未安装)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装 just (如果尚未安装)
# Windows (使用 scoop)
scoop install just
# macOS (使用 homebrew)
brew install just
# 或者使用 cargo
cargo install just
```

### 2. 克隆仓库并安装依赖

```bash
cd football_detection
uv sync
```

### 3. 设置环境变量

创建 `.env` 文件或设置环境变量：

```bash
# 创建 .env 文件
echo "ROBOFLOW_API_KEY=YOUR_API_KEY" > .env
```

> **注意**: 将 `YOUR_API_KEY` 替换为您自己的 Roboflow API 密钥。

## 📦 数据集

本项目使用的数据集托管在 Roboflow Universe 上。当您首次运行训练脚本时，程序会自动检查本地 `datasets` 目录。如果数据集不存在，它将自动从
Roboflow 下载。

- **球员检测
  **: [football-players-detection](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc)
- **足球检测**: [football-ball-detection](https://universe.roboflow.com/roboflow-jvuqo/football-ball-detection-rejhg)
- **球场检测**: [football-field-detection](https://universe.roboflow.com/roboflow-jvuqo/football-field-detection-f07vi)

## 🎯 使用方法

项目使用 `just` 命令运行器来简化操作。所有命令都会自动使用 `uv run` 来执行。

### 推理模式

#### 球场检测

```bash
just pitch
```

检测足球场关键点，输出带标注的视频。

#### 球员检测

```bash
just player
```

检测场上所有球员位置。

#### 足球检测

```bash
just ball
```

检测和追踪足球位置。

#### 球员追踪

```bash
just tracking
```

跨帧追踪球员移动轨迹。

#### 队伍分类

```bash
just team
```

自动识别不同队伍的球员。

#### 雷达视图

```bash
just radar
```

生成战术分析的雷达图。

### 训练模式

#### 训练球员检测模型

```bash
just train_player
```

#### 训练足球检测模型

```bash
just train_ball
```

#### 训练球场关键点检测模型

```bash
just train_pitch
```

## 🎮 自定义使用

您也可以直接使用 `uv run` 来执行脚本：

```bash
# 自定义视频路径和参数
uv run main.py --source_video_path your_video.mp4 \
               --target_video_path output.mp4 \
               --device cuda \
               --mode PLAYER_DETECTION

# 运行演示脚本
uv run demo.py
```

## 📊 模型训练

训练结果（包括权重文件和可视化图表）将保存在 `runs/` 目录下：

- **球员检测模型**: `runs/player/detect/train/`
- **足球检测模型**: `runs/ball/detect/train/`
- **球场关键点检测模型**: `runs/pitch/pose/train/`

训练完成后，脚本会自动验证模型性能，并将训练过程中的图表（如 `results.png`、`confusion_matrix.png`）和预测示例保存在对应的结果目录中。

## 📜 许可证

本项目采用 [MIT License](LICENSE) 开源。
