""""
Exemplo de algoritimo ganancioso - Dijakstra.
Soluçao do caminho mais curto.
"""


# 1. Definir: representar o grafo (mapa) e a tabela de soluçoes
DISTANCE = 0
PREDECESSOR = 1
INFINIT = float("inf")

map = {
    "A": {"B":5, "D":9, "E":2},
    "B": {"A":5, "C":2},
    "C": {"B":2, "D":3},
    "D": {"A":9, "C":3, "F":2},
    "E": {"A":2, "F":3},
    "F": {"D":2, "E":3},
}

table = {
    "A": [0, None],
    "B": [INFINIT, None],
    "C": [INFINIT, None],
    "D": [INFINIT, None],
    "E": [INFINIT, None],
    "F": [INFINIT, None],
}


#2. Definir funcao que retorna a distancia mais curta de um vetice a partir da origem
def get_shortest_distance(table: dict, vertex: str) -> int:
    """
    Retorna a distancia mais curta de um vertice a partir da origem
    """
    return table[vertex][DISTANCE]


def set_shortest_distance(table: dict, vertex: str, distance: int):
    """
    Funcao que atualiza a distancia mais curta na tabela
    """
    table[vertex][DISTANCE] = distance


def set_predecessor(table: dict, vertex: str, predecessor: str):
    """
    Funcao que atualiza o atecessor do vertice na tabela
    """
    table[vertex][PREDECESSOR] = predecessor


def get_distace(map: dict, first_vertex: str, second_vertex):
    """
    Funcao que retorna a distancia entre 2 verices.
    """
    return map[first_vertex][second_vertex]


def get_next_vertex(table: dict, visited: list):
    """
    Funcao que retorna o proximo vetice a ser visitado
    """

    unvisited = list(
        set(
            table.keys()
        ).difference(visited)
    )

    min_vertex = unvisited[0]
    min_distance = table[unvisited[0]][DISTANCE]

    for vertex in unvisited:
        if table[vertex][DISTANCE] < min_distance:
            min_vertex = vertex
            min_distance = table[vertex][DISTANCE]

    return min_vertex


def find_shortes_path(map: dict, table: dict, origin: str = "A"):
    """
    Funcao principal que resolve o problema do caminho mais curto
    """
    visited = []
    current = origin
    start = origin

    while True:
        adjacent_vertex = map[current]
        
        if set(adjacent_vertex).issubset(set(visited)):
            ...
        else:
            unvisited = set(adjacent_vertex).difference(set(visited))

            for vertex in unvisited:
                distance_from_start = get_shortest_distance(table, vertex)

                if distance_from_start == INFINIT and current == start:
                    total_distance = get_distace(map, vertex, current)
                else:
                    total_distance = get_shortest_distance(table, current)
                    total_distance += get_distace(map, current, vertex)

                if total_distance < distance_from_start:
                    set_shortest_distance(table, vertex, total_distance)
                    set_predecessor(table, vertex, current)
                
        visited.append(current)

        if len(visited) == len(table.keys()):
            break

        current = get_next_vertex(table, visited)

    return table

def rota(destino, solucoes):
    rota = []
    atual = destino

    while atual is not None:
        rota.append(atual)
        atual = solucoes[atual][1]

    return rota[::-1]

result = find_shortes_path(map, table)
print(result)

gps = rota("D", table)
print(gps)