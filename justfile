
push:
    git add . && git commit -m "init "  &&  git push repo main:master



pitch:
      sudo uv run  main.py --source_video_path models/2e57b9_0.mp \
      --target_video_path models/2e57b9_0-pitch-detection.mp4 \
      --device cuda --mode PITCH_DETECTION


player:
      uv run  main.py --source_video_path models/2e57b9_0.mp4 \
      --target_video_path models/2e57b9_0-player-detection.mp4 \
      --device cuda  --mode PLAYER_DETECTION



ball:
       uv run  main.py --source_video_path models/2e57b9_0.mp4 \
        --target_video_path models/2e57b9_0-ball-detection.mp4 \
        --device cuda --mode BALL_DETECTION



tracking:
      uv run  main.py --source_video_path models/2e57b9_0.mp4 \
      --target_video_path models/2e57b9_0-player-tracking.mp4 \
      --device cuda --mode PLAYER_TRACKING



team:
       uv run  main.py --source_video_path models/2e57b9_0.mp4 \
         --target_video_path models/2e57b9_0-team-classification.mp4 \
         --device cuda --mode TEAM_CLASSIFICATION



radar:
        uv run main.py --source_video_path models/2e57b9_0.mp4 \
        --target_video_path models/2e57b9_0-radar.mp4 \
        --device cuda --mode RADAR