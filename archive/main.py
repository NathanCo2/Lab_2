
from motor_driver import MotorDriver
from encoder_reader import Encoder
import pyb
import time


# set up timer 4 for encoder 1
TIM4 = pyb.Timer(4, prescaler=1, period=0xFFFF) # Timer 4, no prescalar, frequency 100kHz
# set up timer 8 for encoder 2
TIM8 = pyb.Timer(8, prescaler=1, period=0xFFFF) # Timer 8, no prescalar, frequency 100kHz
# Define pin assignments for encoder 1
pinb6 = pyb.Pin(pyb.Pin.board.PB6)
pinb7 = pyb.Pin(pyb.Pin.board.PB7)
#Define pin assignments for encoder 2
pinc6 = pyb.Pin(pyb.Pin.board.PC6)
pinc7 = pyb.Pin(pyb.Pin.board.PC7)
# Create first encoder object
Tom = Encoder(pinb6, pinb7, TIM4)
Jerry = Encoder(pinc6, pinc7, TIM8)

# setup motor
TIM3 = pyb.Timer(3, freq=2000) # Timer 3, frequency 2000Hz
# Define pin assignments for motor 1
pina10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
pinb4= pyb.Pin(pyb.Pin.board.PB4)
pinb5 = pyb.Pin(pyb.Pin.board.PB5)

# Create motor drivers
moe = MotorDriver(pina10, pinb4, pinb5, TIM3)
while True:
    moe.set_duty_cycle (-50)#Reverse at 50% duty cycle
    #read encoder 20times for 20 seconds
    time.sleep(0.01)
    Tom.read()
    #change to different duty cycle
#     moe.set_duty_cycle (50)
#     #read encoder 20 times for 20 sec
#     time.sleep(0.5)
#     Tom.read()

