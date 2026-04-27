import os
import time

def capture_image():
    # ensure logs folder exists
    logs_path = "/home/naveen/rescueway/logs"
    os.makedirs(logs_path, exist_ok=True)

    timestamp = int(time.time())
    image_path = f"{logs_path}/violation_{timestamp}.jpg"

    # capture image using Raspberry Pi camera
    cmd = f"rpicam-still --nopreview -o {image_path}"
    os.system(cmd)

    # verify image saved
    if os.path.exists(image_path):
        print(f"📸 Image saved: {image_path}")
        return image_path
    else:
        print("❌ Image capture failed")
        return None
