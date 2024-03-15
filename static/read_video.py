import cv2

# 读取视频
video_capture = cv2.VideoCapture('haoke-4d.mp4')

# 检查视频是否成功打开
if not video_capture.isOpened():
    print("Error: Unable to open video file.")
    exit()

# 读取并保存视频帧
frame_count = 0
while True:
    ret, frame = video_capture.read()

    # 如果视频读取结束，退出循环
    if not ret:
        break

    # 保存帧为图片
    cv2.imwrite(f'haoke_{frame_count}.jpg', frame)

    # 递增帧计数器
    frame_count += 1

# 释放资源
video_capture.release()