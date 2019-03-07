import math


class calculations:

    def __init__(self, energy, life):
        self.energy = energy
        self.life = life

    def calcifon(self, currentradiation, minradiation, maxradiation):
       radiationRatio = (currentradiation-minradiation)/(maxradiation-minradiation)
       energyloss = radiationRatio * 5
       self.energy = self.energy-math.ceil(energyloss)

       return math.ceil(energyloss)

    def calcifoff(self, currentrad,minrad, maxrad,currenttemp,mintemp,maxtemp):
       temperatureRatio =(currenttemp-mintemp)/(maxtemp - mintemp)
       radiationRatio = (currentrad - minrad) / (maxrad - minrad)

       lifeloss = radiationRatio*5
       self.life = self.life - math.ceil(lifeloss)

       energygain = temperatureRatio * 5
       self.energy = self.energy + math.ceil(energygain)
       return lifeloss, energygain



#Testing
object1= calculations(energy= 10, life = 11)
energyloss = object1.calcifon(5, 3, 7)
energyloss, energygain = object1.calcifoff(currentrad=5, minrad=3, maxrad=7, currenttemp=8, mintemp=4, maxtemp=10)
