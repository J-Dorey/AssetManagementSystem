from http import client
import socket
import pickle
import Addresses
import time


def clientSend(ipaddress, port, dictionary):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((ipaddress, port))
        serial_dict = pickle.dumps(dictionary)
        client_socket.send(serial_dict)
        client_socket.close()
        
    except socket.error as e:
        print(e)
        client_socket.close()


dict = Addresses.loadConfig()
increment = 0

while(1):

    for k, v in dict.items():
        dict[k] = increment

    dict['time_stamp'] = time.strftime("%H:%M:%S", time.localtime())

    clientSend('192.168.20.39', 1234, dict)
    time.sleep(1)
    increment += 1

  