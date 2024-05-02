# Introdução
Bem-Vindo a Blog API !
Este é um projeto de uma API para um blog relacionado a livros desenvolvida em Django e DRF(Django REST Framework).

# Funcionalidades/Recursos Disponíveis

**Usuários:**
CRUD dos usuários.

**Posts:**
CRUD dos posts.
Curtida e descurtida de posts.
Listagem de posts por categorias.
Acesso a estatísticas sobre os posts.

**Comentários:**
CRUD dos comentários.

# Autenticação

Método de Autenticação : JWT Token

Para acessar os endpoints protegidos da API ,a autenticação por JWT é necessária.Siga as instruções da documentação.

# Documentação Completa da API

Para acessar a documentação completa da API feita através da ferramenta Postman basta acessar o link abaixo :

https://documenter.getpostman.com/view/32598004/2sA3JFBQ55

# Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

    Python
    Pip (gerenciador de pacotes do Python)

# Instalação das Dependências do Projeto

Para instalar todas as dependências necessárias para o funcionamento correto do projeto(especificadas no requirements.txt) utilize o comando:

pip install -r requirements.txt

# Configuração do Banco de Dados

Para configurar o banco de dados do projeto são necessários dois comandos na seguinte ordem:

1 - python manage.py makemigrations

2 - python manage.py migrate

# Rodando o Servidor Local

Para iniciar o servidor de desenvolvimento do Django em sua máquina utilize o seguinte comando:

python manage.py runserver
