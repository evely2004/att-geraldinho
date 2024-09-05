def contagem_regressiva(N):
   
    if N < 0:
        return

    print(N)
 
    contagem_regressiva(N - 1)

N = 8
contagem_regressiva(N)

