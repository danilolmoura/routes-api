class Node:
    def __init__(self, label):
        self.label = label
        self.head_adjacency_list = None
        self.previous = None


class Adjacency:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
        self.next = None


class Graph:
    def __init__(self):
        self.total_nodes = 0
        self.total_edges = 0
        self.nodes = {}

    def add_node(self, label):
        """[Add node to the Graph]

        Args:
            label ([str]): [label of new node]
        """        
        if label not in self.nodes.keys():
            self.nodes[label] = Node(label)
            self.total_nodes += 1


def create_graph(file_path):
    """[Create a graph and fill it with data of file]

    Args:
        file_path ([str]): [path from file]

    Returns:
        [Graph]: [object of Graph]
    """    
    graph = Graph()

    labels = []
    f = open(file_path)
    lines = f.readlines()
    f.close()

    for line in lines:
        line_items = line.replace('\n', '').split(',')

        if line_items[0] not in labels:
            graph.add_node(line_items[0])
        
        if line_items[1] not in labels:
            graph.add_node(line_items[1])

        create_edge(graph, line_items[0], line_items[1], int(line_items[2]))

    return graph


def create_edge(graph, initial_node, final_node, weight):
    """[Create edge between two nodes]

    Args:
        graph ([Graph]): object of Graph
        initial_node ([str]): [label of initial node]
        final_node ([str]): [label of final node]
        weight ([type]): [weight of edge]

    Returns:
        [bool]: [True if edge was created, False if edge was not created]
    """    
    if not graph:
        return False
    
    new_adjacency = Adjacency(final_node, weight)

    new_adjacency.next = graph.nodes[initial_node].head_adjacency_list

    graph.nodes[initial_node].head_adjacency_list = new_adjacency
    graph.total_edges += 1

    return True


def initialize_graph(graph, distances, predecessors, initial_node):
    """[Define default values]

    Args:
        graph ([Graph]): object of Graph
        distances ([dict]): [dict containing node label and information about its current lowest distance, example {'GRU': 0, 'SCL': 20}]
        predecessors ([dict]): [dict where keys are node labels and each value is label of current previous node]
        initial_node ([str]): [label of initial node]
    """    
    for i in graph.nodes.keys():
        distances[i] = float("inf")
        predecessors[i] = -1

    distances[initial_node] = 0


def relax_edge(graph, distances, predecessors, initial_node, final_node):
    """[Change distance value, if distance between two node is smallest than previous distance]

    Args:
        graph ([Graph]): object of Graph
        distances ([dict]): [dict containing node label and information about its current lowest distance, example {'GRU': 0, 'SCL': 20}]
        predecessors ([dict]): [dict where keys are node labels and each value is label of current previous node]
        initial_node ([str]): label of initial node
        final_node ([str]): label of initial
    """    
    adjacency = graph.nodes[initial_node].head_adjacency_list

    while(adjacency and adjacency.node != final_node):
        adjacency = adjacency.next

    if adjacency:
        if distances[final_node] > distances[initial_node] + adjacency.weight:
            distances[final_node] = distances[initial_node] + adjacency.weight
            predecessors[final_node] = initial_node

            graph.nodes[final_node].previous = initial_node


def open_exists(open_node):
    """[Check if exists some open node]

    Args:
        open_node ([dict]): [dict containing node label and information if it is open or close, example {'GRU': True, 'SCL': False}]

    Returns:
        [bool]: [True if exists some item from open_node checked as True, False doesn't exist any item from open_node checked as True]
    """    
    if True in open_node.values():
        return True

    return False


def smallest_distancee(graph, open_node, distances):
    """[Finds the node with the smallest distance between the open nodes]

    Args:
        graph ([Graph]): object of Graph
        open_node ([dict]): [dict containing node label and information if it is open or close, example {'GRU': True, 'SCL': False}]
        distances ([type]): [dict containing node label and information about its current lowest distance, example {'GRU': 0, 'SCL': 20}]

    Returns:
        [str]: [label of node with the smallest distance]
    """    
    smallest_distancee_value = float("inf")
    smallest_distancee_node = None

    for k, v in open_node.items():
        if v:
            if distances[k] < smallest_distancee_value:
                smallest_distancee_value = distances[k]
                smallest_distancee_node = k

    return smallest_distancee_node


def dirjkstra(graph, initial_node):
    """ Finds the lower path between an initial node and all other node of graph

    Args:
        graph ([Graph]): object of Graph
        initial_node ([str]): label of node where search will begin

    Returns:
        [dict]: [dict which keys are node labels and the values are its distaces from initial_node, example {'GRU': 0, 'SCL': 20}]
    """    
    distances = {}
    predecessors = {}
    initialize_graph(graph, distances, predecessors, initial_node)
    open_node = {}

    for i in graph.nodes.keys():
        open_node[i] = True

    while open_exists(open_node):
        initial_node = smallest_distancee(graph, open_node, distances)
        if not initial_node:
            break

        open_node[initial_node] = False
        adjacency = graph.nodes[initial_node].head_adjacency_list
        while adjacency:
            relax_edge(graph, distances, predecessors, initial_node, adjacency.node)
            adjacency = adjacency.next

    return distances


def get_best_route_price(graph, initial_node, final_node):
    """ Get best route between two node in a Graph

    Args:
        graph ([Graph]): object of Graph
        initial_node ([str]): label of node where search will begin
        final_node ([str]): label of node where search will end

    Returns:
        [str]: path from initial to final node, formatted as expected, if it exists
    """
    result = dirjkstra(graph, initial_node)

    route_cost = result[final_node]

    if route_cost == float('inf'):
        return route_cost

    route_path = []
    last_path = final_node
    while last_path:
        route_path.append(last_path)
        last_path  = graph.nodes[last_path].previous

    route_path = ' - '.join(route_path[::-1])
    route_path += ' > ${}'.format(route_cost)

    return route_path
