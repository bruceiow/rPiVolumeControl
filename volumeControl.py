from RPi import GPIO
from time import sleep
import alsaaudio

clk = 22
dt = 23
#These are the GPIO numbers for the clk and dt pins from the encoder

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
m = alsaaudio.Mixer()
vol = m.getvolume()
vol1 = iter(vol)
counter = vol1.next()
clkLastState = GPIO.input(clk)

try:
      while True:
              clkState = GPIO.input(clk)
              dtState = GPIO.input(dt)
              if clkState != clkLastState:
                  if dtState != clkState:
                    if counter < 96:
                      counter += 4
                  else:
                    if counter > 4:
                      counter -= 4
                  m.setvolume(counter)
              clkLastState = clkState
              sleep(0.01)
finally:
      GPIO.cleanup()
