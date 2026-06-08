def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números. Lança ValueError se b for zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def calcular_media(lista):
    """Retorna a média aritmética de uma lista de números. Lança ValueError se a lista estiver vazia."""
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")
    return sum(lista) / len(lista)
