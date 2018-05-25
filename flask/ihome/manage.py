from flask import render_template

from APP.App import create_app
from flask_script import Manager

from APP.config import Config

app = create_app(Config)

manager = Manager(app=app)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
