import paho.mqtt.client as mqtt
def ao_conectar(client,userdata,flags,rc):

    print(f"nos conectamos com o seguinte codigo de resultado {rc}")


def ao_receber(client,userdata,msg):
    print(f"{msg.topic} --- {msg.payload} ")

