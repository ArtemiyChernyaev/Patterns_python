from abc import ABC, abstractmethod


class Product1(ABC):

    @abstractmethod
    def params(self):
        ...


class Product2(ABC):

    @abstractmethod
    def params(self):
        ...


class Product11(Product1):

    def __init__(self):
        self.__params = {'type': '1.1'}

    @property
    def params(self):
        return self.__params


class Product12(Product1):

    def __init__(self):
        self.__params = {'type': '1.2'}

    @property
    def params(self):
        return self.__params


class Product21(Product2):

    def __init__(self):
        self.__params = {'type': '2.1'}

    @property
    def params(self):
        return self.__params


class Product22(Product2):

    def __init__(self):
        self.__params = {'type': '2.2'}

    @property
    def params(self):
        return self.__params


class Factory(ABC):

    @abstractmethod
    def create_product1(self) -> Product1:
        ...

    @abstractmethod
    def create_product2(self) -> Product2:
        ...


class Factory1(Factory):

    def create_product1(self) -> Product11:
        return Product11()

    def create_product2(self) -> Product12:
        return Product12()


class Factory2(Factory):

    def create_product1(self) -> Product21:
        return Product21()

    def create_product2(self) -> Product22:
        return Product12()


def get_products(creator: Factory):
    print(creator.create_product1().params)
    print(creator.create_product2().params)


if __name__ == '__main__':
    fc1: Factory1 = Factory1()
    fc2: Factory2 = Factory2()

    get_products(fc1)
    get_products(fc2)
