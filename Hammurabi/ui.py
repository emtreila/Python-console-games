import random

from hammurabi.game import Game
from hammurabi.services import Service


class UI:
    def __init__(self, service: Service = Service):
        self._service = service

    def show_report(self, current_game: Game):
        if not current_game:
            return
        print(f"In year {current_game.year}, {current_game.people_starved} people starved.")
        print(f"{current_game.people_to_city} people came to the city.")
        print(f"City population is {current_game.city_population}")
        print(f"City owns {current_game.city_acres} acres of land.")
        print(f"Harvest was {current_game.harvest_units} units per acre.")
        print(f"Rats ate {current_game.rats_units} units.")
        print(f"Land price is {current_game.price_acre} units per acre.\n")
        print(f"Grain stocks are {current_game.grain_stocks} units.")

    def main(self):
        if not self._service.get_current_game():
            self._service.start_game()

        while self._service.get_current_game().year <= 5:
            self.show_report(self._service.get_current_game())
            self._service.update_year(self._service.get_current_game().year + 1)

            while True:
                acres = input("Acres to buy/sell (+/-) -> ")
                try:
                    acres = int(acres)
                except Exception as e:
                    print(f"Invalid input! Reason: {e}")
                    continue

                if acres < 0:
                    if abs(acres) > self._service.get_current_game().city_acres:
                        print("You cannot sell more acres than you have!")
                        continue
                elif acres > 0:
                    units_for_land = 20 * acres
                    if units_for_land > self._service.get_current_game().grain_stocks:
                        print("You cannot buy more land than you have grain for!")
                        continue
                break

            if acres < 0:
                self._service.sell_land(abs(acres))
            elif acres > 0:
                self._service.buy_land(acres)
            self._service.change_price()

            while True:
                feed_population = input("Units to feed the population -> ")
                try:
                    feed_population = int(feed_population)
                except:
                    print("Invalid input!")
                    continue
                if feed_population < 0:
                    print("Invalid input!")
                if feed_population > self._service.get_current_game().grain_stocks:
                    print("You cannot feed people with grain you do not have!")
                    continue
                break

            self._service.feed_population(feed_population)
            if not (self._service.check_population_starved(feed_population)):
                print("GAME OVER! Half of the population starved!")
                exit()
            self._service.new_people_to_city(feed_population)

            while True:
                acres_to_plant = input("Acres to plant -> ")
                print("\n")
                try:
                    acres_to_plant = int(acres_to_plant)
                except:
                    print("Invalid input!")
                    continue
                if acres_to_plant > self._service.get_current_game().city_acres:
                    print("You cannot plant more acres than you have!")
                    continue
                elif acres_to_plant > self._service.get_current_game().grain_stocks:
                    print("You cannot plant grain that you do not have!")
                    continue
                break

            self._service.harvest(acres_to_plant)
            self._service.change_harvest_unit()

            self._service.rat_infestation()

        if self._service.get_current_game().city_population > 100 and self._service.get_current_game().city_acres > 1000:
            print("GAME WON! CONGRATULATIONS!")
        else:
            print("GAME OVER!")
