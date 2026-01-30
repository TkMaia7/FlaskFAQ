from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash
from flask_faq.extensions import db, simple_login
from flask_faq.models import User

def verify_login(user):
    """Valida usuário e senha para o SimpleLogin."""
    
    username = user.get("username")
    password = user.get("password")
    
    # Debug dos dados recebidos
    print(f"Tentativa para usuário: {username}")
    
    stmt = db.select(User).where(User.username == username)
    existing_user = db.session.execute(stmt).scalar_one_or_none()
    
    if not existing_user:
        print("ERRO: Usuário não encontrado no banco.")
        return False
    
    if check_password_hash(existing_user.password, password):
        print("SUCESSO: Senha correta!")
        return True
    
    print("ERRO: Senha incorreta.")
    return False

def init_app(app):
    """Inicializa o sistema de login."""
    simple_login.init_app(app, login_checker=verify_login)