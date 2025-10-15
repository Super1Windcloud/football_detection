from main import Mode, start_run_model
import os


def select_mode():
    modes = list(Mode)
    print("请选择检测模式：")
    for idx, mode in enumerate(modes, 1):
        print(f"{idx}. {mode.value}")

    while True:
        choice = input("输入数字选择模式: ")
        if not choice.isdigit():
            print("请输入有效数字")
            continue
        choice = int(choice)
        if 1 <= choice <= len(modes):
            return modes[choice - 1]
        else:
            print(f"请输入 1 到 {len(modes)} 之间的数字")


if __name__ == "__main__":
    videos_files = os.listdir("./videos/")
    mode = select_mode()
    print(f"你选择的模式是: {mode.value}")

    for video_file in videos_files:
        file_name = video_file.split(".")[0].replace("\\", "/")
        video_file = os.path.join("./videos/", video_file)
        if os.path.isfile(video_file):
            target_file = os.path.join(
                "./videos/", file_name + "_detection_result.mp4"
            ).replace("\\", "/")
            print(target_file)
            start_run_model(
                source_video_path=video_file,
                target_video_path=target_file,
                device="cuda",
                mode=mode,
            )


