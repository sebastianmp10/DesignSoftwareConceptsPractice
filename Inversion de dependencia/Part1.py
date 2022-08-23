class Bombilla:
    def turn_on(self):
        print("Bombilla: turned on...")

    def turn_off(self):
        print("Bombilla: turned off...")


class ElectricPowerSwitch:

    def __init__(self, l: Bombilla):
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True


l = Bombilla()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()