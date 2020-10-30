# Routes API

# Table of contents
   * [Introdução](#introdução)
     * [Funcionamento](#funcionamento)
     * [Resolução](#resolução)
   * [Configurando o ambiente local](#configurando-o-ambiente-local)
   * [Interface CLI](#interface-cli)
   * [Interface REST](#interface-rest)
     * [API Documentação](#api-documentação)
   * [References](#references)

# Introdução

Encontra a rota mais barata possível entre dois lugares, através de duas interfaces: CLI e REST.

## Funcionamento

A entrada dos locais disponíveis para viagem se dará através da leitura de arquivos CSV, onde cada linha contém o `local de origem`, `local de destino` e o `valor da viagem` no trecho, separados por virgula, conforme o exemplo abaixo:

```
AAA,BBB,10
BBB,SSS,5
AAA,ZZZ,75
AAA,SSS,20
AAA,YYY,56
YYY,ZZZ,5
SSS,YYY,20
```

Se desejamos ir do `local de origem` até o `local de destino`, existem as seguintes rotas possíveis:

AAA - ZZZ no valor de R$75
AAA - YYY - CGD no valor de R$64
AAA - SSS - YYY - ZZZ no valor de R$45
AAA - BBB - SSS - YYY - ZZZ no valor de R$40

O melhor preço é da rota 4 logo, o output da consulta deve ser AAA - BBB - SSS - OOO - ZZZ.

## Resolução

Para a resolução do problema foi utilizada a implementação da estrutura de dados grafo, onde cada local representa um vertice desse grafo, os caminhos entre os locais representam as arestas direcionadas, e o preço das passagens representam os pesos das arestas.

A implementação do grafo direcionado com peso nas arestas foi implementado inicialmente com lista de adjacencias, com o objetivo de facilitar a busca, e em seguida, para facilitar o acesso aos vértices do grafo, a implementação foi enriquecida com o uso de dicionários do python.

Dada a estrutura e a implementação, a realização busca do caminho mais barato se deu através da implemetação do algoritmo de Dirjkstra, que encontra o caminho mais barato em termos de peso total das arestas que compõem o caminho.

![dirjkstra](https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra#/media/Ficheiro:Dijkstra_Animation.gif)

# Configurando o ambiente local

Uma vez que o docker está instalado em seu computador, execute os seguintes passos:

clonar o projeto

    git clone git@github.com:danilolmoura/routes-api.git

criar e executar a imagem localmente

    cd routes-api
    docker-compose build
    docker-compose up -d

Os logs de execução da aplicação poderão ser visualizados através dos comandos abaixo:

	docker ps | grep routes-api   ## Para buscar o CONTAINER_ID que está executando
	docker logs <CONTAINER_ID>


# Interface CLI

A inicialização do teste através da interface CLI se dará executando o comando abaixo, na linha de comando, na pasta do projeto. O primeiro argumento é o o diretório com o arquivo de rotas inicial:

    docker ps # para listar os containers ativos e pegar CONTAINER_ID
    docker exec -it 855be38d0a9e python app_cli.py check-route -f files/input-routes.csv

E então a interface abaixo aparecerá. Nessa nova interface, a melhor rota poderá ser buscada digitando a origem e destino no formato "DE-PARA"

    please enter the route: GRU-CGD
    best route: GRU - BRC - SCL - ORL - CDG > $40

    please enter the route: BRC-CDG
    best route: BRC - ORL > $30

# Interface REST

A interface REST utiliza o padrão HTTP, e através dela é possível buscar o caminho mais barato entre dois e adicionar novos caminhos no arquivo de lugares

A interface poderá ser acessada em http://127.0.0.1:5000/

## API Documentação

A documentação da API pode ser acessada [clicando aqui](/DOCS.md)

# References

* [Docker](https://www.docker.com/get-started)
* [Flask](http://flask.palletsprojects.com/en/1.1.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)




