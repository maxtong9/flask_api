# Runs the application

from api import app

application = app.create_app()

if __name__ == '__main__':
    application.run(host='localhost')