# coding: utf-8
import csv_util
import my_numpy

# Para facilitar a construção dos métodos, utilizei variáveis globais com o objetivo de reaproveitar as mesmas
global data_list
global gender_column_index
global user_type_column_index
global trip_duration_column_index
global start_station_column_index

data_list = csv_util.open_file_as_list("chicago.csv")

# CSV header: ['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']
data_list = data_list[1:]

# Indices obtidos pela header do documento / removido na linha acima
gender_column_index = -2
user_type_column_index = -3
trip_duration_column_index = 2
start_station_column_index = 3


def get_data_list():
    """Retorna a list de registros do CSV aberto anteriormente
        
        OUTPUT:
            list com os registros do CSV
    """
    return data_list

def print_first_20_registers():
    """Método que implementa a TAREFA 1
    """
    csv_util.print_list_registers(data_list, 0, 20)

def print_first_20_genders():
    """Método que implementa a TAREFA 2
    """
    csv_util.print_list_registers(data_list, 0, 20, gender_column_index)


def copy_registers(column_index=False):
    """Método que implementa a TAREFA 3

        INPUT:
            column_index: caso não definido, todas as colunas serão adicionadas no retorno.
            Caso definido, somente a coluna do column_index será adicionada no retorno

        OUTPUT:
            lista com as colunas definidas pelo param column_index
    """
    return csv_util.get_list_registers(data_list, 0, len(data_list), column_index)


def get_male_registers():
    """Método que implementa a TAREFA 4

        OUTPUT:
            lista com as colunas que contenham Male como valor
    """
    return csv_util.query_registers("Male", data_list, gender_column_index, len(data_list))

def get_female_registers():
    """Método que implementa a TAREFA 4

        OUTPUT:
            lista com as colunas que contenham Female como valor
    """
    return csv_util.query_registers("Female", data_list, gender_column_index, len(data_list))


def count_gender():
    """Método que implementa a TAREFA 5

        OUTPUT:
            lista[2] com as quantidades de registros com Male/Female como valor
            Ex: values[0] // outputs total de registros com Male 
                values[1] // outputs total de registros com Female
    """
    male = len(get_male_registers())
    female = len(get_female_registers())

    return [male, female]


def most_popular_gender():
    """Método que implementa a TAREFA 6

        OUTPUT:
            string com o gênero predominante.
            Possíveis valores: Masculino / Igual / Feminino
    """
    count = count_gender()
    male = count[0]
    female = count[1]
    if (male > female):
        return "Masculino"
    elif (male == female):
        return "Igual"
    else: 
        return "Feminino"
    
def count_user_type():
    """Método que implementa a TAREFA 7

        OUTPUT:
            lista[2] com as quantidades de registros com Subscriber/Customer como valor
            Ex: values[0] // outputs total de registros com Subscriber 
                values[1] // outputs total de registros com Customer 
    """
    subscriber = csv_util.query_registers("Subscriber", data_list, user_type_column_index, len(data_list))
    customer = csv_util.query_registers("Customer", data_list, user_type_column_index, len(data_list))

    return [len(subscriber), len(customer)]

def get_trip_duration_list():
    """Método que implementa a TAREFA 7

        OUTPUT:
            lista[2] com os valores gerais da duração das viagens
            Ex: values[0] // outputs tempo minímo de uma viagem 
                values[1] // outputs tempo máximo de uma viagem
                values[2] // outputs tempo médio de uma viagem
                values[2] // outputs tempo mediano de uma viagem
    """

    # O trecho que converte o array de strings para float poderia ser removido com Numpy
    # assim calculos de mediana, média também.
    # Pelo contexto do projeto, implementei minhas próprias soluções em my_numpy

    data_list = copy_registers(trip_duration_column_index)
    converted_list = my_numpy.convert_array_to_float_values(data_list)

    min = my_numpy.get_min(converted_list)
    max = my_numpy.get_max(converted_list)
    mean = my_numpy.get_mean(converted_list)
    median = my_numpy.get_median(converted_list)

    return [min, max, mean, median]


def get_start_stations():
    """Método que implementa a TAREFA 10

        OUTPUT:
            set de start_station
    """
    return set(copy_registers(3))