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

    
# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program
if __name__ == "__main__":# set up timer 3
    TIM3 = pyb.Timer(3, freq=2000) # Timer 3, frequency 2000Hz
    # Define pin assignments for motor 1
    ENA = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    IN1A = pyb.Pin(pyb.Pin.board.PB4)
    IN2A = pyb.Pin(pyb.Pin.board.PB5)


    # Create motor drivers
    moe = MotorDriver(ENA, IN1A, IN2A, TIM3)
    while True:
        moe.set_duty_cycle (100)				#Forward at 50% duty cycle
        time.sleep(2)						#Sleeps for 2 seconds
        moe.set_duty_cycle (-50)			#Reverse at 50% duty cycle
        time.sleep(2)						#Sleeps for 2 seconds
        moe.set_duty_cycle (50)			#Reverse at 50% duty cycle
        time.sleep(2)
        moe.set_duty_cycle (0)				#Stops the duty cycle
        time.sleep(2)						#Sleeps for 2 seconds



