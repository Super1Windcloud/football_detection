
push:
    git add . && git commit -m "init "  &&  git push origin  main



pitch:
      uv run  main.py --source_video_path models/ball.mp4  \
      --target_video_path models/ball-pitch-detection.mp4 \
      --device cuda --mode PITCH_DETECTION


player:
      uv run  main.py --source_video_path models/player.mp4 \
      --target_video_path models/player-detection.mp4 \
      --device cuda  --mode PLAYER_DETECTION



ball:
       uv run  main.py --source_video_path models/ball.mp4 \
        --target_video_path models/ball-detection.mp4 \
        --device cuda --mode BALL_DETECTION



tracking:
      uv run  main.py --source_video_path models/tracking.mp4 \
      --target_video_path models/player-tracking.mp4 \
      --device cuda --mode PLAYER_TRACKING



team:
       uv run  main.py --source_video_path models/team.mp4 \
         --target_video_path models/team-classification.mp4 \
         --device cuda --mode TEAM_CLASSIFICATION



radar:
        uv run main.py --source_video_path models/radar.mp4 \
        --target_video_path models/radar-detection.mp4 \
        --device cuda --mode RADAR



train_player: 
      uv run trains/train_player_detector.py 

train_ball:
      uv run  trains/train_ball_detector.py 

train_pitch:
      uv run  trains/train_pitch_keypoint_detector.py
      

clear:
      git rm --cached -r . 