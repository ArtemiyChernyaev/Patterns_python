class ObjPool:

    def __init__(self, number: int):
        self._objects = [Obj() for _ in range(number)]

    def acquire(self) -> 'Obj':
        return self._objects.pop()

    def release(self, obj: 'Obj'):
        self._objects.append(obj)


class Obj:
    pass


object_pool: 'ObjPool' = ObjPool(10)
obj: 'Obj' = object_pool.acquire()
object_pool.release(obj)
