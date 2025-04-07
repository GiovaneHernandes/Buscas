"""
Exemplo de Greed Search.
"""

from map import Romania
from sort import Sort


class Routes:
    def __init__(self, target):
        self.target = target
        self.found = False

    def search(self, current):
        print(f"\nAtual: {current.label}")
        current.visited = True

        if current == self.target:
            self.found = True
        else:
            sorted_routes = Sort(len(current.adjacent))

            for adjacent in current.adjacent:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    sorted_routes.insert(adjacent.vertex)
            
            sorted_routes.show_array()

            if sorted_routes.array[0]:
                self.search(sorted_routes.array[0])


if __name__ == "__main__":
    map = Romania()
    gps = Routes(map.bucarest)
    gps.search(map.arad)