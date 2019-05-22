import paho.mqtt.client as mqtt
import time

broker = "test.mosquitto.org"

###
def on_message(client, userdata, message) :
	print("Message : ", str(message.payload.decode("utf-8")))
	print("Topic : ", message.topic)
	print("QOS level : ", message.qos)
###
def on_connect (client, userdata, flags, rc) : 
	print 'Connected with code : %s' % str(rc)

###

client = mqtt.Client("cl-1")

#custom function
client.on_message = on_message
client.on_connect = on_connect

client.connect('iot.eclipse.org', 1883)
print 'Connect to broker'



client.loop_start()

#subscribe dulu baru publish

client.subscribe("sensor/temp")
print 'Subscribed to sensor/temp'

client.publish("sensor/temp", "ON")
print 'publish to sensor/temp'

time.sleep(4) # wait

client.loop_stop()