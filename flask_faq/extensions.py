from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_simplelogin import SimpleLogin
from flask_wtf.csrf import CSRFProtect  
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
bootstrap = Bootstrap()
admin = Admin()
simple_login = SimpleLogin()
csrf = CSRFProtect()  