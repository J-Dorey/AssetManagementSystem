import socket
import pickle

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

