from hangman.repository import TextMemoRepo
from hangman.service import Service
from hangman.ui import UI

repository = TextMemoRepo()
service = Service(repository)
ui = UI(service)

ui.main()
