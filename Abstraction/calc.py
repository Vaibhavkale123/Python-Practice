from abc import ABC, abstractmethod

class Calculator:
    @abstractmethod
    def addition(self):
        pass
    @abstractmethod
    def subtraction(self):
        pass

    @abstractmethod
    def multiplicaition(self):
        pass
    @abstractmethod
    def division(self):
        pass