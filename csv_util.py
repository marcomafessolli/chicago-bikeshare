# coding: utf-8
import csv

def open_file_as_list(file_name):
    """Abre um arquivo CSV e retorna o mesmo como lista

        OUTPUT:
            lista com os valores lidos no arquivo CSV
    """
    print("\n\nLendo o documento...")

    with open(file_name, "r") as file_read:
        reader = csv.reader(file_read)
        return list(reader)

def get_list_registers(list, first, last, fixed_column=False):
    """Retorna uma nova lista com os filtros definidos pelos parametros

        INPUT:
            list: a lista a ser filtrada
            first(int): indice inicial do filtro
            last(int): indice final do filtro
            fixed_column: caso não definido, todas as colunas serão adicionadas no retorno.
            Caso definido, somente a coluna do fixed_column será adicionada no retorno 

        OUTPUT:
            lista com os valores filtrados pelos parametros
    """
    data_list = []
    for index in range(first, last):
        if (fixed_column != False):
            data = list[index][fixed_column]
            data_list.append(data)
        else:
            data_list.append(list[index])

    return data_list

def query_registers(query, list, fixed_column=False, limit=20):
    """Retorna uma nova lista com registros iguais a query e com os filtros definidos pelos parametros

        INPUT:
            query(string): String a ser comparada nos valores da lista
            list: a lista a ser filtrada
            fixed_column: caso não definido, todas as colunas serão adicionadas no retorno.
            Caso definido, somente a coluna do fixed_column será adicionada no retorno 
            limit(int): Quantidade de registros na nova lista

        OUTPUT:
            lista com os valores filtrados pelos parametros
    """
    data_list = get_list_registers(list, 0, limit)
    queried_list = []
    for list_register in data_list:
        if (fixed_column):
            if (list_register[fixed_column] == query):
                queried_list.append(list_register)
        else:
            for register in list_register:
                if (register == query):
                    queried_list.append(list_register)
                    break
        

    return queried_list


def print_list_registers(list, first, last, fixed_column=False):
    """Printa os valores da lista com os filtros definidos pelos parametros

        INPUT:
            list: a lista a ser filtrada
            first(int): indice inicial do filtro
            last(int): indice final do filtro
            fixed_column: caso não definido, todas as colunas serão adicionadas no retorno.
            Caso definido, somente a coluna do fixed_column será adicionada no retorno 
    """
    data_list = get_list_registers(list, first, last, fixed_column)
    for register in data_list:
        if (register):
            print(register)
        else:
            print("Not Defined")
