"""!
@file encoder_reader.py
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
        self.timer.counter(0)
        self.previous = self.timer.counter()
        self.deltatot = 0
        
    def read(self):
        """!
        This method returns the current position of the
        motor using the encoder
        """
        print("Counter = ", self.timer.counter());
        self.current = self.timer.counter()
        self.delta = self.current - self.previous
        self.AR = int((0xFFFF + 1)/2)
        print("Delta = ", self.delta);
        if self.delta > self.AR: # check underflow
            self.delta -= self.AR # offset to correct underflow
        elif self.delta < -self.AR: # check overflow
            self.delta += self.AR # offset to correct overflow
        self.deltatot += self.delta
        print("Delta = ", self.delta);
        print("Delta Total = ", self.deltatot);
        self.previous = self.current
        
    def zero(self):
        """!
        This method sets the encoder count to zero at the
        current position of the motor
        """
        self.timer.counter(0)
        print ("Encoder count reset to zero")

# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program           
if __name__ == "__main__":
    # set up timer 4 for encoder 1
    TIM4 = pyb.Timer(4, prescaler=1, period=0xFFFF) # Timer 3, no prescalar, frequency 100kHz
    # set up timer 3 for encoder 2
    TIM3 = pyb.Timer(3, prescaler=1, period=0xFFFF) # Timer 3, no prescalar, frequency 100kHz
    # Define pin assignments for encoder 1
    pinb6 = pyb.Pin(pyb.Pin.board.PB6)
    pinb7 = pyb.Pin(pyb.Pin.board.PB7)
    #Define pin assignments for encoder 2
    pinc6 = pyb.Pin(pyb.Pin.board.PC6)
    pinc7 = pyb.Pin(pyb.Pin.board.PC7)
    # Create encoder objects
    Tom = Encoder(pinb6, pinb7, TIM4)
    Jerry = Encoder(pinc6, pinc7, TIM3)
    
    while True:
        time.sleep(0.01)
        Tom.read()
