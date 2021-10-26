import serial
from pub import MqttPublish


def get_connection():
    ser = serial.Serial('/dev/cu.usbmodem14401', timeout=1)
    return ser


ser = get_connection()

mp = MqttPublish(
    broker="broker.hivemq.com",
    topic="house/humidity",
    client="client-isu-xitowzys-pub",
    client_to="client-isu-xitowzys-sub"
)

while True:
    try:
        test = ser.readline().decode()
        mp.push(int(test) // 4)
    except Exception:
        continue
