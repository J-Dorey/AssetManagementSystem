from random import randint, random
import time
import Functions
import Addresses
import Server
import Server
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

while(1):
    '''
    readingDict = Functions.readMemoryAddressDict(addressDict)
    print(readingDict.values())
    time.sleep(1)
    '''

    message = Server.socketServer('192.168.0.249', 1234, 20)

    for k, v in message.items():
        message[k] = randint(0,100)
        print(k,':', message[k])
    
    print('.' * 100)

    





