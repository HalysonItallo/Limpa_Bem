# Projeto Limpa-Bem ♲ 

Este projeto é um desafio de estágio da empresa Venda Mais, backend [Django](https://www.djangoproject.com/).


## Models
  > Service 
  > - id
  > - name
  > - value
  > - isAvailable

> Customer Service
>  - Service
>  - attendant_id
>  - responsible_helper
>  - amount (up to 10% off)
>  - type_payment
>  - created_at
>  - will_carried_at
>  - status (pendente, realizado ou cancelado)
>  - Client

> Client
> - name
> - cellphone
> - adress

> Status
> - name

> Attendant
> name

lembrar de avisa sobre o ambiente virtual do py

python manage.py loaddata seeds/*.json


# Permissões dos usuários dentro de usuários

# admin django:
# pode criar um gerente

# autenticado:
# um admin pode criar um atendente
# um atendente pode listar os usuários tipo cliente
# um helper pode listar os usuários tipo cliente
# um cliente pode listar apenas ele mesmo

# não autenticado:
# pode criar um client
