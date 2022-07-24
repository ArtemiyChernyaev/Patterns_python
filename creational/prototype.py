class Class:

    def __init__(self, prototype: 'Class' = None):
        if prototype:
            self.attr1 = prototype.attr1
            self.attr2 = prototype.attr2

    def clone(self):
        return Class(self)


if __name__ == '__main__':
    obj1 = Class()

    obj1.attr1 = 10
    obj1.attr2 = 20

    obj2 = obj1.clone()
    obj2.attr1 = 666

    print(obj1.__dict__)
    print(obj2.__dict__)