[![N|Solid](http://www.ifs.edu.br/comunicacao/images/Imagens/Marcas/IFS_puro/IFS---horizontal-01.png)](http://www.ifs.edu.br/)
# Vulnerabilidades

## Sobre
Desenvolvido em Django, o Hotsite exibite das vulnerabilidades, assim como suas informações, para a rede do Instituto Federal de Sergipe, auxiliando na comunicação e correções das inseguranças.

## Dependências
### Projeto
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [Git](https://github.com/) | 2.14.1 | Controle de versão
| [Python](https://www.python.org/) | 3.6+ | Linguagem
| [Mysql](https://www.mysql.com/) | 5.7.19 | Banco de dados
| [Node.js](https://nodejs.org/) | v6+ | Gerenciamento das depências do Frontend
| [Virtualenv](https://virtualenv.pypa.io/) | 15.1.0 | Gerenciamento das dependências do Python
| [Supervisor](http://supervisord.org/) | 3.3.3 | Controle dos processos
| [Nginx](https://nginx.org/en/) | 1.12.1 | Servidor Web

### Backend
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [Django](https://www.djangoproject.com/) | 1.11.4 | Framework
| [Mysqlclient](https://pypi.python.org/pypi/mysqlclient/1.3.10) | 1.3.10 | Plugin de conexão com o banco de dados
| [Gunicorn](http://gunicorn.org/) |  | Gateway de comunicação entre o servidor e a aplicação disponibilizada no servidor Web

### Frontend 
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [bootstrap](getbootstrap.com/) | 4.0.0-alpha.6 | Biblioteca do frontend
| [datatables.net](https://datatables.net) | 1.10.15 | Customização das tabelas e seus dados 
| [datatables.net-bs](https://datatables.net) | 1.10.15 | Link do datatables com o bootstrap
| [font-awesome](http://fontawesome.io/) | 4.7.0 | Icones em fontes
| [jquery](https://jquery.com/) | 3.2.1 | Biblioteca JavaScript
| [pace-js](github.hubspot.com/pace/docs/welcome/) | 1.0.2 | Progeresso do carregamento
| [select2](https://select2.github.io/) | 4.0.3 | Customização do selectbox com suporte a busca
| [tether](tether.io/) | 1.4.0 | Posicionamento dos elementos na tela
| [toastr](https://github.com/CodeSeven/toastr) | 2.1.2 | Notificações

## Preparação
Clone o repositório

```
$ git clone https://unanimad@bitbucket.org/unanimad/ifs-vulnerabilidades.git
```
Acesse o diretório do repositório e altere para a branch **master**
```
$ git pull origin dev
```

Crie um ambiente python virtual utilizando o **python3** como versão
```
$ virtualenv -p python3 venv
```

Ative o ambiente virtual
```
$ source venv/bin/activate
```

Instale as dependências da aplicação
```
$ pip install -r req.txt
```

Instale as dependências do frontend, não esqueça de ir até o diretório do arquivo `package.json` para executar seguinte comando
```
$ npm install
```

Colete os arquivos estáticos para o diretório relacionado
```
$ python manage.py collectstatic
```

Configure o banco de dados no arquivo `settings.py`, localizando a variável `DATABASES`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}
```

Faça as migrações
```
$ python manage.py migrate 
```

Execute a aplicação para testar com o seguinte comando
```
$ python manage.py runserver
```