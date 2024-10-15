from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla,get_original_matrix

matriz = []

matiz_concesioanrio = get_original_matrix()
columnas = ["Garage", "Marca", "Modelo", "Cantidad", "Valor", "Ganancia" ]

def inciar_matriz (matriz:list[list]):
    for i in range(20):
        matriz_garage = [i+1,matiz_concesioanrio[0][i],matiz_concesioanrio[1][i],matiz_concesioanrio[2][i],matiz_concesioanrio[3][i],matiz_concesioanrio[4][i]]
        matriz.append(matriz_garage)
    mostrar_matriz_texto_tabla(matriz, columnas)

inciar_matriz(matriz)

