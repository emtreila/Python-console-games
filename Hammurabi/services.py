import random

from hammurabi.game import Game
from hammurabi.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self._repo = repo

    def start_game(self):
        self._repo.start_game()

    def get_current_game(self) -> Game:
        return self._repo.current_game

    def update_year(self, value):
        self._repo.current_game.year = value

    def sell_land(self, acres_to_sell):
        """
        Sell the land
        :param acres_to_sell: how many acres of land are sold
        """
        new_acres = self.get_current_game().city_acres - acres_to_sell
        stocks = self.get_current_game().grain_stocks + acres_to_sell * self.get_current_game().price_acre

        self._repo.current_game.city_acres = new_acres
        self._repo.current_game.grain_stocks = stocks

    def buy_land(self, acres_to_buy):
        """
        Buy the land
        :param acres_to_buy: how many acres of land are bought
        """
        new_acres = self.get_current_game().city_acres + acres_to_buy
        stocks = self.get_current_game().grain_stocks - acres_to_buy * self.get_current_game().price_acre

        self._repo.current_game.city_acres = new_acres
        self._repo.current_game.grain_stocks = stocks

    def change_price(self):
        """
        Changes the price for the land
        :return: the new price
        """
        self.get_current_game().price_acre = random.randint(15, 25)

    def feed_population(self, feed_population):
        """
        Feed the population
        :param feed_population: the population that is fed
        """
        self.get_current_game().grain_stocks -= feed_population
        self.get_current_game().people_starved = self.get_current_game().city_population - feed_population // 20
        self.get_current_game().city_population -= self.get_current_game().people_starved


    def check_population_starved(self, feed_population):
        """
        Check if the population is starved
        :param feed_population: the population that is fed
        :return: True = the population did not starve
                    False = the population starved
        """
        people_fed = feed_population // 20
        city_population = self.get_current_game().city_population
        if people_fed <= city_population // 2:
            return False
        return True

    def new_people_to_city(self, feed_population):
        """
        Checking if people can come to the city
        Adds people to the city if all population is fed

        :param feed_population: the population that is fed
        """
        people_fed = feed_population // 20
        city_population = self.get_current_game().city_population
        if people_fed != city_population:
            return

        people_coming = random.randint(1, 10)
        self.get_current_game().city_population += people_coming

    def people_to_city(self):
        """
        Returns the number of people coming to the city
        :return: number of people coming to the city
        """

        return people_coming

    def harvest(self, acres_to_plant):
        """
        Harvest the grain from the acres
        :param acres_to_plant: the acres that can be harvested
        """
        population_can_harvest = self.get_current_game().city_population * 10
        if  acres_to_plant > population_can_harvest:
            self.get_current_game().grain_stocks += self.get_current_game().harvest_units  * population_can_harvest
        else:
            self.get_current_game().grain_stocks += self.get_current_game().harvest_units * self.get_current_game().city_acres

    def change_harvest_unit(self):
        """
        Changes the number of units harvested per acre
        :return: the new number of units harvested per acre
        """
        self.get_current_game().harvest_units = random.randint(1, 6)

    def rat_infestation(self):
        """
        Check if there is a rat infestation. The probability of a rat infestation is 20%
        Update the number of rats units if so
        """
        if random.random() > 0.2:
            self.get_current_game().rats_units = self.get_current_game().grain_stocks * random.random()
            self.get_current_game().grain_stocks -= int(self.get_current_game().rats_units)
