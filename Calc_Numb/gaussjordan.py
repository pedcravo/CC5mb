def GaussJordanMethod(augMat):
    n = len(augMat)
    m = len(augMat[0])

    #print(n,m)

    for i in range(n):
        if augMat[i][i] == 0:
            for j in range(i + 1, n):
                if augMat[j][i] != 0:
                    augMat[i], augMat[j] = augMat[j], augMat[i]
                    break
                else:
                    raise ValueError("Matriz Singular")


        #   Normalizar a linha; definir pivo
        #   L_i <-- L_i/a_ii
        if augMat[i][i] != 1:
            divisor = augMat[i][i]
            for k in range(m):
                augMat[i][k] /= divisor
            if i == 0:
                print(augMat[i])
        else:
            pass

        #   Zerar as entradas referentes aos pivos
        #   L_j <-- L_j - a_ij * L_i 
        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][i] -= coef * augMat[i][k]
                if i == 0 and j == 1:
                    print(augMat[j])
                else:
                    pass
    print(augMat)

matriz = [[3, 2, -4, 3],
          [2, 3, 3, 15],
          [5, -3, 1, 14]]

GaussJordanMethod(matriz)