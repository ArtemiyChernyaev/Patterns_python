class Investor:

    @staticmethod
    def invest():
        print('invest...')


class Vendor:

    @staticmethod
    def give():
        print('give...')


class Builder:

    @staticmethod
    def build():
        print('build...')


class BuildingProject:

    def __init__(self):
        self.investing: 'Investor' = Investor()
        self.giving: 'Vendor' = Vendor()
        self.building: 'Builder' = Builder()

    def realize(self, *, n_invest: int, n_give: int, n_build: int):
        [self.investing.invest() for _ in range(n_invest)]
        [self.giving.give() for _ in range(n_give)]
        [self.building.build() for _ in range(n_build)]


building_project: 'BuildingProject' = BuildingProject()
building_project.realize(n_invest=1, n_give=2, n_build=3)
