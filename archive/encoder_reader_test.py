"""!
@file encoder_reader_test.py
Run real or simulated dynamic response tests and plot the results. This program
demonstrates a way to make a simple GUI with a plot in it. It uses Tkinter, an
old-fashioned and ugly but useful GUI library which is included in Python by
default.

This file is based loosely on an example found at
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Jessica Perez, Jacquelyn Banh, and Nathan Chapman
@date   2024-02-06 Original program, based on example from above listed source
@copyright (c) 2024 by Jessica Perez, Jacquelyn Banh, and Nathan Chapman and released under the GNU Public Licenes V3
"""

import time
import pyb
from encoder_reader import Encoder
from motor_driver import MotorDriver

    
# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program
if __name__ == "__main__":
    
    # set up timer 4 for encoder 1
    TIM4 = pyb.Timer(4, prescaler=1, period=100000) # Timer 3, no prescalar, frequency 100kHz
    # set up timer 3 for encoder 2
    TIM3 = pyb.Timer(3, prescaler=1, period=100000) # Timer 3, no prescalar, frequency 100kHz
    # Define pin assignments for encoder 1
    pinb6 = pyb.Pin(pyb.Pin.board.PB6)
    pinb7 = pyb.Pin(pyb.Pin.board.PB7)
    #Define pin assignments for encoder 2
    pinc6 = pyb.Pin(pyb.Pin.board.PC6)
    pinc7 = pyb.Pin(pyb.Pin.board.PC7)
    # Create first encoder object
    Tom = Encoder(pinb6, pinb7, TIM4)
    Jerry = Encoder(pinc6, pinc7, TIM3)
    
    while True:
        time.sleep(0.01)
        Tom.read()

