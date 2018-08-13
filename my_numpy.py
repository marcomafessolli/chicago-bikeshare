# coding: utf-8

def convert_array_to_float_values(list):
    """Converte uma lista de strings em uma lista de floats

        OUTPUT:
            lista com seus valores convertidos para Float
    """
    converted_list = []
    for value in list:
        converted_list.append(float(value))

    return converted_list

def sum_list(list):
    """Soma todos os valores de uma lista

        OUTPUT:
            float com a soma de todos os valores da lista
    """
    total = 0
    for value in list:
        total += value

    return total

def get_min(list):
    """Retorna o valor mínimo da lista

        OUTPUT:
            float com o valor mínimo da lista
    """
    min = 9999
    for value in list:
        if (min > value):
            min = value
    
    return min

def get_max(list):
    """Retorna o valor máximo da lista

        OUTPUT:
            float com o valor máximo da lista
    """
    max = 0
    for value in list:
        if (value > max):
            max = value
    
    return max

def get_mean(list):
    """Retorna a média da soma de todos os valores da lista

        OUTPUT:
            float com a média da lista
    """
    total = sum_list(list)
    return total / len(list)

def get_median(list):
    """Retorna a mediana de todos os valores da lista

        OUTPUT:
            float com a mediana da lista
    """
    sorted_list = sorted(list)
    median_index = len(sorted_list) // 2
    if (median_index % 2):
        return sorted_list[median_index]
    else:
        median_value = (sorted_list[median_index] + sorted_list[median_index + 1]) / 2.0
        return median_value