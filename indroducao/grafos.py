class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []

    def adciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo) 

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

class Grafo:
    arad = Vertice("Arad", 366)
    zerind = Vertice("Zerind", 374)
    oradea = Vertice("Oradea", 380)
    sibiu = Vertice("Sibiu", 253)
    timisoara = Vertice("Timisoara", 329)
    lugoj = Vertice("Lugoj", 244)
    mehadia = Vertice("Mehadia", 241)
    dobreta = Vertice("Dobreta", 242)
    craiova = Vertice("Craiova", 160)
    rimnicu = Vertice("Rimnicu Vilcea", 193)
    fagaras = Vertice("Fagaras", 178)
    pitesti = Vertice("Pitesti", 98)
    bucarest = Vertice("Bucarest", 0)
    giurgiu = Vertice("Giurgiu", 77)


    arad.adciona_adjacente(Adjacente(zerind, 75))
    arad.adciona_adjacente(Adjacente(timisoara, 118))
    arad.adciona_adjacente(Adjacente(sibiu, 140))

    zerind.adciona_adjacente(Adjacente(oradea, 71))
    zerind.adciona_adjacente(Adjacente(arad, 75))

    oradea.adciona_adjacente(Adjacente(zerind, 71))
    oradea.adciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adciona_adjacente(Adjacente(rimnicu, 80))
    sibiu.adciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adciona_adjacente(Adjacente(arad, 140))
    sibiu.adciona_adjacente(Adjacente(oradea, 151))

    timisoara.adciona_adjacente(Adjacente(lugoj, 111))
    timisoara.adciona_adjacente(Adjacente(arad, 118))

    lugoj.adciona_adjacente(Adjacente(mehadia, 70))
    lugoj.adciona_adjacente(Adjacente(timisoara, 111))

    mehadia.adciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adciona_adjacente(Adjacente(craiova, 120))

    craiova.adciona_adjacente(Adjacente(dobreta, 120))
    craiova.adciona_adjacente(Adjacente(pitesti, 138))
    craiova.adciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adciona_adjacente(Adjacente(craiova, 146)) #
    rimnicu.adciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adciona_adjacente(Adjacente(sibiu, 99))#
    fagaras.adciona_adjacente(Adjacente(bucarest, 211))
    
    pitesti.adciona_adjacente(Adjacente(craiova, 138))
    pitesti.adciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adciona_adjacente(Adjacente(bucarest, 101))

    bucarest.adciona_adjacente(Adjacente(pitesti, 101))
    bucarest.adciona_adjacente(Adjacente(giurgiu, 90))
    bucarest.adciona_adjacente(Adjacente(fagaras, 211))