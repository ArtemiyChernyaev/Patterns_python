from abc import ABC, abstractmethod


class SingletonBaseClass(ABC):

    @abstractmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class SingletonClassOne(SingletonBaseClass):
    _instance = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


class SingletonClassTwo(SingletonBaseClass):
    _instance = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


obj11 = SingletonClassOne()
obj12 = SingletonClassOne()

obj21 = SingletonClassTwo()
obj22 = SingletonClassTwo()

print(f'id obj11 {id(obj11)}')
print(f'id obj12 {id(obj12)}')
print(f'id obj21 {id(obj21)}')
print(f'id obj22 {id(obj22)}')