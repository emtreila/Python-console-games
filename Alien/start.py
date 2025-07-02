from alien.repository import Repo
from alien.services import Service
from alien.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()
