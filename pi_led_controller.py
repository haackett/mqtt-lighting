### CONFIG ###

#Pin numbers.
RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

### END ###

import sys
import pigpio
import time


class PiLedController():

    def __init__(self):
        self.pi = pigpio.pi()
        self.redPin = RED_PIN
        self.greenPin = GREEN_PIN
        self.bluePin = BLUE_PIN
        self.bright = 255

    def setPin(self, pin, brightness):
        realBrightness = int(int(self.__roundBrightness(brightness)) * (float(self.bright) / 255.0))
        print(" settings pin " + str(pin) + " to " + str(realBrightness))
        #self.pi.set_PWM_dutycycle(pin, realBrightness)

    def __roundBrightness(self, brightness):
        if brightness > 255:
            return 255
        if brightness < 0:
            return 0
        return brightness
    
    def close(self):
        time.sleep(0.5)
        self.pi.stop()


