import Addresses
import Client
import Server
import Functions
import time
import queue
import threading
from pprint import pprint


# pi1 will be the pi which communicates with the omron and sends the socket to pi3

# pi2 will be the same as pi1

#pi3 will act as a socket server to pi1 and pi2 and will send data to azure



# State Machine will be used to determine which pi will act as pi1, pi2 or pi 3

def stateMachine(state):

    states = ['pi1', 'pi2', 'pi3']

    # this state is for pi1 
    if (state == states[0]):
        Functions.ipAddressSet('192.168.250.11') # used for pi1
        time.sleep(3)
        address_dictionary = Addresses.loadConfig()
        

        while(1):
            connections_error = 0
            response = Functions.setup('192.168.250.1', 2, 1)
            time.sleep(1)


            while(type(response) == str):
                response = Functions.setup('192.168.250.1', 2, 1)
                connections_error += 1
                time.sleep(1)

                if(connections_error > 50):
                    return('Connection to Omron has failed')

            reading_dictionary = Functions.readMemoryAddressDict(address_dictionary)
            
            Client.clientSend('192.168.250.13', 1234, reading_dictionary)
            time.sleep(3)

    # this state is for pi3
    if (state == states[2]):

        Functions.ipAddressSet('192.168.250.13')
        time.sleep(3)

        # Use multithreading to allow other operations while wiating for client to connect
        # multithreading_queue = queue.Queue()

        while(1):

            message = Server.socketServer('192.168.250.13', 1234, 30)
            pprint(message)
            print('#' * 200)
            '''
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
            '''
stateMachine('pi1')
# stateMachine('pi3')
