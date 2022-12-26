from pickle import FALSE, TRUE
import sys
import time
import paho.mqtt.client as paho

#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string

#MQTT
broker="192.168.62.55"
#broker="127.0.0.1" for working in local
portMQTT =1883
runs = "False"

def on_message(client, userdata, message):
    time.sleep(1)
    print("received Topic: =",message.topic)
    try:
        if (message.topic=="Roboter/isRunning"):
            runs = str(message.payload.decode("utf-8"))

        
    except:
        print("Keine Verbindung zum Roboter")

  
def sendData(x,p):#(VariableName,Boolean)
    try:#Attempt connection to server
        client= paho.Client("client-003")
        client.on_message=on_message
    
        client.connect(broker,portMQTT)
        client.loop_start() #start loop to process received messages
        client.publish(x, p) #publish
        #client.subscribe("Roboter/isRunning")#subscribe
        time.sleep(1)
        client.disconnect() #disconnect
        client.loop_stop() #stop loop

    except:
        print("Could not make a connection to the server")
        input("Press enter to quit")
        sys.exit(0)





#def getData():
#    try:#Attempt connection to server
#        client= paho.Client("client-001") 
#        client.on_message=on_message

#        while TRUE:   #evtl WHILE Schleife kann man wegmachen
#            #hier sollte ein Event abgefragt werden vom OPC/UA
#            #aktuell wird im sekundentakt subscribed
#            client.connect(broker, portMQTT)#connect
#            print("subscribing ")
#            client.subscribe("Roboter/isRunning")#subscribe
#            time.sleep(1)
#            client.loop_forever()
    

#    except:
#        print("Could not make a connection to the server")
#        input("Press enter to quit")
#        sys.exit(0)

def getRuns():
    return runs