from sense_hat import SenseHat	#importing sensehat function
import time	#inmporting time module

sense = SenseHat()
sense.clear()	#to clear output on the sensehat grid

#creating functions for different colours 

def red():
    sense.clear(255,0,0)

def green():
    sense.clear(0,255,0)

def blue():
    sense.clear(100,100,0)
 
def temp():
    sense.clear(100,100,0)

#assigning colour for every joystick direction

sense.stick.direction_up = red
sense.stick.direction_down = green
sense.stick.direction_left = blue
sense.stick.direction_right = temp
sense.stick.direction_middle = sense.clear()

while True:
    pass
