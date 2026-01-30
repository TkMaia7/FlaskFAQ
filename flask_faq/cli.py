import click
from flask_faq.extensions import db
from flask_faq.models import create_user, Faq

def create_db():
    """Cria o banco de dados e as tabelas."""
    db.create_all()
    click.echo("Banco de dados criado com sucesso!")

def drop_db():
    """Limpa o banco de dados."""
    db.drop_all()
    click.echo("Banco de dados apagado.")

def init_app(app):
    """Registra os comandos no Flask."""
    
    # flask create-db
    app.cli.add_command(app.cli.command()(create_db))
    
    # flask drop-db
    app.cli.add_command(app.cli.command()(drop_db))

    # flask add-user
    @app.cli.command()
    @click.option("--username", "-u", required=True)
    @click.option("--password", "-p", required=True)
    @click.option("--name", "-n", required=True)
    def add_user(username, password, name):
        """Adiciona um novo usuário administrador."""
        try:
            create_user(username, password, name)
            click.echo(f"Usuário {username} criado!")
        except RuntimeError as e:
            click.echo(e)