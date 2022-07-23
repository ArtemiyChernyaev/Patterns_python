from typing import List, Dict


class Shared:

    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:

    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passport = passport

    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passport


class Flyweight:

    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print('Displaying new data: common - {}_{}'.format(self.__shared.company, self.__shared.position),
              'and unique {}_{}'.format(unique.name, unique.passport))

    def get_data(self):
        return self.__shared.company + '_' + self.__shared.position


class FlyweightFactory:

    def get_key(self, shared: Shared):
        return '{}_{}'.format(shared.company, shared.position)

    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_flyweight(self, shared: Shared):
        key: str = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            print('Flyweight factory: Common object by key' + key + 'not found. Сreating a new one.')
            self.__flyweights[key] = Flyweight(shared)
        else:
            print('Flyweight factory: Extracting data from existing records by key' + key + '.')
        return self.__flyweights[key]

    def list_flyweights(self):
        count: int = len(self.__flyweights)
        print('\nFlyweight factory: There are {} entries in total'.format(count))
        for pair in self.__flyweights.values():
            print(pair.get_data())


def add_specialist_database(
                            ff: FlyweightFactory,
                            company: str,
                            position: str,
                            name: str,
                            passport: str):
    print()
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))


shared_list: List[Shared] = [
                            Shared('Microsoft', 'CEO'),
                            Shared('Google', 'Anroid-developer'),
                            Shared('Google', 'IOS-developer'),
                            Shared('Apple', 'Web-developer')]

factory = FlyweightFactory(shared_list)
factory.list_flyweights()

add_specialist_database(
                        factory,
                        'Google',
                        'Web-developer',
                        'John',
                        'AM-5132654')

add_specialist_database(
                        factory,
                        'Apple',
                        'CEO',
                        'Alex',
                        'DM-5654774')

factory.list_flyweights()