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
    
def populate_db():
    faqs = [
        Faq(pergunta='O que é o Flask?', resposta='Flask é um micro-framework web escrito em Python. É chamado de "micro" porque não exige ferramentas ou bibliotecas específicas, mantendo um núcleo simples, mas extensível.'),
        Faq(pergunta='Qual a diferença entre Flask e Django?', resposta='O Django é "full-stack" (baterias inclusas), vindo com ORM e Admin prontos. O Flask é minimalista, permitindo que o desenvolvedor escolha suas próprias ferramentas (banco de dados, autenticação, etc).'),
        Faq(pergunta='O que é uma Rota (Route)?', resposta='Rotas são o mapeamento entre uma URL (ex: /contato) e uma função Python. Usa-se o decorador @app.route para definir o que acontece quando o usuário acessa aquele endereço.'),
        Faq(pergunta='O que é o Jinja2?', resposta='É o motor de templates padrão do Flask. Ele permite misturar lógica Python (loops, variáveis) dentro de arquivos HTML para gerar páginas dinâmicas.'),
        Faq(pergunta='Como exibo uma variável no HTML com Jinja2?', resposta='Utiliza-se chaves duplas. Por exemplo: {{ nome_do_usuario }} irá imprimir o valor da variável na tela.'),
        Faq(pergunta='Para que serve a função url_for()?', resposta='Ela gera URLs dinamicamente baseada no nome da função da rota. É preferível usar url_for("index") do que escrever "/" manualmente, facilitando mudanças futuras.'),
        Faq(pergunta='O que é a pasta "static"?', resposta='É o diretório onde o Flask procura por arquivos estáticos que não mudam, como folhas de estilo CSS, arquivos JavaScript e imagens.'),
        Faq(pergunta='O que é a pasta "templates"?', resposta='É onde ficam os arquivos HTML que contêm a estrutura da página e a lógica do Jinja2. O Flask busca arquivos aqui automaticamente ao usar render_template().'),
        Faq(pergunta='Como acessar dados enviados por um formulário (POST)?', resposta='Através do objeto "request". Usa-se request.form["nome_do_campo"] para pegar os dados enviados via método POST.'),
        Faq(pergunta='O que são Blueprints?', resposta='Blueprints permitem dividir a aplicação em componentes menores e reutilizáveis (módulos). Isso é essencial para organizar projetos grandes, separando Admin, API e Site Público, por exemplo.'),
        Faq(pergunta='O que é o Flask-SQLAlchemy?', resposta='É uma extensão que facilita o uso do SQLAlchemy (um ORM) dentro do Flask, permitindo manipular bancos de dados usando classes e objetos Python em vez de SQL puro.'),
        Faq(pergunta='O que é o padrão Application Factory?', resposta='É a prática de criar a aplicação dentro de uma função (def create_app). Isso permite criar múltiplas instâncias do app com configurações diferentes, facilitando testes automatizados.'),
        Faq(pergunta='O que é WSGI?', resposta='Web Server Gateway Interface. É o protocolo padrão que permite que servidores web (como Nginx ou Apache) conversem com aplicações Python (como o Flask). O Werkzeug é a biblioteca WSGI do Flask.'),
        Faq(pergunta='Para que serve o objeto "session"?', resposta='A session permite armazenar informações específicas de um usuário de uma requisição para outra. No Flask, isso é gravado em cookies assinados criptograficamente.'),
        Faq(pergunta='O que é o Flask-WTF?', resposta='É uma extensão que integra o WTForms ao Flask. Ela facilita a criação, validação e proteção de formulários HTML, incluindo proteção contra CSRF.'),
        Faq(pergunta='O que é CSRF e como o Flask protege contra isso?', resposta='CSRF (Cross-Site Request Forgery) é um ataque onde um site malicioso engana o navegador. O Flask-WTF previne isso exigindo um token secreto único em cada formulário enviado.'),
        Faq(pergunta='O que é o objeto "g"?', resposta='O "g" é um objeto global para armazenamento temporário. Ele serve para guardar dados durante uma única requisição (ex: usuário logado, conexão de banco) e é descartado ao final dela.'),
        Faq(pergunta='Qual a diferença entre servidor de desenvolvimento e produção?', resposta='O servidor embutido do Flask (`flask run`) é para testes e debug. Em produção, deve-se usar um servidor WSGI robusto como Gunicorn ou uWSGI para aguentar tráfego real.'),
        Faq(pergunta='Como lidar com erros 404 (Página não encontrada)?', resposta='Usa-se o decorador @app.errorhandler(404). Isso permite criar uma função que retorna uma página HTML personalizada sempre que o usuário acessar uma rota inexistente.'),
        Faq(pergunta='O que são "Contexts" no Flask?', resposta='Existem dois principais: o "Application Context" (configurações do app) e o "Request Context" (dados da requisição atual). O Flask gerencia isso magicamente para que `request` e `current_app` estejam sempre disponíveis.')
    ]
    
    db.session.add_all(faqs)
    db.session.commit()
    click.echo("Banco atualizado com 20 perguntas sobre Flask!")

def init_app(app):
    """Registra os comandos no Flask."""
    
    # flask create-db
    app.cli.add_command(app.cli.command()(create_db))
    
    # flask drop-db
    app.cli.add_command(app.cli.command()(drop_db))
    
    # populate-db
    app.cli.add_command(app.cli.command()(populate_db))

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