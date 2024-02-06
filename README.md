# Lab_2
ME 405-04 with Dr. Ridgely

Members: Jacquelyn Banh, Nathan Chapman, Jessica Perez

Tub: mecha06

Lab 02 Program Description:

The goal of this lab is to set up an encoder to be able to read motor position. An Encoder Reader class sets up an encoder object using two pins and the corresponding timer. The timer is set up in encoder counting mode and reads the two pins of the encoder, returning the encoder value. The read() method measures the delta and uses an algorithm to correct overflow and underflow, then adds it to a delta total that will allow us to measure the absolute position of the motor. The test block is set up to measure the encoder connected to pin B6 and B7 using Timer 4.
