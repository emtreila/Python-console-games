from stellar_journey.repository import Repo
from stellar_journey.services import Service
from stellar_journey.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()
