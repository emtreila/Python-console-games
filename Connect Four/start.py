from repository.repository import MemoRepo
from service.service import Service
from ui.ui import UI

repository = MemoRepo()
service = Service(repository)
ui = UI(service)

ui.main()

