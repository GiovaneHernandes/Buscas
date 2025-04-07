"""
Representação do mapa da Romênia, junto com a heurística - distância
em linha reta do vértice até Bucareste.
"""

class Vertex:
    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)
    
    def show_adjacent(self):
        for adjacent in self.adjacent:
            print(f"Adjacente: {adjacent.vertex.label} - {adjacent.cost} km")


class Ajacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        #NEW
        self.star_distance = vertex.target_distance + cost


class Romania:
    arad = Vertex("Arad", 366)
    zerind = Vertex("Zerind", 374)
    oradea = Vertex("Oradea", 380)
    sibiu = Vertex("Sibiu", 253)
    timisoara = Vertex("Timisoara", 329)
    lugoj = Vertex("Lugoj", 244)
    mehadia = Vertex("Mehadia", 241)
    dobreta = Vertex("Dobreta", 242)
    craiova = Vertex("Craiova", 160)
    rimnicu = Vertex("Rimnicu Vilcea", 193)
    fagaras = Vertex("Fagaras", 178) # <-
    pitesti = Vertex("Pitesti", 98)
    giurgiu = Vertex("Giurgiu", 77)
    bucarest = Vertex("Bucarest", 0)

    arad.add_adjacent(Ajacent(zerind, 75))
    arad.add_adjacent(Ajacent(timisoara, 118))
    arad.add_adjacent(Ajacent(sibiu, 140))

    zerind.add_adjacent(Ajacent(oradea, 71))
    zerind.add_adjacent(Ajacent(arad, 75))

    oradea.add_adjacent(Ajacent(zerind, 71))
    oradea.add_adjacent(Ajacent(sibiu, 151))

    sibiu.add_adjacent(Ajacent(rimnicu, 80))
    sibiu.add_adjacent(Ajacent(fagaras, 99))
    sibiu.add_adjacent(Ajacent(arad, 140))
    sibiu.add_adjacent(Ajacent(oradea, 151))

    timisoara.add_adjacent(Ajacent(lugoj, 111))
    timisoara.add_adjacent(Ajacent(arad, 118))

    lugoj.add_adjacent(Ajacent(mehadia, 70))
    lugoj.add_adjacent(Ajacent(timisoara, 111))

    mehadia.add_adjacent(Ajacent(lugoj, 70))
    mehadia.add_adjacent(Ajacent(dobreta, 75))

    dobreta.add_adjacent(Ajacent(mehadia, 75))
    dobreta.add_adjacent(Ajacent(craiova, 120))

    craiova.add_adjacent(Ajacent(dobreta, 120))
    craiova.add_adjacent(Ajacent(pitesti, 138))
    craiova.add_adjacent(Ajacent(rimnicu, 146))

    rimnicu.add_adjacent(Ajacent(craiova, 146)) #
    rimnicu.add_adjacent(Ajacent(sibiu, 80))
    rimnicu.add_adjacent(Ajacent(pitesti, 97))

    fagaras.add_adjacent(Ajacent(sibiu, 99))#
    fagaras.add_adjacent(Ajacent(bucarest, 211))
    
    pitesti.add_adjacent(Ajacent(craiova, 138))
    pitesti.add_adjacent(Ajacent(rimnicu, 97))
    pitesti.add_adjacent(Ajacent(bucarest, 101))

    bucarest.add_adjacent(Ajacent(pitesti, 101))
    bucarest.add_adjacent(Ajacent(giurgiu, 90))
    bucarest.add_adjacent(Ajacent(fagaras, 211))