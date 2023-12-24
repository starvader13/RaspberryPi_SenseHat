from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

g = (0,255,0)
r = (200,0,0)
w = (100,100,100)
e = (0,0,0)
b = (255,255,255)

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

sense.set_pixels(paxi)