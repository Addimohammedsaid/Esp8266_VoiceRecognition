import network
import socket
from machine import Pin


# Led pin 2 as an output :
led = Pin(2, Pin.OUT)

# Ip @ and port number :
UDP_IP = ""
UDP_PORT = 5005

# set as Udp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((UDP_IP, UDP_PORT))

try:

    while True:

        print('waiting...')

        data, addr = s.recvfrom(1024)

        print(str(addr)+'has just connect')

        # check the received message :
        print("received Message: ", data)

        # Convert the Bytes data to str :
        data = (data.decode("utf-8"))

        if(data.find('on') > 1):
            # Turn the led on
            led.value(0)  # for my board it's in reverse values
        elif (data.find('off') > 1):
            # By default the led is off
            led.value(1)

except:
    led.value(1)
    s.close()
    print("closed connection")
