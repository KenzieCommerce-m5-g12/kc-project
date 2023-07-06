# kc-project

## O que é?
kc_project API (Kenzie Commerce Project) é uma API que genrencia dados de compra e venda de produtos variados por seus respectivos usuários (clientes e/ou vendedores), podendo anunciar produtos à venda e  também comprar de outros usuários.

## O que ela faz?
O kc_project é capaz de:
- Criação de usuário (login e senha);
- Suporta três tipos de usuário (Administrador, Vendedor e Cliente);
- Cliente e vendedor podem publicar produtos para venda e também comprarem produtos para si;
- Administradores possuem privilégios para editar e deletar items de usuários comuns e gerir toda plataforma;
- Clientes e Vendedores podem listar todas as compras feitas, ver os produtos que colocaram à venda, bem como todos os pedidos realizados por outros usuários nos seus próprios produtos anunciados;
- Possui proteção em rotas específicas.
- Os usuários podem criar lista de desejo;

##  Como rodar a aplicação?
1) Crie um ambiente virtual com o comando: `python -m venv venv`;

<br>

2) Ative o venv com o comando: 
```
source venv/bin/activate
```

<br>

3) Instale a lista de dependências do projeto:
```
pip install -r requirements.txt
```

<br>

4) É necessário configurar na máquina local o banco de dados em Postgres de acordo com o arquivo "**.env.example**";

<br>

5) Após, rodar os comandos
```
python manage.py makemigrations
``` 
e 
```
python manage.py migrate
```
para realizar as migrações e relações necessárias.

