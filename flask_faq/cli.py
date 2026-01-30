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
    """Insere as perguntas iniciais no banco."""
    faqs = [
        Faq(pergunta='O que configura o impedimento?', resposta='Um jogador está em posição de impedimento se estiver mais próximo da linha de meta adversária do que a bola e o penúltimo adversário no momento em que a bola é tocada por um companheiro de equipe.'),
        Faq(pergunta='Quando o VAR pode ser acionado?', resposta='O Árbitro de Vídeo (VAR) só pode intervir em quatro situações de "erro claro e óbvio": validação de gols (se houve falta ou impedimento), marcação de pênaltis, cartões vermelhos diretos e confusão de identidade de jogadores.'),
        Faq(pergunta='É possível fazer um gol direto de arremesso lateral?', resposta='Não. Segundo a regra, não é válido um gol marcado diretamente de um arremesso lateral. Se a bola entrar no gol adversário sem tocar em ninguém, é marcado tiro de meta; se entrar no próprio gol, é escanteio.'),
        Faq(pergunta='Quantas substituições são permitidas em uma partida oficial?', resposta='Atualmente, a regra geral da FIFA permite até 5 substituições por equipe, que devem ser realizadas em no máximo três paradas durante o jogo (o intervalo não conta como parada).'),
        Faq(pergunta='Qual a diferença entre tiro livre direto e indireto?', resposta='No tiro livre direto, o gol pode ser validado se a bola entrar direto na meta. No tiro livre indireto (geralmente marcado por jogo perigoso ou recuo para o goleiro), a bola precisa tocar em outro jogador antes de entrar no gol.'),
        Faq(pergunta='O goleiro pode pegar a bola com a mão se receber um recuo?', resposta='Não se o recuo for feito intencionalmente com os pés por um companheiro de equipe. Se o recuo for de cabeça, peito ou coxa, o goleiro pode usar as mãos. Se usar as mãos num recuo com o pé, é marcado tiro livre indireto.'),
        Faq(pergunta='Qual a duração regulamentar de uma partida?', resposta='Uma partida oficial consiste em dois tempos de 45 minutos cada, totalizando 90 minutos, mais os acréscimos determinados pelo árbitro para compensar o tempo perdido.'),
        Faq(pergunta='O que acontece se um jogador receber dois cartões amarelos?', resposta='Se um jogador receber o segundo cartão amarelo na mesma partida, ele receberá automaticamente um cartão vermelho e será expulso do campo, não podendo ser substituído.'),
        Faq(pergunta='Qual a distância oficial da marca do pênalti?', resposta='A marca da penalidade máxima fica localizada a exatos 11 metros (ou 12 jardas) do centro da linha do gol, equidistante das traves.'),
        Faq(pergunta='Qual o número mínimo de jogadores para uma partida acontecer?', resposta='Uma partida não pode começar ou continuar se qualquer uma das equipes tiver menos de 7 jogadores em campo (incluindo o goleiro).')
    ]
    
    db.session.add_all(faqs)
    db.session.commit()
    click.echo("Banco de dados populado com sucesso!")

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