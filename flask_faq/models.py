from flask_faq.extensions import db
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash 

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    name: Mapped[str]

class Faq(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    pergunta: Mapped[str] = mapped_column(String(255))
    resposta: Mapped[str] = mapped_column(Text) 

def create_user(username, password, name):
    stmt = db.select(User).where(User.username == username)
    existing_user = db.session.execute(stmt).scalar_one_or_none()
    
    if existing_user:
        raise RuntimeError(f"{username} já está cadastrado!")

    u = User(username=username, password=generate_password_hash(password), name=name)
    db.session.add(u)
    db.session.commit()