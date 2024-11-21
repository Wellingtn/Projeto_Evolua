Evolua
Evolua é uma plataforma que permite que alunos respondam quizzes para identificar suas vocações, enquanto professores podem analisar os resultados dos quizzes da turma, identificando as preferências e alinhamentos dos alunos.

Tecnologias Utilizadas
Backend: Python com Django e Jinja
Frontend: HTML e CSS
Banco de Dados: PostgreSQL

Pré-requisitos
Antes de começar, você precisará ter:

Python
Django
Visual Studio Code
Ambiente virtual para rodar o Django
Passo a Passo de Instalação

Clone o Repositório
git clone git@github.com:Wellingtn/Projeto_Evolua.git
cd evolua

Crie o Ambiente Virtual
python3 -m venv venv
Ative o Ambiente Virtual

No Linux/macOS:
source venv/bin/activate

No Windows:
.\venv\Scripts\activate
Instale o Django e Outras Dependências

<<<<<<< HEAD
pip install -r requirements.txt
=======
    pip install -r requirements.txt
Configure o Banco de Dados Configure as credenciais de acesso ao PostgreSQL.
>>>>>>> 83a33aef78d33bd3a7f659863c3ac4069a54451b

Configure o Banco de Dados Configure as credenciais de acesso ao PostgreSQL.
Execute as Migrações
python manage.py migrate

Inicie o Servidor
python manage.py runserver

