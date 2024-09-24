import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(lista).reshape(3, 3)
    
    mean = [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), matriz.mean().tolist()]
    variance = [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), matriz.var().tolist()]
    std_dev = [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), matriz.std().tolist()]
    max_val = [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), matriz.max().tolist()]
    min_val = [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), matriz.min().tolist()]
    sum_val = [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), matriz.sum().tolist()]
    
    calculos = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    return calculos
