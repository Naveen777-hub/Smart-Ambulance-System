import time
import os
import logging

from utils.serial_listener import get_serial, read_line
from hardware.camera import capture_image
from ai.detector import VehicleDetector

# 🔧 Setup logging
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

print("🚑 Smart Ambulance System Started...")
logging.info("System started")

# Initialize components
ser = get_serial()
detector = VehicleDetector()

try:
    while True:

        # 🔁 Auto reconnect
        if ser is None:
            print("🔄 Reconnecting serial...")
            logging.warning("Serial disconnected, reconnecting...")
            ser = get_serial()
            time.sleep(2)
            continue

        data = read_line(ser)

        # 🔌 Handle disconnect
        if data == "DISCONNECTED":
            print("⚠️ Serial lost!")
            logging.error("Serial disconnected")
            ser = None
            continue

        if data:
            print(f"📩 Received: {data}")
            logging.info(f"Received: {data}")

            # 🚨 VIOLATION CASE
            if data == "NOT_MOVED":
                print("🚨 Violation detected")
                logging.info("Violation detected")

                image_path = capture_image()

                if image_path:
                    logging.info(f"Image captured: {image_path}")

                    print("🧠 Running detection...")
                    vehicle_found = detector.detect_vehicle(image_path)

                    if vehicle_found:
                        print("✅ Vehicle confirmed → keeping image")
                        logging.info("Vehicle detected → image kept")

                        # 👉 Future: send to Flask API here

                    else:
                        print("❌ No vehicle → deleting image")
                        logging.info("No vehicle detected → image deleted")

                        if os.path.exists(image_path):
                            os.remove(image_path)

            # ✅ SAFE CASE
            elif data == "MOVED":
                print("✅ Path cleared")
                logging.info("Path cleared")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 System stopped by user")
    logging.info("System stopped manually")
