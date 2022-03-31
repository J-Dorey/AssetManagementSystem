from curses import baudrate
import time
import serial
import pickle
from pprint import pprint 

def UARTSetup():
    ser = serial.Serial(
        port = '/dev/serial0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 10
    )

    return(ser)

# funciton to send data to raspberry pi using pins 14 and 15
def UARTTxDic(serial_info_struct, dictionary):
    dicbyte = pickle.dumps(dictionary)
    serial_info_struct.write(dicbyte)
    serial_info_struct.write(b'END')

# function to recieve a dictionary over UART
def UARTRxDic(serial_info_struct):
    dicbyte = serial_info_struct.read_until(b'END') 
    dicitonary = pickle.loads(dicbyte)
    pprint(dicitonary)

    return(dicitonary)
