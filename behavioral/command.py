from abc import ABC, abstractmethod
from typing import List


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        ...


class Assistant:

    def prepare_pizza_dough(self):
        print('Assistant prepares pizza dough')

    def prepare_topping(self):
        print('Assistant prepares pizza topping')

    def prepare_sauce(self):
        print('Assistant prepares pizza sauce')


class Oven:

    def prepare_oven(self):
        print('The oven is heating up')

    def cooking_pizza(self):
        print('Pizza is cooked in the oven')


class Chief:

    def make_pizza_base(self):
        print('Chef rolls out the pizza base')

    def applied_sauce(self):
        print('Chef puts sauce on pizza base')

    def add_topping_to_pizza(self):
        print('Chef adds toppings to pizza')

    def bon_appetit(self):
        print('The chef wishes the client a pleasant appetite!')


class PrepareOvenCommand(Command):

    def __init__(self, executor: Oven):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_oven()


class PrepareDoughCommand(Command):

    def __init__(self, executor: Assistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_pizza_dough()


class PrepareToppingCommand(Command):

    def __init__(self, executor: Assistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_topping()


class PrepareSauceCommand(Command):

    def __init__(self, executor: Assistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_sauce()


class CookingPizzaCommand(Command):

    def __init__(self, executor: Oven):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking_pizza()


class MakePizzaBaseCommand(Command):

    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_pizza_base()


class AppliedSauceCommand(Command):

    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.applied_sauce()


class AddToppingCommand(Command):

    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping_to_pizza()


class BonAppetitCommand(Command):

    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.bon_appetit()


class Pizzeria:

    def __init__(self):
        self.history: List[Command] = []

    def add_command(self, command: Command) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print('The order of execution of pizza',
                  'preparation commands is not set')
        else:
            [executor.execute() for executor in self.history]
        self.history.clear()


if __name__ == '__main__':
    chief = Chief()
    assistant = Assistant()
    stove = Oven()
    pizzeria = Pizzeria()

    pizzeria.add_command(PrepareDoughCommand(assistant))
    pizzeria.add_command(MakePizzaBaseCommand(chief))
    pizzeria.add_command(PrepareSauceCommand(assistant))
    pizzeria.add_command(AppliedSauceCommand(chief))
    pizzeria.add_command(PrepareOvenCommand(stove))
    pizzeria.add_command(PrepareToppingCommand(assistant))
    pizzeria.add_command(AddToppingCommand(chief))
    pizzeria.add_command(CookingPizzaCommand(stove))
    pizzeria.add_command(BonAppetitCommand(chief))

    pizzeria.cook()
