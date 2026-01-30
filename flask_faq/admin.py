from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_simplelogin import login_required
from flask_faq.extensions import admin, db
from flask_faq.models import User, Faq
from flask_admin import AdminIndexView 

class ProtectedIndexView(AdminIndexView):
    def is_accessible(self):
        from flask_simplelogin import is_logged_in
        return is_logged_in()
    
    def inaccessible_callback(self, name, **kwargs):
        from flask import redirect, url_for
        return redirect(url_for('simplelogin.login', next='/admin'))

class ProtectedView(ModelView):
    def is_accessible(self):
        from flask_simplelogin import is_logged_in
        return is_logged_in()

def init_app(app):
    """Inicializa o Painel Admin."""
    
    admin.init_app(app, index_view=ProtectedIndexView())
    
    admin.name = "FAQ Futebol"
    admin.template_mode = "bootstrap3"
    admin.base_template = 'admin/custom_master.html'
    
    admin.add_view(ProtectedView(User, db.session))
    admin.add_view(ProtectedView(Faq, db.session))
    admin.add_link(MenuLink(name='Voltar ao Site', url='/'))