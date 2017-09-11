# Vulnerabilidades

[![N|Solid](http://www.ifs.edu.br/comunicacao/images/Imagens/Marcas/IFS_puro/IFS---horizontal-01.png)](http://www.ifs.edu.br/)

# Sobre
Desenvolvido em Django, o Hotsite exibite das vulnerabilidades, assim como suas informações, para a rede do Instituto Federal de Sergipe, auxiliando na comunicação e correções das inseguranças.

# Dependências
### Projeto
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [Git](https://github.com/) | 2.14.1 | 
| [Python](https://www.python.org/) | 3.6+ | 
| [Mysql](https://www.mysql.com/) |  | 
| [Node.js](https://nodejs.org/) | v6+ | Gerenciamento das depências do Front-end
| [Virtualenv](https://virtualenv.pypa.io/) |  | Gerenciamento das dependências do Python
| [Supervisor](http://supervisord.org/) |  | Controle dos processos
| [Nginx](https://nginx.org/en/) |  | Servidor HTTP

### Backend
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [Django](https://www.djangoproject.com/) | 1.11.4 | 
| [Mysqlclient](https://pypi.python.org/pypi/mysqlclient/1.3.10) | 1.3.10 | 
| [Gunicorn](http://gunicorn.org/) |  | 

### Frontend 
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [bootstrap]() | 4.0.0-alpha.6 | 
| [datatables.net]() | 1.10.15 | 
| [datatables.net-bs]() | 1.10.15 | 
| [font-awesome]() | 4.7.0 | 
| [jquery]() | 3.2.1 | 
| [pace-js]() | 1.0.2 | 
| [select2]() | 4.0.3 | 
| [tether]() | 1.4.0 | 
| [toastr]() | 2.1.2 | 

# Instalação
Clone o seguinte repositório

```
$ git clone https://unanimad@bitbucket.org/unanimad/ifs-vulnerabilidades.git
```
Acesse o diretório do repositório e altere para a branch **dev**
```
$ git pull origin dev
```

Crie um virtualenv utilizando o **python3**
```
$ virtualenv -p python3 venv
```

Ative o ambiente virtual
```
$ source venv/bin/activate
```
Instale as depências da aplicação
```
$ pip install -r req.txt
```
