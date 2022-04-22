# This is the main file which will perform the communication with the Omron PLC and the raspberry pi

from ast import Add
from logging.config import valid_ident
from aphyt import omron
import time
import Addresses 
from pprint import pprint
import Functions

def main(variable_dictionary, plc_connection):

    for k in variable_dictionary.keys():
        try:
            variable_dictionary[k] = plc_connection.read_variable(k)
        except:
            variable_dictionary[k] = 'N/A'

        return(variable_dictionary)

variable_dictionary = Addresses.loadConfig('M188config.yaml')
plc_connection = Functions.omronConnectionSetup('192.168.250.1')

while(1):
    variable_dictionary = main(variable_dictionary, plc_connection)
    pprint(variable_dictionary)
    time.sleep(2)