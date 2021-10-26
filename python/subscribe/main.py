import serial
import paho.mqtt.client as paho

broker = "broker.hivemq.com"

def get_connection():
    ser = serial.Serial('COM8', timeout=1)
    return ser

ser = get_connection()

def on_message(client, userdata, message):
    if message.topic == 'house/humidity':
        data = int(str(message.payload.decode()))
        ser.write(bytearray([data]))

client = paho.Client("client-isu-fsldmf-pub")
client.on_message = on_message

print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Subscribing")
client.subscribe("house/humidity")

while True:
    ...