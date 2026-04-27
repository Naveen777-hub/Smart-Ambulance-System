import serial
import glob
import time

BAUD_RATE = 115200


def get_serial():
    ports = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')

    for port in ports:
        try:
            ser = serial.Serial(port, BAUD_RATE, timeout=1)
            time.sleep(2)
            ser.reset_input_buffer()
            print(f"✅ Connected to {port}")
            return ser
        except Exception as e:
            print(f"❌ Failed on {port}: {e}")

    return None


def read_line(ser):
    try:
        if ser is None:
            return None

        line = ser.readline().decode('utf-8', errors='ignore').strip()

        if not line:
            return None

        print(f"RAW: {line}")  # debug

        if "DATA:" in line:
            data = line.replace("DATA:", "").strip()

            if data in ["MOVED", "NOT_MOVED"]:
                return data

    except serial.SerialException:
        print("⚠️ Serial disconnected!")
        return "DISCONNECTED"

    except Exception as e:
        print("⚠️ Read error:", e)

    return None
