from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

while True:
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":
        sense.show_letter("U")
      if event.direction == "down":
        sense.show_letter("D")
      if event.direction == "left":
        sense.show_letter("L")
      if event.direction == "right":
        sense.show_letter("R")
      if event.direction == "middle":
        sense.show_letter("M")
    time.sleep(0.5)
    sense.clear()
