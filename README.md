# Employee Manager

Api escrita usando **Python** e **Django**, criada gerenciar dados de funcionários.

### Iniciando a aplicação

Na pasta *employee-manager* instale os pacotes listados no arquivo *requirements.txt*:

- `pip install -r requirements.txt`

Feito isso, crie as tabelas e as popule usando o comando:

- `python manage.py migrate`

Crie um usuário no terminal para ter acesso ao painel administrativo do django:

- `python manage.py createsuperuser`

Para rodar a aplicação execute o comando:

- `python manage.py runserver`


## Funcionamento

### URL

**/admin/**

- Abre o painel administrativo, onde você pode criar funcionários e atualizar seus registros, apenas usuários que possuem login tem acesso ao painel.

**/api/employees/**

- Envia um `json` contendo todos os funcionários cadastrados e seus dados

