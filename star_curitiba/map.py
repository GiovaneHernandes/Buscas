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


class Parana:
    porto_uniao = Vertex("Porto Uniao", 203)
    paulo_frontin = Vertex("Porto Uniao", 172)
    canoinhas = Vertex("Canoinhas", 141)
    irati = Vertex("Porto Uniao", 139)
    tres_barras = Vertex("Tres Barras", 131)
    sao_matheus = Vertex("São Matheus", 123)
    palmeira = Vertex("Palmeira", 59)
    mafra = Vertex("Mafra", 94)
    lapa = Vertex("Lapa", 74)
    contenda = Vertex("Contenda", 39)
    balsa_nova = Vertex("Balsa Nova", 41)
    araucaria = Vertex("Araucária", 23)
    tijucas_do_sul = Vertex("Tijucas do Sul", 56)
    sao_jose_dos_pinhais = Vertex("São José dos Pinhais", 13)
    curitiba = Vertex("Curitiba", 0)
    campo_largo = Vertex("Campo Largo", 27)


    porto_uniao.add_adjacent(Ajacent(paulo_frontin, 46))
    porto_uniao.add_adjacent(Ajacent(sao_matheus, 87))
    porto_uniao.add_adjacent(Ajacent(canoinhas, 78))

    paulo_frontin.add_adjacent(Ajacent(porto_uniao, 46))
    paulo_frontin.add_adjacent(Ajacent(irati, 75))

    canoinhas.add_adjacent(Ajacent(porto_uniao, 78))
    canoinhas.add_adjacent(Ajacent(tres_barras, 12))
    canoinhas.add_adjacent(Ajacent(mafra, 66))

    irati.add_adjacent(Ajacent(paulo_frontin, 75))
    irati.add_adjacent(Ajacent(palmeira, 75))
    irati.add_adjacent(Ajacent(sao_matheus, 57))

    tres_barras.add_adjacent(Ajacent(canoinhas, 12))
    tres_barras.add_adjacent(Ajacent(sao_matheus, 43))

    sao_matheus.add_adjacent(Ajacent(porto_uniao, 87))
    sao_matheus.add_adjacent(Ajacent(tres_barras, 43))
    sao_matheus.add_adjacent(Ajacent(lapa, 60))
    sao_matheus.add_adjacent(Ajacent(palmeira, 77))
    sao_matheus.add_adjacent(Ajacent(irati, 57))

    palmeira.add_adjacent(Ajacent(irati, 75))
    palmeira.add_adjacent(Ajacent(sao_matheus, 77 ))
    palmeira.add_adjacent(Ajacent(campo_largo, 55))

    mafra.add_adjacent(Ajacent(canoinhas, 66))
    mafra.add_adjacent(Ajacent(tijucas_do_sul, 99))
    mafra.add_adjacent(Ajacent(lapa, 57))

    lapa.add_adjacent(Ajacent(mafra, 57))
    lapa.add_adjacent(Ajacent(sao_matheus, 60))
    lapa.add_adjacent(Ajacent(contenda, 26))

    contenda.add_adjacent(Ajacent(lapa, 26))
    contenda.add_adjacent(Ajacent(araucaria, 18))
    contenda.add_adjacent(Ajacent(balsa_nova, 19))

    balsa_nova.add_adjacent(Ajacent(contenda, 19))
    balsa_nova.add_adjacent(Ajacent(curitiba, 51))
    balsa_nova.add_adjacent(Ajacent(campo_largo, 22))

    araucaria.add_adjacent(Ajacent(contenda, 18))
    araucaria.add_adjacent(Ajacent(curitiba, 37))

    tijucas_do_sul.add_adjacent(Ajacent(mafra, 99))
    tijucas_do_sul.add_adjacent(Ajacent(sao_jose_dos_pinhais, 49))

    sao_jose_dos_pinhais.add_adjacent(Ajacent(tijucas_do_sul, 49))
    sao_jose_dos_pinhais.add_adjacent(Ajacent(curitiba, 15))
    
    curitiba.add_adjacent(Ajacent(araucaria, 37))
    curitiba.add_adjacent(Ajacent(sao_jose_dos_pinhais, 15))
    curitiba.add_adjacent(Ajacent(balsa_nova, 51))
    curitiba.add_adjacent(Ajacent(campo_largo, 29))

    campo_largo.add_adjacent(Ajacent(curitiba, 29))
    campo_largo.add_adjacent(Ajacent(balsa_nova, 22))
    campo_largo.add_adjacent(Ajacent(palmeira, 55))