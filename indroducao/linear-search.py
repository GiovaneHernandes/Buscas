"""
Exemplo de busca linear.
"""


def search(elements: list, element: int)-> int:
    """
    Função que recebe uma lista e um valor, para que o algorítimo faça a busca.
    """
    ...

    for index,value in enumerate(elements):
        # Caso base - condição que faz o loop parar.
        if value == element:
            print(index)
        
    return "Elemento nao encontrado"




elements = [3,4,1,6,14]
result = search(elements, 14)
print(f"O indice do elemento é: {result}")