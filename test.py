import torch

cuda_available = torch.cuda.is_available()

gpu_count = torch.cuda.device_count()

if cuda_available:
    gpu_name = torch.cuda.get_device_name(0)  # 0 表示第一块 GPU
else:
    gpu_name = "N/A"

print(f"CUDA 是否可用: {cuda_available}")
print(f"GPU 数量: {gpu_count}")
print(f"GPU 名称: {gpu_name}")

if cuda_available:
    try:
        # 创建一个 CPU 张量
        x_cpu = torch.tensor([1.0, 2.0])
        # 将张量移动到第一个 GPU 上
        x_cuda = x_cpu.to("cuda")

        print("\n--- 启动测试结果 ---")
        print(f"张量创建成功，并已移动到设备: {x_cuda.device}")
        print("结论：PyTorch CUDA 环境启动正常！✅")

    except Exception as e:
        print("\n--- 启动测试结果 ---")
        print(f"错误：尝试将张量移动到 CUDA 设备时失败。错误信息: {e}")
        print("结论：CUDA 环境可能存在配置问题或依赖库缺失。❌")
else:
    print("\n结论：CUDA 不可用，请检查驱动和 PyTorch 版本匹配情况。❌")