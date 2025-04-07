"""
Exemplo de buscas binaria, utilizando o conseito de 'Divisão e Conquista'.
"""



def search(elements: list, element: int, end: int, start: int = 0):
    """

    """
    # Caso base
    while start <= end:
        mid = start + ((end - start) // 2)

        # Caso loop
        if elements[mid] == element:
            return mid
        elif elements[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    
    return "Elemento não encontrado."


elements = [4,6,9,13,14,18,21,24,38]
element = 13

result = search(elements, element, len(elements) - 1)
print(f"O indice do elemesnto é: {result}")