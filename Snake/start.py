from snake.repository import Repo
from snake.services import Service
from snake.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()
