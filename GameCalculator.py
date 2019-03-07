import math


class calculations:

    def __init__(self, energy, life):
        self.energy = energy
        self.life = life
        self.counter = 0

    def calc_if_on(self, currentradiation, minradiation, maxradiation):
        radiationRatio = float(currentradiation - minradiation) / float(maxradiation - minradiation)
        energyloss = radiationRatio * 5
        return math.ceil(energyloss)

    def calc_if_off(self, currentrad, minrad, maxrad, currenttemp, mintemp, maxtemp):
        temperatureRatio = (currenttemp - mintemp) / float(maxtemp - mintemp)
        radiationRatio = (currentrad - minrad) / float(maxrad - minrad)
        lifeloss = radiationRatio * 5
        energygain = temperatureRatio * 5
        return math.ceil(lifeloss), math.ceil(energygain)

    def make_decision_turn_on_shield(self, energy_gain_ceiled, loss_ceiled):
            if(self.counter == 1):
                self.counter = 0
                return True
            else:
                self.counter = 1
                return False


    def make_change(self, energy_gain_ceiled, loss_celied, is_on):
        if is_on:  # If shield if on.
            self.energy = self.energy - loss_celied
        else:
            self.energy = self.energy + energy_gain_ceiled
            self.life = self.life - loss_celied










