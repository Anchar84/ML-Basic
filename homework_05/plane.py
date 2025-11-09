"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    max_cargo: int
    cargo = 0

    def __init__(self, weight, started, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo: int):
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload()
        else:
            self.cargo = self.cargo + cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo