# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    resultado = []
    for list in matrix:
        for elemento in list:
            resultado.append(elemento)
    return resultado

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    resultado = []
    for list in matrix:
        suma = 0
        for elemento in list:
            suma = suma + elemento
        resultado.append(suma)
    return resultado



def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    if len(matrix) ==0:
        return []
    num_colms = len(matrix[0])
    resultado = []
    for col in range(num_colms):
        total = 0
        for fila in matrix:
            total= total + fila[col]
        resultado.append(total)
    return resultado


