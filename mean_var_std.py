import numpy as np

def calculate(list):
    # Verificação se o tamanho da lista fornecida como entrada para o algoritmo é igual a 9
    if len(list) != 9: 
        raise ValueError('List must contain nine numbers.')
    
    matrix = np.array(list).reshape(3, 3)

    # Mean - Média das colunas, linhas e matriz achatada
    mean_axis1 = np.mean(matrix, axis = 0).tolist()
    mean_axis2 = np.mean(matrix, axis = 1).tolist()
    mean_flattened = np.mean(matrix).tolist()

    # Variance - Cálculo da variância das colunas, linhas e matriz achatada
    var_axis1 = np.var(matrix, axis = 0).tolist()
    var_axis2 = np.var(matrix, axis = 1).tolist()
    var_flattened = np.var(matrix).tolist()

    # Standard Deviation - Desvio-padrão das colunas, linhas e matriz achatada
    std_axis1 = np.std(matrix, axis = 0).tolist()
    std_axis2 = np.std(matrix, axis = 1).tolist()
    std_flattened = np.std(matrix).tolist()

    # Maximum - Valores máximos das colunas, linhas e matriz achatada
    max_axis1 = np.max(matrix, axis = 0).tolist()
    max_axis2 = np.max(matrix, axis = 1).tolist()
    max_flattened = np.max(matrix).tolist()

    # Minimum - Valores mínimos das colunas, linhas e matriz achatada
    min_axis1 = np.min(matrix, axis = 0).tolist()
    min_axis2 = np.min(matrix, axis = 1).tolist()
    min_flattened = np.min(matrix).tolist()

    # Sum - Soma das colunas, linhas e matriz achatada
    sum_axis1 = np.sum(matrix, axis = 0).tolist()
    sum_axis2 = np.sum(matrix, axis = 1).tolist()
    sum_flattened = np.sum(matrix).tolist()

    # Dicionário com o resultado acumulado dos cálculos anteriores
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [var_axis1, var_axis2, var_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations