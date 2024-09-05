def exibir_ate(N):
    if N < 0:
        return
    
    exibir_ate(N - 1)
  
    print(N)

N = 6
exibir_ate(N)
