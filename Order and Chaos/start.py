from order_and_chaos_var2.repository import Repo
from order_and_chaos_var2.services import Service
from order_and_chaos_var2.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()