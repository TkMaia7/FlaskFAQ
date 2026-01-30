from flask_admin.contrib.sqla import ModelView
from flask_simplelogin import login_required
from flask_faq.extensions import admin, db
from flask_faq.models import User, Faq

class ProtectedView(ModelView):
    def is_accessible(self):
        from flask_simplelogin import is_logged_in
        return is_logged_in()

def init_app(app):
    """Inicializa o Painel Admin."""
    admin.init_app(app)
    
    admin.name = app.config.get("FLASK_ADMIN_NAME", "Admin")
    admin.template_mode = app.config.get("FLASK_ADMIN_TEMPLATE_MODE", "bootstrap3")
    
    admin.add_view(ProtectedView(User, db.session))
    admin.add_view(ProtectedView(Faq, db.session))