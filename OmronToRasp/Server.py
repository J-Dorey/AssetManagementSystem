import socket
import pickle
import time

# This function creates a socket server for sending data


def socketServer(ipaddr, port, timeout):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ipaddr, port))
    server_socket.listen(1)
    server_socket.settimeout(timeout) # for testing purposes
    client_connected, client_address = server_socket.accept() 
    message = client_connected.recv(1024)
    messagedict = pickle.loads(message)
    return(messagedict)

'''
while(1):
    test_dict = socketServer('192.168.0.249', 124)

    for k, v in test_dict.items():
        test_dict[k] = 10

    print(test_dict)
'''
