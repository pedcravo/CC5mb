# Resumo dos Caps 1-5
Este é um resumo mais geral sobre os Caps 1-5

## **Parte 01: Introdução a Frameworks Web**

Este documento apresenta os fundamentos de servidores web e o framework Flask, uma ferramenta poderosa para criar aplicações web em Python.

### **1. Servidor HTTP Simples em Python**
- **O que é?**  
  Um servidor web básico implementado com o módulo `http.server` do Python. Ele é capaz de responder a requisições HTTP GET e servir arquivos estáticos, como páginas HTML, diretamente de um diretório local.

- **Como funciona?**  
  Utiliza duas classes principais:
  - **`HTTPServer`**: Escuta conexões em uma porta específica (ex.: 8000).
  - **`SimpleHTTPRequestHandler`**: Processa requisições GET, mapeando URLs para arquivos no sistema de arquivos.

- **Exemplo prático**  
  Aqui está um código simples para criar um servidor:
  ```python
  from http.server import HTTPServer, SimpleHTTPRequestHandler

  PORT = 8000
  httpd = HTTPServer(("", PORT), SimpleHTTPRequestHandler)
  print(f"Servidor rodando na porta {PORT}")
  httpd.serve_forever()
  ```
  - Execute esse código em um diretório com um arquivo `index.html`. Acesse `http://localhost:8000/` no navegador para ver o conteúdo do arquivo servido.

- **Detalhes técnicos**  
  - O servidor associa automaticamente URLs a arquivos. Por exemplo, `/index.html` entrega o arquivo `index.html`.
  - Ele responde com códigos HTTP padrão (ex.: 200 OK para sucesso, 404 Not Found para arquivos inexistentes).

- **Limitações**  
  - Suporta apenas requisições GET, sem suporte nativo a POST, PUT ou DELETE.
  - Não oferece segurança (sem HTTPS ou autenticação).
  - Ideal para testes locais, mas inadequado para produção.

- **Aplicação prática**  
  Experimente criar um arquivo `index.html` com um texto simples, como `<h1>Meu primeiro servidor!</h1>`, e use o servidor para visualizá-lo. Isso ajuda a entender como requisições web funcionam na prática.

---

### **2. Flask - Olá Mundo!**
- **O que é Flask?**  
  Flask é um micro-framework Python para desenvolvimento web. Ele é leve, flexível e permite criar aplicações web rapidamente, desde projetos simples até sistemas mais complexos.

- **Instalação e configuração inicial**  
  1. Crie um ambiente virtual:
     ```bash
     python3 -m venv venv
     ```
  2. Ative o ambiente:
     - Linux/Mac: `source venv/bin/activate`
     - Windows: `venv\Scripts\activate`
  3. Instale o Flask:
     ```bash
     pip install flask
     ```

- **Estrutura básica de um projeto Flask**  
  ```
  bloguvv/
  ├── venv/              # Ambiente virtual
  ├── app/              # Diretório principal da aplicação
  │   ├── __init__.py   # Inicializa o Flask
  │   └── routes.py     # Define as rotas
  └── bloguvv.py        # Arquivo de entrada
  ```

- **Exemplo de código**  
  - **`app/__init__.py`**: Configura o aplicativo Flask.
    ```python
    from flask import Flask
    app = Flask(__name__)
    from app import routes
    ```
  - **`app/routes.py`**: Define as rotas e respostas.
    ```python
    from app import app

    @app.route('/')
    @app.route('/index')
    def index():
        return "Olá Mundo!"
    ```
  - **`bloguvv.py`**: Ponto de entrada.
    ```python
    from app import app
    ```

- **Como executar?**  
  1. Defina a variável de ambiente:
     - Linux/Mac: `export FLASK_APP=bloguvv.py`
     - Windows: `set FLASK_APP=bloguvv.py`
  2. Inicie o servidor:
     ```bash
     flask run
     ```
  3. Acesse `http://localhost:5000/` no navegador e veja "Olá Mundo!".

- **Conceitos fundamentais**  
  - **Rotas**: Associam URLs a funções Python usando o decorador `@app.route()`.
  - **Funções de visualização**: São funções que retornam respostas HTTP (ex.: texto, HTML).
  - **Ambientes virtuais**: Isolam as dependências do projeto, evitando conflitos com outros projetos.

- **Aprofundando**  
  - Tente criar rotas adicionais, como `/sobre` ou `/contato`, retornando mensagens diferentes.
  - Explore os parâmetros de `@app.route()`, como `methods=['GET', 'POST']`, para entender como lidar com diferentes tipos de requisições.

---

## **Parte 02: Templates**

Aqui, o foco é usar templates para separar a lógica da aplicação da apresentação visual, utilizando o Jinja2, o motor de templates integrado ao Flask.

### **1. Modo DEBUG**
- **O que é?**  
  Um modo de desenvolvimento que facilita a depuração:
  - Recarrega o servidor automaticamente ao salvar alterações no código.
  - Exibe um depurador interativo no navegador em caso de erros.

- **Como habilitar?**  
  - Linux/Mac: `export FLASK_DEBUG=1`
  - Windows: `set FLASK_DEBUG=1`
  - Em seguida, execute `flask run`.

- **Cuidados**  
  - Nunca use em produção! O modo DEBUG expõe vulnerabilidades, como a execução remota de código.

- **Prática**  
  Ative o modo DEBUG, altere uma rota e veja o servidor recarregar automaticamente.

---

### **2. Templates com Jinja2**
- **O que são?**  
  Arquivos HTML com marcadores dinâmicos que permitem inserir dados gerados pelo Python. O Flask usa o Jinja2 para renderizar esses templates.

- **Onde ficam?**  
  Os templates devem estar no diretório `app/templates/`.

- **Exemplo básico**  
  - **`app/templates/index.html`**:
    ```html
    <h1>Olá, {{ user.username }}!</h1>
    ```
  - **`app/routes.py`**:
    ```python
    from flask import render_template

    @app.route('/')
    def index():
        user = {'username': 'Wanderson'}
        return render_template('index.html', user=user)
    ```

- **Recursos do Jinja2**  
  - **Variáveis**: Use `{{ variavel }}` para exibir valores.
  - **Condicionais**:
    ```html
    {% if title %}
      <title>{{ title }} - Blog UVV</title>
    {% else %}
      <title>Bem vindo ao Blog UVV!</title>
    {% endif %}
    ```
  - **Loops**:
    ```html
    {% for post in posts %}
      <p>{{ post.author }} disse: <b>{{ post.body }}</b></p>
    {% endfor %}
    ```
  - **Herança de templates**:  
    - Crie um template base (`base.html`):
      ```html
      <html>
        <head>
          <title>{% block title %}{% endblock %} - Blog UVV</title>
        </head>
        <body>
          <div>Blog UVV: <a href="/index">Home</a></div>
          <hr>
          {% block content %}{% endblock %}
        </body>
      </html>
      ```
    - Estenda-o em outro template:
      ```html
      {% extends "base.html" %}
      {% block content %}
        <h1>Olá, {{ user.username }}!</h1>
      {% endblock %}
      ```

- **Aprofundando**  
  - Crie um `base.html` com uma barra de navegação e estenda-o em várias páginas.
  - Passe uma lista de posts para um template e use um loop para exibi-los.

---

## **Parte 03: Formulários Web**

Este documento explora como capturar e processar dados enviados por usuários através de formulários.

### **1. Flask-WTF**
- **O que é?**  
  Uma extensão do Flask que simplifica a criação e validação de formulários, protegendo contra ataques como CSRF (Cross-Site Request Forgery).

- **Instalação**  
  ```bash
  pip install flask-wtf
  ```

- **Configuração**  
  Adicione uma chave secreta para segurança:
  - **`config.py`**:
    ```python
    class Config:
        SECRET_KEY = 'uma-chave-secreta-aqui'
    ```
  - Atualize `app/__init__.py`:
    ```python
    app.config.from_object(Config)
    ```

- **Exemplo de formulário**  
  - **`app/forms.py`**:
    ```python
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, SubmitField
    from wtforms.validators import DataRequired

    class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Sign In')
    ```

---

### **2. Hashing**
- **O que é?**  
  Hashing transforma dados (como senhas) em uma sequência fixa de caracteres, dificultando sua reversão. É essencial para segurança.

- **Exemplo com `hashlib`**  
  ```python
  import hashlib
  senha = "minhasenha"
  hash_object = hashlib.sha256(senha.encode())
  print(hash_object.hexdigest())  # Exibe o hash em hexadecimal
  ```

- **Salting**  
  Adiciona um valor aleatório (salt) para aumentar a segurança:
  ```python
  import secrets
  salt = secrets.token_hex(16)  # Gera um salt único
  hash_object = hashlib.sha256((senha + salt).encode())
  print(hash_object.hexdigest())
  ```

---

### **3. Formulários de Login**
- **Renderização**  
  - **`app/templates/login.html`**:
    ```html
    <form method="post">
      {{ form.hidden_tag() }}
      <p>{{ form.username.label }} {{ form.username() }}</p>
      <p>{{ form.password.label }} {{ form.password() }}</p>
      <p>{{ form.submit() }}</p>
    </form>
    ```
- **Processamento**  
  - **`app/routes.py`**:
    ```python
    from flask import render_template, flash, redirect, url_for
    from app.forms import LoginForm

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash(f'Login solicitado por {form.username.data}')
            return redirect(url_for('index'))
        return render_template('login.html', form=form)
    ```

- **Aprofundando**  
  - Adicione validação personalizada (ex.: tamanho mínimo da senha).
  - Use mensagens flash para feedback visual ao usuário.

---

## **Parte 04: Flask e Banco de Dados**

Aqui, aprendemos a integrar bancos de dados com o Flask usando Flask-SQLAlchemy e Flask-Migrate.

### **1. Flask-SQLAlchemy e Flask-Migrate**
- **Instalação**  
  ```bash
  pip install flask-sqlalchemy flask-migrate
  ```

- **Configuração**  
  - **`config.py`**:
    ```python
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```
  - **`app/__init__.py`**:
    ```python
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    ```

---

### **2. Modelos de Banco de Dados**
- **Exemplo**  
  - **`app/models.py`**:
    ```python
    from app import db

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), unique=True, nullable=False)
    ```

- **Migrações**  
  1. Inicialize: `flask db init`
  2. Crie uma migração: `flask db migrate -m "criando tabela user"`
  3. Aplique: `flask db upgrade`

---

### **3. Relacionamentos**
- **Exemplo com relação**  
  - **`app/models.py`**:
    ```python
    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        body = db.Column(db.String(140))
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ```

- **Aprofundando**  
  - Use o comando `flask shell` para inserir e consultar dados:
    ```python
    u = User(username='Wanderson')
    db.session.add(u)
    db.session.commit()
    ```

---

## **Parte 05: Logins de Usuário**

Este documento foca na autenticação de usuários com Flask-Login e hashing de senhas.

### **1. Password Hashing**
- **Uso do Werkzeug**  
  - Gere um hash:
    ```python
    from werkzeug.security import generate_password_hash
    hash_senha = generate_password_hash('minhasenha')
    ```
  - Verifique:
    ```python
    from werkzeug.security import check_password_hash
    check_password_hash(hash_senha, 'minhasenha')  # Retorna True
    ```

---

### **2. Flask-Login**
- **Instalação**  
  ```bash
  pip install flask-login
  ```

- **Configuração**  
  - **`app/__init__.py`**:
    ```python
    from flask_login import LoginManager
    login = LoginManager(app)
    login.login_view = 'login'
    ```

- **Exemplo de uso**  
  - Proteja uma rota:
    ```python
    from flask_login import login_required

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return "Bem-vindo ao dashboard!"
    ```

- **Aprofundando**  
  - Implemente login e logout completos, integrando com o banco de dados.
