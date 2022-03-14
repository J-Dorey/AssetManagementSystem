import socket
import pickle
import time
import threading

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

def socketServerMultiThreading(ipaddr, port, timeout, queue):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((ipaddr, port))
    except socket.error as e:
        print(e)

    finally:
        server_socket.listen(1)
    #    server_socket.settimeout(timeout) # for testing purposes
        client_connected, client_address = server_socket.accept()
        message = client_connected.recv(1024)
        messagedict = pickle.loads(message)
        time.sleep(10)
        queue.put(messagedict)

    
 
