# DOCUMENTAÇÃO

# Table of contents
   * [Descrição](#descrição)
   * [Cabeçalho](#cabeçalho)
   * [Buscar melhor caminho (BMC)](#buscar-melhor-caminho-bmc)
      * [Exemplo busca](#exemplo-busca)
   * [Adicionar caminho (AC)](#adicionar-caminho-ac)
      * [Exemplo adição](#exemplo-adição)

## Descrição

A interface da API utiliza o padrão `HTTP REST`, e através dela é possível   se dará executando o comando abaixo, na linha de comando, na pasta do projeto. O primeiro argumento é o o diretório com o arquivo de rotas inicial

## Cabeçalho

Para cada requisição realizada para a API, **é necessário** adicionar o `Content-type` conforme o exemplo abaixo:
```json
{
	"Content-Type": "application/json"
}
```

## Buscar melhor caminho (BMC)

Através desse recurso, é possível encontrar o caminho mais barato entre dois lugares, considerando os pontos abaixo:

- Caso mais de um caminho seja encontrado, a resposta será o caminho com o menor custo.
- Caso o menor custo seja encontrado em dois caminhos, somente o último caminho encontrado pelo algoritmo será devolvido.

### Exemplo busca

```json
GET /route/find?initial_position=CDG&final_position=GRU
```

Na resposta, será retornado o melhor caminho encontrado pela API:
```json
HTTP Response 200

"GRU - BRC - SCL - ORL - CDG > $40"
```

Ou, retornará um dos casos abaixo:

Exceção caso a `initial_position` não exista como posição no arquivo:
```json
HTTP Response 400

"Initial position does not exist: LLL"
```

Exceção caso a `final_position` não exista como posição no arquivo:
```json
HTTP Response 400

"Final position does not exist: LLL"
```

Caso não seja possível chegar da `initial_positon` até a `final_position`, a resposta será no formato abaixo:
```json
HTTP Response 200

"It is not possible to go from CDG to GRU"
```

## Adicionar caminho (AC)

Através deste recurso é possível criar um novo caminho entre os lugares:

- Não é necessário adicionar o `id` do parceiro em sua criação.
- Todos os campos são obrigatórios, exceto o `id`
- Não é possível cadastrar um parceiro com o mesmo `document`.

### Exemplo adição

```json
POST /route/add

{
	"initial_position": "GRU",
	"final_position": "SSA",
	"weight": 50
}
```

Na resposta, será retornado um valor booleano `true` em caso de sucesso:
```json
HTTP Response 200

true
```

Ou, retornará um dos casos abaixo:

Exceção caso a `initial_position` não seja uma `string`:
```json
HTTP Response 400

"Invalid initial_position format, expected string"
```

Exceção caso a `final_position` não seja uma `string`:
```json
HTTP Response 400

"Invalid final_position format, expected string"
```

Exceção caso o `weight` não seja seja um `int`, maior que `0`:
```json
HTTP Response 400

"Invalid weight format, expected int bigger than 0"
```
