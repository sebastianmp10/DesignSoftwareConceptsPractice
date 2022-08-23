from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass


class Bombilla(Switchable):
    def turn_on(self):
        print("Bombilla: truned on...")

    def turn_off(self):
        print("Bombilla: turned off...")

class Ventilador(Switchable):
    def turn_on(self):
        print("Ventilador: truned on...")

    def turn_off(self):
        print("Ventilador: turned off...")

class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False

        else:
            self.client.turn_on()
            self.on = True

l = Bombilla()
f = Ventilador()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()