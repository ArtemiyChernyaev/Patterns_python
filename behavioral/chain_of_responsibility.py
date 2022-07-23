from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def set_next_worker(self, worker: 'Worker') -> 'Worker':
        pass

    @abstractmethod
    def execute(self, command: str) -> str:
        pass


class Laborer(Worker):

    def __init__(self):
        self.__next_worker: Worker = None

    def set_next_worker(self, worker: Worker) -> Worker:
        self.__next_worker = worker
        return worker

    def execute(self, command: str) -> str:
        if self.__next_worker:
            return self.__next_worker.execute(command)
        return ''


class Designer(Laborer):

    def execute(self, command: str) -> str:
        if command == 'Design a house':
            return 'The designer executed the command ' + command
        else:
            return super().execute(command)


class Carpenter(Laborer):

    def execute(self, command: str) -> str:
        if command == 'Laying bricks':
            return 'The carpenter executed the command ' + command
        else:
            return super().execute(command)


class FinishingWorker(Laborer):

    def execute(self, command: str) -> str:
        if command == 'Glue wallpaper':
            return 'The finishing worker executed the command ' + command
        else:
            return super().execute(command)


def give_command(worker: Worker, command: str):
    string: str = worker.execute(command)
    if not string:
        print(command + ' - no one knows how to do it')
    else:
        print(string)


designer = Designer()
carpenters = Carpenter()
finishingWorker = FinishingWorker()

designer.set_next_worker(carpenters).set_next_worker(finishingWorker)

give_command(designer, 'Design a house')
give_command(designer, 'Laying bricks')
give_command(designer, 'Glue wallpaper')

give_command(designer, 'Сonduct wires')
