from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
import os


app = create_app(os.getenv('BLOG_CONFIG', 'default'))
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
