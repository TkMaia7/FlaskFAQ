# FlaskFAQ

Este projeto é uma aplicação web de Perguntas Frequentes (FAQ) desenvolvida em Python utilizando o framework Flask.

## Sobre o Projeto

Este sistema trata-se de uma refatoração e migração do projeto **[FAQ-Web](https://github.com/TkMaia7/FAQ-Web)**, originalmente escrito em PHP com tema de Futebol.

**Principais Mudanças:**
* **Tecnologia:** Migração de PHP para Python/Flask.
* **Arquitetura:** Implementação do padrão *Application Factory* e *Blueprints*.
* **Tema:** O conteúdo foi alterado de futebol para o própio framework Flask.
* **Funcionalidades:** Adição de ORM (SQLAlchemy), sistema de Login seguro e Painel Administrativo automático.

---

## Como Rodar o Projeto

Você pode executar o projeto usando o gerenciador de pacotes padrão (`pip/venv`) ou o (`uv`). Escolha uma das opções abaixo:

### Opção 1: Padrão (Venv + Pip)

1. Clonar o repositório.
2. Acessar o diretório do projeto:
```bash
cd FlaskFAQ
```
3. Criar o ambiente virtual Python:
```bash
python3 -m venv .venv
```
4. Ativar o ambiente virtual:
* Linux/Mac: `source .venv/bin/activate`
* Windows: `.\.venv\Scripts\activate`
5. Instalar as dependências:
```bash
pip install -r requirements.txt
```

### Opção 2: UV

Se você utiliza o **uv**, basta rodar:

```bash
uv sync
```
---

## Configuração do Banco de Dados

Com o ambiente virtual ativo, execute a sequência abaixo para configurar o sistema:

1. Criar o Banco de Dados e as Tabelas:
```bash
flask create-db
```
2. Criar um Usuário Administrador:
*Nota: Substitua os dados conforme desejar.*
```bash
flask add-user -u admin -p 123 -n "Administrador"
```
3. Popular o Banco com Perguntas (Seed):
```bash
flask populate-db
```

---

## Executando a Aplicação

1. Inicie o servidor:
```bash
flask run
```
2. Acesse no navegador: [http://127.0.0.1:5000/](https://www.google.com/search?q=http://127.0.0.1:5000/)

---

### Estrutura de Pastas

* `flask_faq/`: Código fonte da aplicação.
* `blueprints/`: Rotas do site público.
* `templates/`: Arquivos HTML (Jinja2).
* `models.py`: Modelos do Banco de Dados.
* `cli.py`: Comandos personalizados de terminal.
* `instance/`: Onde o banco de dados SQLite (`flask.db`) é salvo.
