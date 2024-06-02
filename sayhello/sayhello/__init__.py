from flask import Flask

# Bootstrap-Flask is a collection of Jinja macros for Bootstrap and Flask.
# It helps you to render Flask-related data and objects to Bootstrap markup HTML more easily.
from flask_bootstrap import Bootstrap4

# This extension enhances Jinja2 templates with formatting of dates and times using moment.js.
from flask_moment import Moment

from flask_sqlalchemy import SQLAlchemy

from sayhello.blueprints import about_bp

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.register_blueprint(about_bp)

db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)
moment = Moment(app)

from sayhello import views, errors, commands
