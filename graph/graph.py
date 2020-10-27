class Vertice:
    def __init__(self):
        self._repr = ''
        self._cabeca_lista_adjacencia = None


class Adjacencia:
    def __init__(self, vertice, peso):
        self._vertice = vertice
        self._peso = peso
        self._proximo = None


class Graph:
    def __init__(self, total_vertices):
        self._total_vertices = total_vertices
        self._total_arestas = 0
        self._adjacencias = [Vertice() for _ in range(self._total_vertices)]


def cria_grafo(total_vertices):
    grafo = Graph(total_vertices)


    return grafo


def cria_adjacencia(vertice, peso):
    adjacencia = Adjacencia(vertice, peso)

    return adjacencia


def cria_aresta(grafo, vertice_inicial, vertice_final, peso):
    if not grafo:
        return False
    if vertice_final < 0 or vertice_final >= grafo._total_vertices:
        return False
    if vertice_inicial < 0 or vertice_inicial >= grafo._total_vertices:
        return False
    
    nova_adjacencia = cria_adjacencia(vertice_final, peso)
    nova_adjacencia._proximo = grafo._adjacencias[vertice_inicial]._cabeca_lista_adjacencia

    grafo._adjacencias[vertice_inicial]._cabeca_lista_adjacencia = nova_adjacencia
    grafo._total_arestas += 1

    return True


def imprime_grafo(grafo):
    print("Vertices: {} \nArestas: {}\n\n".format(
        grafo._total_vertices, grafo._total_arestas))

    for i in range(grafo._total_vertices):
        adjacencia = grafo._adjacencias[i]._cabeca_lista_adjacencia
        
        texto = ["V{}: ".format(i)]

        while(adjacencia):
            texto.append("-> V{}({}) ".format(adjacencia._vertice, adjacencia._peso))

            adjacencia = adjacencia._proximo

        texto.append("\n")
        print(''.join(texto))


def inicializa_grafo(grafo, distancias, predecessores, vertice_inicial):
    for _ in range(grafo._total_vertices):
        distancias.append(float("inf"))
        predecessores.append(-1)

    distancias[vertice_inicial] = 0


def relaxa_aresta(grafo, distancias, predecessores, vertice_inicial, vertice_final):
    adjacencia = grafo._adjacencias[vertice_inicial]._cabeca_lista_adjacencia

    while(adjacencia and adjacencia._vertice != vertice_final):
        adjacencia = adjacencia._proximo

    if adjacencia:
        if distancias[vertice_final] > distancias[vertice_inicial] + adjacencia._peso:
            distancias[vertice_final] = distancias[vertice_inicial] + adjacencia._peso
            predecessores[vertice_final] = vertice_inicial


def existe_aberto(grafo, abertos):
    for i in range(grafo._total_vertices):
        if abertos[i]:
            return True

    return False

def menor_distancia(grafo, abertos, distancias):
    aberto_index = None
    for i in range(grafo._total_vertices):
        if abertos[i]:
            aberto_index = i
            break

    if aberto_index == grafo._total_vertices:
        return -1

    menor = i

    for i in range(menor+1, grafo._total_vertices):
        if abertos[i] and distancias[menor] > distancias[i]:
            menor = i

    return menor

def dirjkstra(grafo, vertice_inicial):
    distancias = []
    predecessores = []
    inicializa_grafo(grafo, distancias, predecessores, vertice_inicial)
    abertos = []

    for i in range(grafo._total_vertices):
        abertos.append(True)

    while existe_aberto(g, abertos):
        vertice_inicial = menor_distancia(g, abertos, distancias)
        abertos[vertice_inicial] = False

        adjacencia = grafo._adjacencias[vertice_inicial]._cabeca_lista_adjacencia
        while adjacencia:
            relaxa_aresta(grafo, distancias, predecessores, vertice_inicial, adjacencia._vertice)
            adjacencia = adjacencia._proximo

    return distancias


if __name__ == "__main__":
    g = cria_grafo(5)
    cria_aresta(g, 0, 1, 10)
    cria_aresta(g, 0, 2, 20)
    cria_aresta(g, 0, 3, 75)
    cria_aresta(g, 0, 4, 56)
    cria_aresta(g, 1, 2, 5)
    cria_aresta(g, 2, 4, 20)
    cria_aresta(g, 4, 3, 5)

    result = dirjkstra(g, 0)

    for i in range(g._total_vertices):
        print("D(v0 -> v{}) = {}\n".format(i, result[i]))
