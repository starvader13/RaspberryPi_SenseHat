from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    acc = sense.get_accelerometer_raw()
    x = acc['x']
    y = acc['y']
    z = acc['z']
   
    x=round(x,2)
    y=round(y,2)
    z=round(z,2)
   
    print("x = {0} , y = {1} , z = {2}".format(x,y,z))
   
    if x==1:
        sense.set_rotation(180)
    elif y==1:
        sense.set_rotation(90)
    elif y==-1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)