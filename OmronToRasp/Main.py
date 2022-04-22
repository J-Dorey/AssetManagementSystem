# This is the main file which will perform the communication with the Omron PLC and the raspberry pi

from ast import Add
from logging.config import valid_ident
from aphyt import omron
import time
import Addresses 
from pprint import pprint

def main(omron_ipaddress):
    plc_connection = omron.n_series.NSeries()
    plc_connection.connect_explicit(omron_ipaddress)
    plc_connection.register_session()
    plc_connection.update_variable_dictionary()

    variable_dictionary = Addresses.loadConfig()

    while(1):
        for k in variable_dictionary.keys():
            try:
                variable_dictionary[k] = plc_connection.read_variable(k)
            except:
                vairable_dictionary[k] = 'N/A'

        pprint(variable_dictionary)
        time.sleep(2)

main('192.168.250.1')