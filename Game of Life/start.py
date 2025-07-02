from game_of_life.repository import Repo
from game_of_life.service import Service
from game_of_life.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()
