from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from application import app, db_session
app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db_session)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()