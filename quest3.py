def soma_impares(N):

    if N < 1:
        return 0, []
    
    if N % 2 == 1:
        soma_parcial, impares = soma_impares(N - 2)
        impares.append(N)
        return soma_parcial + N, impares
    else:
        return soma_impares(N - 1)
    
N = 10
resultado, impares = soma_impares(N)
print(f"Os números ímpares menores ou iguais a {N} são: {', '.join(map(str, impares))}")
print(f"O resultado da soma é: {resultado}")



