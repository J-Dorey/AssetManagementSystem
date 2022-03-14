from pprint import pprint
from random import randint, random
import re
import time

from janus import Queue
import Functions
import Addresses
import Server
import threading
import queue
# import Client

# Functions.ipAddressSet()
'''
time.sleep(2)
response = Functions.setup('192.168.250.1', 20, 1)

while(type(response) == str):
    response = Functions.setup('192.168.250.1', 20, 1)
    time.sleep(1)
'''


# Dictionary which has all the memory addresses for each trigger
addressDict = Addresses.loadConfig()
multithreading_queue = queue.Queue()

while(1):
    '''
    readingDict = Functions.readMemoryAddressDict(addressDict)
    print(readingDict.values())
    time.sleep(1)
    '''
    message = threading.Thread(
        target= Server.socketServerMultiThreading, 
        args= ('192.168.20.39', 1234, 20, multithreading_queue))
    # message = Server.socketServerMultiThreading('192.168.20.39', 1234, 20)
    message.start()
    for i in range(7):
        print('this is working between threads')
        time.sleep(1)

    message.join()
    recieved_dictionary = multithreading_queue.get()

    pprint(recieved_dictionary)
    print('')


    





