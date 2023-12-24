# Gyro Sensor

**The Gyro Sensor present on the SenseHat can be used to get the cordinates of the Sensehat, but not just that these cordinates can be printed on terminal in realtime which means it keeps on updating as the SenseHat moves**.

**The given code in this directory will help you to print the cordinates**

***To geth the cordinates the function ```get_acceloremeter_raw()``` is used which is further used to access different axes-cordinates i.e x,y and z***
```
acc = sense.get_accelerometer_raw()
    x = acc['x']
    y = acc['y']
    z = acc['z']
```