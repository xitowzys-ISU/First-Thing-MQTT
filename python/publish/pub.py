import paho.mqtt.client as paho


class MqttPublish:
    def __init__(self, broker: str, topic: str, client: str, client_to: str) -> None:
        self.broker: str = broker
        self.topic: str = topic
        self.client: "paho.Client" = paho.Client(client)
        self.client_to: str = client_to

        self.start()

    def start(self):
        print("Connecting to broker", self.broker)

        self.client.connect(self.broker)
        self.client.loop_start()

        print("Publishing")

    def push(self, data):
        print(f"data is {data}")
        self.client.publish(self.topic, data)