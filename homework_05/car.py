"""
Создайте класс `Car`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine

class Cal(Vehicle):
    engine: Engine


    def __init__(self, weight, started, fuel, fuel_consumption):
        super().__init__(weight, started, fuel, fuel_consumption)

    def set_endine(self, engine: Engine):
        self.engine = engine