from app.app_controller import AppController
from app.app_factory import AppFactory

app_factory = AppFactory()
app = app_factory.get_instance()
app_metadata = app_factory.get_metadata()

AppController(app, app_metadata)
