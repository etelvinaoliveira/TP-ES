# Escopo do sistema

## Objetivo:

Este projeto tem como objetivo criar um site para publicação de artigos voltado para temas relacionados à área da Ciência da Computação.  Além disso, também permite a interação dos usuários com os posts. No que diz respeito aos requisitos não funcionais, temos como objetivo implementar testes para garantir a robustez do sistema.

## Principais Features:

#### Cadastro de Usuário
Para realizar publicações, o usuário precisa realizar o login (ou cadastro) para sua autenticação no sistema. Assim, os dados são coletados e inseridos no banco de dados.

#### Filtragem por busca 
Os usuários possuem a opção de filtrar artigos por palavras-chave e/ou tópicos relevantes ao usuário.


#### Gerenciamento de Publicações
O usuário, após realizar a sua autenticação no sistema, pode criar, editar, remover e publicar artigos.


#### Filtragem por Categoria
Os usuários podem filtrar os posts relacionados a uma categoria específica.


#### Interações com o post
Os usuários poderão favoritar posts e comentar qualquer publicação.


##  Membros da equipe e papel

* Etelvina Costa Santos Sá Oliveira: Full Stack


* Indra Matsiendra Cardoso Dias Ribeiro: Full Stack


* Leonardo de Oliveira Maia: Full Stack


* Rafaela de Fátima Silva Alexandre: Full Stack


* Pedro Henrique Meireles de Almeida: Full Stack



## Tecnologias:

* Python

* Django 

* SQLite

* HTML

* CSS

## Backlog do Produto

* Como usuário, eu gostaria de me cadastrar no site
* Como usuário, eu gostaria de fazer login no site
* Como usuário, eu gostaria de criar publicações
* Como usuário, eu gostaria de ver a lista das publicações do site
* Como usuário, eu gostaria de ler publicações
* Como usuário, eu gostaria de editar e deletar publicações
* Como usuário, eu gostaria de realizar a busca de publicações por título
* Como usuário, eu gostaria de filtrar por categoria publicações
* Como usuário, eu gostaria de realizar a busca de publicações por autor
* Como usuário, eu gostaria de visualizar o histórico das últimas publicações lidas
* Como usuário, eu gostaria de visualizar as minhas publicações
* Como usuário, eu gostaria de comentar publicações
* Como usuário, eu gostaria de curtir publicações
* Como usuário, eu gostaria de salvar publicações

## Backlog da Sprint

### História #1: Como usuário, eu gostaria de me cadastrar no site
#### Tarefas e responsáveis:
* Instalar o Django [Todos]
* Instalar o SQLite, criar banco de dados e tabelas de usuário [Indra]
* Implementar uma versão inicial da tela de cadastro do usuário [Rafaela]
* Implementar regras para o cadastro do nome e senha do usuário [Rafaela]
* Implementar no backend a lógica de cadastro do usuário [Rafaela] 

### História #2: Como usuário, eu gostaria de fazer login no site
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de login do usuário [Leonardo]
* Implementar no backend a lógica de login do usuário [Leonardo]

### História #3: Como usuário, eu gostaria de ver a lista das publicações do site
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de listagem de posts, que será a tela inicial do site [Etelvina]
* Criar no banco de dados tabelas de publicações [Indra]
* Ordenar na tela inicial as publicações por data da última atualização [Etelvina]
* Implementar no backend a lógica de listagem de posts [Etelvina]

### História #4: Como usuário, eu gostaria de ler publicações
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de visualização do artigo completo [Indra]
* Implementar no backend a lógica de visualização de posts [Indra]

### História #5: Como usuário, eu gostaria de criar publicações
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de criação de posts [Pedro]
* Restringir a criação de publicações a usuários devidamente logados no site [Pedro]
* Implementar no backend a lógica de tela de criação de posts [Pedro]

## Versão Revisada Backlog da Sprint

### História #1: Como usuário, eu gostaria de me cadastrar no site
#### Tarefas e responsáveis:
* Instalar o Django [Todos]
* Instalar o SQLite, criar banco de dados e tabelas de usuário [Indra]
* Implementar uma versão inicial da tela de cadastro do usuário [Rafaela]
* Implementar regras para o cadastro do nome e senha do usuário [Rafaela]
* Implementar no backend a lógica de cadastro do usuário [Rafaela] 

### História #2: Como usuário, eu gostaria de fazer login no site
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de login do usuário [Leonardo]
* Implementar no backend a lógica de login do usuário [Leonardo]

### História #3: Como usuário, eu gostaria de criar publicações
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de criação de posts [Pedro]
* Restringir a criação de publicações a usuários devidamente logados no site [Pedro]
* Implementar no backend a lógica de tela de criação de posts [Pedro]

### História #4: Como usuário, eu gostaria de ver a lista das publicações do site
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de listagem de posts, que será a tela inicial do site [Etelvina]
* Criar no banco de dados tabelas de publicações [Indra]
* Ordenar na tela inicial as publicações por data da última atualização [Etelvina]
* Implementar no backend a lógica de listagem de posts [Etelvina]

### História #5: Como usuário, eu gostaria de ler publicações
#### Tarefas e responsáveis:
* Implementar uma versão inicial da tela de visualização do artigo completo [Indra]
* Implementar no backend a lógica de visualização de posts [Indra]



### Diagrama UML

![UML](https://github.com/etelvinaoliveira/TP-ES/assets/85119132/f438f08c-3bb0-40fe-ae30-f69e16a230fc)


### Diagrama de atividades

![Diagrama_sem_nome drawio](https://github.com/etelvinaoliveira/TP-ES/assets/85119132/81ce9b3e-720d-4698-9785-090de24f22d2)


