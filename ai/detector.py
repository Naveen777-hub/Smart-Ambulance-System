import cv2

class VehicleDetector:
    def __init__(self):
        print("📦 Lightweight detector initialized")

    def detect_vehicle(self, image_path):
        frame = cv2.imread(image_path)

        if frame is None:
            return False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)

        # 🔥 Focus on center region
        h, w = edges.shape
        roi = edges[h//3:2*h//3, w//3:2*w//3]

        edge_pixels = cv2.countNonZero(roi)

        print(f"[ML] Edge intensity (center): {edge_pixels}")

        # 🔥 Adjusted threshold
        if edge_pixels > 5000:
            print("[ML] Vehicle likely present")
            return True
        else:
            print("[ML] No vehicle detected")
            return False
