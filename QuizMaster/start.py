from quiz_master.repository import Repo
from quiz_master.service import Service
from quiz_master.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()
