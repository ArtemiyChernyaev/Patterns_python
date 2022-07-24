from abc import ABC, abstractmethod


class ObjectBase(ABC):

    @abstractmethod
    def object_method(self):
        ...


class Object(ObjectBase):

    def object_method(self):
        print('this is an object')


class ProxyObject(ObjectBase):

    def __init__(self):
        self.object = Object()

    def object_method(self):
        print('this is an proxy object')
        self.object.object_method()


if __name__ == '__main__':
    o1: Object = Object()
    o1.object_method()

    o2: ProxyObject = ProxyObject()
    o2.object_method()
