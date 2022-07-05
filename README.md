# CLT vs PJ

## Introdução
...
## Refêrencias

Este projeto foi desenvolvido usando as seguintes tecnologias:
- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [React](https://pt-br.reactjs.org/)

## Configurando o projeto:

Clone o repositorio para o seu ambiente local
```bash
git clone https://github.com/gogixweb/clt-vs-pj.git
```
</p>

### Rodando o projeto

O projeto é um [monorepo](https://pt.stackoverflow.com/questions/452607/o-que-%C3%A9-um-monorepo-quais-s%C3%A3o-as-suas-vantagens-e-desvantagens), então é possivel encontrar a api no pasta backend e o desenvolvimento do front na pasta frontend

### Frontend local
Para acessar o frontend da aplicação através do django é necessario rodar o comando de build dentro da pasta "frontend"
```bash
cd frontend && npm run build
```
ou 
```bash
make build
```
### Migrations
Você precisa rodar o comando de migração para criar as tabelas necessarias no banco de dados

```bash
python manage.py migrate
```
ou 
```bash
make migrate
```
### Iniciando o servidor
Execute o comando para iniciar o servidor web no localhost:
```bash
python manage.py runserver
```
ou
```bash
make run
```
