# coding: utf-8

import matplotlib.pyplot as plt
import data_model

# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
data_model.print_first_20_registers()



# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
data_model.print_first_20_genders()



# # TAREFA 3
# # TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
column_list = data_model.copy_registers(-2);


# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# DEV Note: Métodos chamados nos asserts foram mudados pelo método implementado em data_model.py 
assert type(data_model.copy_registers()) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(data_model.copy_registers()) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert data_model.copy_registers(-2)[0] == "" and data_model.copy_registers(-2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------



# # TAREFA 4
# # TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

male = len(data_model.get_male_registers())
female = len(data_model.get_female_registers())

# # Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# # -----------------------------------------------------



# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(data_model.count_gender())

# # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# DEV Note: Métodos chamados nos asserts foram mudados pelo método implementado em data_model.py 
assert type(data_model.count_gender()) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(data_model.count_gender()) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert data_model.count_gender()[0] == 935854 and data_model.count_gender()[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# # -----------------------------------------------------



# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", data_model.most_popular_gender())

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(data_model.most_popular_gender()) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert data_model.most_popular_gender() == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = data_model.copy_registers(-2)
types = ["Male", "Female"]
quantity = data_model.count_gender()
y_pos = list(range(len(types)))

plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Genero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Genero')
plt.show(block=True)



# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
user_type_list = data_model.copy_registers(-3)
types = ["Subscriber", "Customer"]
quantity = data_model.count_user_type()
y_pos = list(range(len(types)))

plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuario')
plt.show(block=True)


# TAREFA 8
# TODO: Responda a seguinte questão
male, female = data_model.count_gender()
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_model.get_data_list()))
answer = "Porque parte dos registros não possuem definição de sexo."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Sua resposta aqui.", "TAREFA 8: Sua resposta aqui!"
# -----------------------------------------------------



# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
min_trip, max_trip, mean_trip, median_trip = data_model.get_trip_duration_list()

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------



# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

user_types = data_model.get_start_stations()
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------



# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
# """
# Função de exemplo com anotações.
# Argumentos:
#     param1: O primeiro parâmetro.
#     param2: O segundo parâmetro.
# Retorna:
#     Uma lista de valores x.

# """
