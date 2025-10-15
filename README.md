# Football Video Analysis Tool

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A powerful computer vision tool for analyzing soccer/football matches from video. This project provides various analysis
modes including player detection, ball tracking, team classification, and radar visualization.

## Features

- **Player Detection**: Identify and track players on the field
- **Ball Detection**: Track the ball's position and movement
- **Team Classification**: Classify players into their respective teams
- **Pitch Detection**: Automatically detect and map the soccer pitch
- **Radar View**: Generate a top-down radar view of player positions
- **Player Tracking**: Track individual players across frames

## Prerequisites

- Python 3.8+
- CUDA (for GPU acceleration, recommended)
- FFmpeg (for video processing)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sport
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

Run the analysis using the main script:

```bash
python main.py --source_video_path path/to/your/video.mp4 --mode MODE --device cuda  # or cpu
```

### Interactive Mode

For a more user-friendly interface, use the demo script:

```bash
python demo.py
```

Then follow the on-screen prompts to select your desired analysis mode and input video.

### Available Modes

- `PITCH_DETECTION`: Detect and analyze the soccer pitch
- `PLAYER_DETECTION`: Detect players on the field
- `BALL_DETECTION`: Track the ball's movement
- `PLAYER_TRACKING`: Track players across frames
- `TEAM_CLASSIFICATION`: Classify players into teams
- `RADAR`: Generate a radar view of player positions

## Project Structure

```
├── models/                  # Pre-trained models
├── sports/                  # Source code
│   ├── annotators/         # Annotation utilities
│   ├── common/             # Common utilities
│   └── configs/            # Configuration files
├── videos/                 # Sample videos
├── main.py                 # Main script
├── demo.py                 # Interactive demo
└── README.md               # This file
```

## Configuration

Edit the `.env` file to configure environment-specific settings:

```
# Example .env file
MODEL_PATH=models/football-player-detection.pt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [YOLOv8](https://ultralytics.com/yolov8)
- Uses [Supervision](https://roboflow.com/supervision) for computer vision utilities
- Inspired by modern sports analytics tools