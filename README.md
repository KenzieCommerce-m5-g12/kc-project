# kc-project

## O que é?

kc_project API (Kenzie Commerce Project) é uma API que genrencia dados de compra e venda de produtos variados por seus respectivos usuários (clientes e/ou vendedores), podendo anunciar produtos à venda e também comprar de outros usuários.

## O que ela faz?

O kc_project é capaz de:

- Criação de usuário (login e senha);
- Suporta três tipos de usuário (Administrador, Vendedor e Cliente);
- Clientes podem visualizar a lista de items publicadas por todos os vendedores e também realizarem compras, porém não podem vender produtos, a menos que atualizem seu tipo de usuário para vendedor.
- Vendedores cumulam todas as permissões de usuários clientes, porém podem também vender items, visualizar todas as vendas recebidas em cada produtos, alterar status da venda de pedidos recebidos.
- Administradores possuem privilégios para editar, deletar e gerir toda plataforma, produtos e usuários;
- Possui proteção em rotas específicas.
- Os usuários (vendedores e clientes) podem criar a sua própria lista de desejos.

## Como rodar a aplicação?

1. Crie um ambiente virtual com o comando: 
```python
python -m venv venv
```

<br>

2. Ative o venv com o comando:

```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate


```

<br>

3. Instale a lista de dependências do projeto:

```python
pip install -r requirements.txt
```

<br>

4. É necessário configurar na máquina local o banco de dados em Postgres de acordo com o arquivo **".env.example"**;

<br>

5. Após, rodar os comandos:

```python
python manage.py makemigrations
```

e

```python
python manage.py migrate
```

para realizar as migrações e relações necessárias.
