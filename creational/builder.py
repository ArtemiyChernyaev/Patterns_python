from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple


PizzaBase = namedtuple('PizzaBase', ['DoughDepth', 'DoughType'])


class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RYE = auto()


class PizzaSauceType(Enum):
    PESTO = auto()
    WHITE_GARLIC = auto()
    BARBEQUE = auto()
    TOMATO = auto()


class PizzaTopLevelType(Enum):
    MOZZARELLA = auto()
    SALAMI = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.cooking_time = None

    def __str__(self):
        info: str = f'Pizza name: {self.name}\n' \
                    f'dough type: {self.dough.DoughDepth.name}\n' \
                    f'{self.dough.DoughType.name}\n' \
                    f'sauce type: {self.sauce}\n' \
                    f'topping: {[i.name for i in self.topping]}\n' \
                    f'cooking time: {self.cooking_time} minutes'
        return info


class Builder(ABC):

    @abstractmethod
    def prepare_dough(self) -> None: pass

    @abstractmethod
    def add_sauce(self) -> None: pass

    @abstractmethod
    def ass_topping(self) -> None: pass

    @abstractmethod
    def get_pizza(self) -> Pizza: pass


class MargaritaPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza('Margarita')
        self.pizza.cooking_time = 15

    def prepare_dough(self) -> None:
        self.pizza.dough = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauceType.TOMATO

    def ass_topping(self) -> None:
        self.pizza.topping.extend(
            [
                it for it in (PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.BACON)
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza


class SalamiPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza('Salami')
        self.pizza.cooking_time = 10

    def prepare_dough(self) -> None:
        self.pizza.dough = PizzaBase(PizzaDoughDepth.THIN, PizzaDoughType.RYE)

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauceType.BARBEQUE

    def ass_topping(self) -> None:
        self.pizza.topping.extend(
            [
                it for it in (PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.SALAMI)
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza


class Director:

    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_pizza(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.ass_topping()


if __name__ == '__main__':
    director = Director()
    for it in (MargaritaPizzaBuilder, SalamiPizzaBuilder):
        builder = it()
        director.set_builder(builder)
        director.make_pizza()
        pizza = builder.get_pizza()
        print(pizza)
        print('------------------------')
