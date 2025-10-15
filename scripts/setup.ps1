# 获取脚本所在目录
$DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition

# 检查 data 目录是否存在
if (-Not (Test-Path "$DIR\models")) {
    New-Item -ItemType Directory -Path "$DIR\models" | Out-Null
} else {
    Write-Host "'models' directory already exists."
}

# 定义一个下载函数（封装 gdown）
function Download-File($url, $output) {
    Write-Host "Downloading $output ..."
    gdown --fuzzy -O $output $url
}

# 下载模型文件
Download-File "https://drive.google.com/uc?id=1isw4wx-MK9h9LMr36VvIWlJD6ppUvw7V" "$DIR\models\football-ball-detection.pt"
Download-File "https://drive.google.com/uc?id=17PXFNlx-jI7VjVo_vQnB1sONjRyvoB-q" "$DIR\models\football-player-detection.pt"
Download-File "https://drive.google.com/uc?id=1Ma5Kt86tgpdjCTKfum79YMgNnSjcoOyf" "$DIR\models\football-pitch-detection.pt"

# 下载视频文件
Download-File "https://drive.google.com/uc?id=12TqauVZ9tLAv8kWxTTBFWtgt2hNQ4_ZF" "$DIR\models\0bfacc_0.mp4"
Download-File "https://drive.google.com/uc?id=19PGw55V8aA6GZu5-Aac5_9mCy3fNxmEf" "$DIR\models\2e57b9_0.mp4"
Download-File "https://drive.google.com/uc?id=1OG8K6wqUw9t7lp9ms1M48DxRhwTYciK-" "$DIR\models\08fd33_0.mp4"
Download-File "https://drive.google.com/uc?id=1yYPKuXbHsCxqjA9G-S6aeR2Kcnos8RPU" "$DIR\models\573e61_0.mp4"
Download-File "https://drive.google.com/uc?id=1vVwjW1dE1drIdd4ZSILfbCGPD4weoNiu" "$DIR\models\121364_0.mp4"

Write-Host "✅ 所有文件已下载完成。"
