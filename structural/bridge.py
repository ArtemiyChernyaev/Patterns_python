from abc import ABC, abstractmethod


class DataReader(ABC):

    @abstractmethod
    def read(self):
        pass


class FileReader(DataReader):

    def read(self):
        print('FileReader')


class DatabaseReader(DataReader):

    def read(self):
        print('DatabaseReader')


class Sender(ABC):

    def __init__(self, data_reader: 'DataReader'):
        self.reader: 'DataReader' = data_reader

    def set_data_reader(self, data_reader: 'DataReader'):
        self.reader: 'DataReader' = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(Sender):

    def __init__(self, data_reader: 'DataReader'):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('Send via Email')


class TgBotSender(Sender):

    def __init__(self, data_reader: 'DataReader'):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('Send via TgBot')


sender: 'Sender' = EmailSender(DatabaseReader())
sender.send()

sender.set_data_reader(FileReader())
sender.send()

sender = TgBotSender(DatabaseReader())
sender.send()