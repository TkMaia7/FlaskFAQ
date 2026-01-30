from flask import Flask
from dynaconf import FlaskDynaconf
from flask_faq import extensions, cli  

def create_app(**config):
    app = Flask(__name__)

    FlaskDynaconf(app, settings_files=['settings.toml'])

    extensions.db.init_app(app)
    extensions.bootstrap.init_app(app)
    
    
    cli.init_app(app) 

    return app