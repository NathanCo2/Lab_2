"""!
@file motor_driver.py
Run real or simulated dynamic response tests and plot the results. This program
demonstrates a way to make a simple GUI with a plot in it. It uses Tkinter, an
old-fashioned and ugly but useful GUI library which is included in Python by
default.

This file is based loosely on an example found at
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Jessica Perez, Jacquelyn Banh, and Nathan Chapman
@date   2024-01-30 Original program, based on example from above listed source
@copyright (c) 2024 by Jessica Perez, Jacquelyn Banh, and Nathan Chapman and released under the GNU Public Licenes V3
"""

import pyb
import time

class Encoder:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, ch1pin, ch2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param ch1pin: Pin for reading encoder channel 1
        @param ch2pin: Pin for reading encoder channel 2
        @param timer: Timer object for reading encoder
        """
        print ("Creating an encoder reader")
        self.timer = timer
        self.en1 = timer.channel(1, pyb.Timer.ENC_AB, pin=ch1pin) #sets up ch 1 for encoder counting mode on ch1pin
        self.en2 = timer.channel(2, pyb.Timer.ENC_AB, pin=ch2pin) #sets up ch 2 for encoder counting mode on ch2pin
        
    def read(self):
        """!
        This method returns the current position of the
        motor using the encoder
        """
        print("Counter = ", self.timer.counter());
        
    def zero(self):
        """!
        This method sets the encoder count to zero at the
        current position of the motor
        """
        print (f"Setting duty cycle to {level}")

# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program           
if __name__ == "__main__":
    # set up timer 3
    TIM3 = pyb.Timer(3, prescaler=1, period=100000) # Timer 3, no prescalar, frequency 100kHz
    # Define pin assignments for motor 1
    pinc6 = pyb.Pin(pyb.Pin.board.PC6)
    pinc7 = pyb.Pin(pyb.Pin.board.PC7)
    # Create first encoder object
    Tom = Encoder(pinc6, pinc7, TIM3)
    
    while True:
        time.sleep(1)
        Tom.read()