import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app import blueprint

# models
from app.main.model import user, blacklist

app = create_app(os.getenv('RESTFUL_ENV') or 'dev')
app.url_map.strict_slashes = False

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host="0.0.0.0", port=5000)


if __name__ == '__main__':
    manager.run()
