"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel 


class Vehicle(ABC):
    """
    Абстрактный базовый класс для представления транспортных средств.
    
    Этот класс определяет общие атрибуты и поведение для всех типов 
    транспортных средств. Является абстрактным и требует реализации 
    конкретных методов в дочерних классах.
    
    Атрибуты класса:
        weight (int | float): Вес транспортного средства в килограммах. 
                            По умолчанию 0.
        started (bool): Флаг состояния двигателя. True - двигатель запущен,
                       False - заглушен. По умолчанию False.
        fuel (int | float): Количество топлива в баке в литрах. 
                           По умолчанию 0.
        fuel_consumption (int | float): Расход топлива в литрах на 100 км.
                                       По умолчанию 0.
    
    Особенности:
        - Класс абстрактный (ABC), нельзя создать экземпляр напрямую
        - Определяет общий интерфейс для всех транспортных средств
        - Реализация конкретной логики требуется в дочерних классах
    """
 

    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, started, fuel, fuel_consumption):
        super().__init__()
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()
    
    def move(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if self.fuel - fuel_needed < 0:
            raise NotEnoughFuel()
        else:
            self.fuel = self.fuel - fuel_needed

