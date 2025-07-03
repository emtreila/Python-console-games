from hammurabi.repository import Repo
from hammurabi.services import Service
from hammurabi.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()
