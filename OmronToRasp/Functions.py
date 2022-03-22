import fins.udp
import os
import yaml
import random
import pickle
import csv

# Function to setup connection to Omron PLC
def setup(ip_address, destination_node, source_node):

    global omron

    omron = fins.udp.UDPFinsConnection()
    omron.connect(ip_address)
    omron.srce_node_add = destination_node
    omron.dest_node_add = source_node

    response = omron.cpu_unit_status_read()
    print(type(response))  # prints the model number and version of CPU unit
    print(type(response) == str)
    return(response)


# This function will read the specified address of the omron
def readMemoryAddress(address):

    value = omron.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD, address)
    print(address)
    print(value)
    return(value[14:16])


def readMemoryAddressDict(addressDict):
    readingDict = addressDict.copy()

    for k, v in readingDict.items():
        value = omron.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD, v)
        readingDict[k] = int.from_bytes(value[14:16], "big")
        print(v)

    return(readingDict)


# This function converts the hexadecimal value into decimal.
def conversion(hexValue, varName):

    result = int.from_bytes(hexValue, "big")
    print(varName, result)


'''
The mitchDummyData function will load the dictionary and set the values for
each key to a random integer between 0 and 100
'''


def mitchDummyData():
    with open('config.yaml', 'r') as file:
        dictionary = yaml.safe_load(file)

    for k, v in dictionary.items():
        dictionary[k] = random.randrange(0, 100, 1)

    return(dictionary)

# This function sets the ip address of the raspberry pi
def ipAddressSet(ipaddress):
    os.system('sudo ifconfig eth0 down')
    os.system('sudo ifconfig eth0 ' + ipaddress)
    os.system('sudo ifconfig eth0 up')

def saveToFile(file_name, dictionary):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow()

