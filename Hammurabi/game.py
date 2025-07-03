class Game:
    def __init__(self):
        self._id = 0
        self._year = 1

        self._people_starved = 0
        self._people_to_city = 0
        self._city_population = 100
        self._city_acres = 1000
        self._harvest_units = 3
        self._rats_units = 200
        self._price_acre = 20
        self._grain_stocks = 2800

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def people_starved(self):
        return self._people_starved

    @people_starved.setter
    def people_starved(self, value):
        self._people_starved = value

    @property
    def people_to_city(self):
        return self._people_to_city

    @people_to_city.setter
    def people_to_city(self, value):
        self._people_to_city = value

    @property
    def city_population(self):
        return self._city_population

    @city_population.setter
    def city_population(self, value):
        self._city_population = value

    @property
    def city_acres(self):
        return self._city_acres

    @city_acres.setter
    def city_acres(self, value):
        self._city_acres = value

    @property
    def harvest_units(self):
        return self._harvest_units

    @harvest_units.setter
    def harvest_units(self, value):
        self._harvest_units = value

    @property
    def rats_units(self):
        return self._rats_units

    @rats_units.setter
    def rats_units(self, value):
        self._rats_units = value

    @property
    def price_acre(self):
        return self._price_acre

    @price_acre.setter
    def price_acre(self, value):
        self._price_acre = value

    @property
    def grain_stocks(self):
        return self._grain_stocks

    @grain_stocks.setter
    def grain_stocks(self, value):
        self._grain_stocks = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Game: id={self.id}, year={self.year}, people_starved={self.people_starved}, people_to_city={self.people_to_city}, city_population={self.city_population}, city_acres={self.city_acres}, harvest_units={self.harvest_units}, rats_units={self.rats_units}, price_acre={self.price_acre}, grain_stocks={self.grain_stocks}"