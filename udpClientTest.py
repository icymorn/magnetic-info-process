import socket
from config.Config import config
import time
sender = config.data['network']['server']

UDP_IP = sender['ip']
UDP_PORT = sender['port']



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

num = 0.1
while True:
  MESSAGE = "192.168.0.1 [1.2, 3.4, 4.5, 3.4," + str(num) + "]"
  time.sleep(1)
  sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
  print MESSAGE, ": sended"
  num += 0.1