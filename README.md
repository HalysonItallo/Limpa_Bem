# Projeto Limpa-Bem ♲ 

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Modelos](#modelos)

:small_blue_diamond: [Permissões](#permissões)

:small_blue_diamond: [Como rodar o projeto](#como-rodar-o-projeto)

:small_blue_diamond: [Informações adicionais](#informações-do-banco)

## Descrição do projeto
Este projeto é um desafio de estágio da empresa Venda Mais, backend [Django](https://www.djangoproject.com/) e frontend [React](https://pt-br.reactjs.org/).


## Modelos
> Service 
> - id
> - name
> - value
> - isAvailable

> User
> - username
> - first_name
> - password
> - cellphone
> - adress
> - groups

> Status
> - id
> - name

> Customer Service
>  - service: service
>  - attendant: user
>  - helper: user
>  - amount
>  - type_payment
>  - created_at
>  - will_carried_at
>  - status: user 
>  - client: user

## Permissões 

### Permissões dos usuários dentro de usuários

> admin do django:
> - pode criar um gerente

> autenticado:
> - um admin pode criar um atendente
> - um atendente pode listar os usuários tipo cliente
> - um helper pode listar os usuários tipo cliente
> - um cliente pode listar apenas ele mesmo

> não autenticado:
> - pode criar um client
 
### Permissões dos usuários com o serviço
> gerente
> - Ele pode alterar, criar, editar e deletar

> todos os outros
> - Eles podem apenas ler 

### Permissões dos usuários com o status
> gerente
> - Ele pode alterar, criar, editar e deletar

> todos os outros
> - Eles podem apenas ler 

### Permissões dos usuários com os atendimentos
> gerente
> - Ele pode apenas ler 

> atendente
> - Ele pode apenas editar, ler

> cliente 
>  - Ele pode apenas ler os atendimentos dele e pode criar um atendimento("agendamento")

> helper
> - Ele pode apenas ler


## Como rodar o projeto?

No projeto foi utilizado o [Python 3.10.9](https://www.python.org/downloads/)

Com o Python já instalado 

Precisamos ativar o ambiente virtual do python usando esse comando:

```sh
python -m venv venv
```

Depois precisamos adicionar as dependências

No Windows, execute:

```sh
python -m venv env
venv\Scripts\activate.bat
pip install -r requirements.txt
```

No Linux ou no MacOS, execute:
```sh
python -m venv env
source venv/bin/activate
pip install -r requirements.txt
```

Precisamos rodar as migrações e criar o banco:

```sh
python manage.py makemigrations                                 
python manage.py migrate
python manage.py migrate --run-syncdb 
```

Precisamos popular o banco de dados com informações importantes para o teste, então vamos usar esse comando:

```sh
python manage.py loaddata seeds/*.json
```

Depois podemos rodar o projeto
```sh
python manage.py runserver
```

## Informações do banco:
### admin do django:
> - username: admin
> - password: 1234

### usuários para teste:
> - username: cliente
> password: gQp2DW7G38*5

> - username: gerente
> - password: gQp2DW7G38*5

> - username: atendente
> - password: gQp2DW7G38*5

> - username: helper
> - password: gQp2DW7G38*5


### Link do Front-end:
- https://github.com/HalysonItallo/Limpa_Bem_Front


### Obrigado por chegar até aqui 😄

<img src="https://camo.githubusercontent.com/4f373cf8f1fdb8657ba7147239c7a5c4a29573c0f2bb0620d0508286a303a24d/68747470733a2f2f692e696d6775722e636f6d2f55304d354e4e6f2e706e67" height="50px">