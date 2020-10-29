class Vertice:
    def __init__(self, label):
        self.label = label
        self._cabeca_lista_adjacencia = None
        self._anterior = None


class Adjacencia:
    def __init__(self, vertice, peso):
        self._vertice = vertice
        self._peso = peso
        self._proximo = None


class Graph:
    def __init__(self):
        self._total_vertices = 0
        self._total_arestas = 0
        self._adjacencias = {}

    def add_adjacencia(self, label):
        if label not in self._adjacencias.keys():
            self._adjacencias[label] = Vertice(label)
            self._total_vertices += 1

def cria_grafo():
    grafo = Graph()

    labels = []
    f = open('files/input-routes.csv')
    lines = f.readlines()
    for line in lines:
        line_items = line.replace('\n', '').split(',')

        if line_items[0] not in labels:
            grafo.add_adjacencia(line_items[0])
        
        if line_items[1] not in labels:
            grafo.add_adjacencia(line_items[1])

        cria_aresta(grafo, line_items[0], line_items[1], int(line_items[2]))

    return grafo


def cria_adjacencia(vertice, peso):
    adjacencia = Adjacencia(vertice, peso)

    return adjacencia


def cria_aresta(grafo, vertice_inicial, vertice_final, peso):
    if not grafo:
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
    for i in grafo._adjacencias.keys():
        distancias[i] = float("inf")
        predecessores[i] = -1

    distancias[vertice_inicial] = 0


def relaxa_aresta(grafo, distancias, predecessores, vertice_inicial, vertice_final):
    adjacencia = grafo._adjacencias[vertice_inicial]._cabeca_lista_adjacencia

    while(adjacencia and adjacencia._vertice != vertice_final):
        adjacencia = adjacencia._proximo

    if adjacencia:
        if distancias[vertice_final] > distancias[vertice_inicial] + adjacencia._peso:
            distancias[vertice_final] = distancias[vertice_inicial] + adjacencia._peso
            predecessores[vertice_final] = vertice_inicial

            grafo._adjacencias[vertice_final]._anterior = vertice_inicial

def existe_aberto(abertos):
    if True in abertos.values():
        return True

    return False

def menor_distancia(grafo, abertos, distancias):
    menor_distancia = float("inf")
    menor_distancia_vertice = None
    for k, v in abertos.items():
        if v:
            if distancias[k] < menor_distancia:
                menor_distancia = distancias[k]
                menor_distancia_vertice = k

    return menor_distancia_vertice

def dirjkstra(grafo, vertice_inicial):
    distancias = {}
    predecessores = {}
    inicializa_grafo(grafo, distancias, predecessores, vertice_inicial)
    abertos = {}

    for i in grafo._adjacencias.keys():
        abertos[i] = True

    while existe_aberto(abertos):
        vertice_inicial = menor_distancia(grafo, abertos, distancias)
        if not vertice_inicial:
            break

        abertos[vertice_inicial] = False
        adjacencia = grafo._adjacencias[vertice_inicial]._cabeca_lista_adjacencia
        while adjacencia:
            relaxa_aresta(grafo, distancias, predecessores, vertice_inicial, adjacencia._vertice)
            adjacencia = adjacencia._proximo

    return distancias


def get_best_route_price(vertice_inicial, vertice_final):
    grafo = cria_grafo()
    result = dirjkstra(grafo, vertice_inicial)

    route_value = result[vertice_final]

    route_path = []
    last_path = vertice_final
    while last_path:
        route_path.append(last_path)
        last_path  = grafo._adjacencias[last_path]._anterior

    route_path = ' - '.join(route_path[::-1])
    route_path += ' > ${}'.format(route_value)

    return route_path

if __name__ == "__main__":
    pass


