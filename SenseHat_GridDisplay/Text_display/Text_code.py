from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

sense.clear()
sense.low_light=True

g = (0,255,0)
r = (200,0,0)
w = (100,100,100)
e = (0,0,0)
b = (255,255,255)
red = (250,50,50)

def robo():
    paxi = [
        e, r, e, e, e, e, r, e,
        e, e, g, b, b, g, e, e,
        e, r, g, g, g, g, r, e,
        e, r, g, w, w, g, r, e,
        e, r, g, g, g, g, r, e,
        e, r, g, w, w, g, r, e,
        e, e, g, r, r, g, e, e,
        e, g, g, e, e, g, g, e
    ]
    return paxi

images = [robo]
count = 0

while(True):
    sense.set_pixels(images[count % len(images)]())
    sleep(1)
    count += 1
    sense.show_message("Starvader",scroll_speed=.09,text_colour=r,back_colour=w)
