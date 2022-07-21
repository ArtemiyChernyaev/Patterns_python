from abc import ABC, abstractmethod


class Product(ABC):
    
    @abstractmethod
    def release(self):
        pass


class ProductOne(Product):

    def release(self):
        return 'ProductOne release'


class ProductTwo(Product):

    def release(self):
        return 'ProductTwo release'


class Factory(ABC):

    @abstractmethod
    def create(self):
        pass


class FactoryOne(Factory):

    def create(self) -> 'ProductOne':
        return ProductOne()


class FactoryTwo(Factory):

    def create(self) -> 'ProductTwo':
        return ProductTwo()


creator: 'FactoryOne' = FactoryOne()
pr1: 'ProductOne' = creator.create()

creator: 'FactoryTwo' = FactoryTwo()
pr2: 'ProductTwo' = creator.create()

print(pr1.release())
print(pr2.release())
