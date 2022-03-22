from pprint import pprint
import time
import Functions
import Addresses
import Server
import threading
import queue
# import Client

# Functions.ipAddressSet()


# Dictionary which has all the memory addresses for each trigger
addressDict = Addresses.loadConfig()

# Use multithreading to allow other operations while wiating for client to connect
multithreading_queue = queue.Queue()

while(1):

    message = threading.Thread(
        target= Server.socketServerMultiThreading, 
        args= ('192.168.0.249', 1234, 20, multithreading_queue)
        )

    message.start()
    
    for i in range(5):
        print('this is working between threads')
        time.sleep(0.2)

    message.join(timeout=10)
    recieved_dictionary = multithreading_queue.get()

    pprint(recieved_dictionary)
    print('')


    





