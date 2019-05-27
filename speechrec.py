import speech_recognition as sr
import socket


# Ip ãnd port Target :
UDP_IP = "192.168.1.100"
UDP_PORT = 5005

# create the udp socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# create Recognizer object
r = sr.Recognizer()

# get audio from microphone
with sr.Microphone() as source:
    print('Speak Anything: ')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        # analyse the recorded audio
        Message = r.recognize_google(audio)
        print("UDP target IP:", UDP_IP)
        print("UDP target port:", UDP_PORT)
        print("Your Message : {}".format(Message))

        # sending the message :
        s.sendto(str.encode(Message), (UDP_IP, UDP_PORT))

    except:
        print("say it again")
