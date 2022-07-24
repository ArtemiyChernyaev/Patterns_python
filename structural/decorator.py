from abc import ABC, abstractmethod


class IProcessor(ABC):

    @abstractmethod
    def process(self):
        ...


class Transmitter(IProcessor):

    def __init__(self, data: str):
        self.__data = data

    def process(self):
        print('The data {} is transmitted over the communication channel'.format(self.__data))


class Shell(IProcessor):

    def __init__(self, pr: IProcessor):
        self._processor = pr

    @abstractmethod
    def process(self):
        ...


class HammingCoder(Shell):

    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print('A noise-resistant hamming code has been applied->', end='')
        self._processor.process()


class Encryptor(Shell):

    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print('Data encryption->', end='')
        self._processor.process()


if __name__ == '__main__':
    transmitter: Transmitter = Transmitter('12345')
    transmitter.process()
    print()

    hamming_coder: HammingCoder = HammingCoder(transmitter)
    hamming_coder.process()
    print()

    encryptor: Shell = Encryptor(hamming_coder)
    encryptor.process()

