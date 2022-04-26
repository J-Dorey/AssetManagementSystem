#from datetime import date, datetime
#from turtle import Turtle
#import fins.udp
import os
import yaml
#import random
#import pickle
#import csv
import Addresses
from pprint import pprint
import datetime
from aphyt import omron

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
    with open('OmronToRasp\config.yaml', 'r') as file:
        dictionary = yaml.safe_load(file)

    for k, v in dictionary.items():
        dictionary[k] = random.randrange(0, 100, 1)

    pprint(dictionary)

    return(dictionary)

# This function sets the ip address of the raspberry pi
def ipAddressSet(ipaddress):
    os.system('sudo ifconfig eth0 down')
    os.system('sudo ifconfig eth0 ' + ipaddress)
    os.system('sudo ifconfig eth0 up')

def saveToFile(file_name, dictionary):

    with open(file_name,'a', newline='') as file:

        dictionary['Time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        writer = csv.writer(file)
        values = dictionary.values()
        keys = dictionary.keys()

        #writer.writerow(keys)
        writer.writerow(values)
        file.close()


def omronConnectionSetup(omron_ipaddress):
    plc_connection = omron.n_series.NSeries()
    plc_connection.connect_explicit(omron_ipaddress)
    plc_connection.register_session()
    plc_connection.update_variable_dictionary()
    
    return(plc_connection)

# Main read function used to communicate with omron PLC 
 
def readPLCVariables(variable_dictionary):
            
    plc_connection = omronConnectionSetup('192.168.250.1')
    
    for k in variable_dictionary.keys():
        try:
            variable_dictionary[k] = plc_connection.read_variable(k)
        except:
            variable_dictionary[k] = 'N/A'
            
    plc_connection.close_explicit()
    
    return(variable_dictionary)
            
    
    
    
    
    
    
    

            

