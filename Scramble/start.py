from scramble.repository import TextMemoRepo
from scramble.service import Service
from scramble.ui import UI

repository = TextMemoRepo()
service = Service(repository)
ui = UI(service)

ui.main()
