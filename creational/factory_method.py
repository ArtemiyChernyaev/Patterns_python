from abc import ABC, abstractmethod


class Product(ABC):
    
    @abstractmethod
    def release(self):
        ...


class ProductOne(Product):

    def release(self):
        return 'ProductOne release'


class ProductTwo(Product):

    def release(self):
        return 'ProductTwo release'


class Factory(ABC):

    @abstractmethod
    def create(self):
        ...


class FactoryOne(Factory):

    def create(self) -> ProductOne:
        return ProductOne()


class FactoryTwo(Factory):

    def create(self) -> ProductTwo:
        return ProductTwo()


if __name__ == '__main__':
    creator: FactoryOne = FactoryOne()
    pr1: ProductOne = creator.create()

    creator: FactoryTwo = FactoryTwo()
    pr2: ProductTwo = creator.create()

    print(pr1.release())
    print(pr2.release())
