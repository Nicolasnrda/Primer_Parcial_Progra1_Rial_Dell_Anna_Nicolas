from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla,get_original_matrix

matriz = []

matriz_concesioanrio = get_original_matrix()
columnas = ["Garage", "Marca", "Modelo", "Cantidad", "Valor", "Ganancia" ]


def inciar_matriz (matriz:list[list]):
    cantidad_columnas= len(matriz)
    if cantidad_columnas == 0:
        for i in range(20):
            matriz_garage = [i+1,matriz_concesioanrio[0][i],matriz_concesioanrio[1][i],matriz_concesioanrio[2][i],matriz_concesioanrio[3][i],matriz_concesioanrio[4][i]]
            matriz.append(matriz_garage)
        mostrar_matriz_texto_tabla(matriz, columnas)


if __name__ == "__main__":
    inciar_matriz(matriz)
