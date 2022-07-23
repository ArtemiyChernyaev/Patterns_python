from abc import ABC, abstractmethod
from enum import Enum


class ChiefMood(Enum):
    GOOD = 1
    BAD = 2
    BETTER_STAY_AWAY = 3


class Strategy(ABC):

    @abstractmethod
    def check_mood_chief(self, mood: ChiefMood) -> bool:
        pass

    @abstractmethod
    def order_processing(self, money: int) -> str:
        pass


class GoodStrategy(Strategy):

    def check_mood_chief(self, mood: ChiefMood) -> bool:
        if (mood is ChiefMood.GOOD or
                mood is ChiefMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return 'The best drink possible!'


class BadStrategy(Strategy):

    def check_mood_chief(self, mood: ChiefMood) -> bool:
        if (mood is ChiefMood.BETTER_STAY_AWAY or
                mood is ChiefMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return 'And a glass of water will do!'


class NormalStrategy(Strategy):

    def check_mood_chief(self, mood: ChiefMood) -> bool:
        return True

    def order_processing(self, money: int) -> str:
        if money < 5:
            return 'Politely refuse the customer\'s order'
        elif money < 10:
            return 'Prepare espresso'
        elif money < 20:
            return 'Make a cappuccino'
        elif money < 50:
            return 'Make excellent coffee'
        else:
            return 'The best drink possible!'


class Barista:
    def __init__(self, strategy: Strategy,
                 chief_mood: ChiefMood):
        self._strategy = strategy
        self._chief_mood = chief_mood
        print(f'The initial mood of the boss: {chief_mood.name}')

    def get_chief_mood(self) -> ChiefMood:
        return self._chief_mood

    def set_chief_mood(self, chief_mood: ChiefMood) -> None:
        print(f'The current mood of the boss: {chief_mood.name}')
        self._chief_mood = chief_mood

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def take_order(self, money: int) -> None:
        print(f'The customer pays for the order {money} rubles')
        if self._strategy.check_mood_chief(self._chief_mood):
            print(self._strategy.order_processing(money))
        else:
            print('Pretend not to notice the customer!')


if __name__ == "__main__":
    barista = Barista(NormalStrategy(),
                      ChiefMood.BETTER_STAY_AWAY)
    barista.take_order(20)
    barista.take_order(50)
    barista.set_strategy(BadStrategy())
    barista.take_order(40)
    barista.take_order(200)
    barista.set_strategy(GoodStrategy())
    barista.take_order(40)
    barista.set_chief_mood(ChiefMood.GOOD)
    barista.take_order(0)
