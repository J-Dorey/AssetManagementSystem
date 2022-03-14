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

while(1):
    clientSend('192.168.0.249', 1234, dict)
    time.sleep(5)

  