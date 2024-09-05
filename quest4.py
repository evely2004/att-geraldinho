
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f"função(3) = {fibonacci(3)}")  
print(f"função(6) = {fibonacci(6)}")  
print(f"função(7) = {fibonacci(7)}")  
print(f"função(12) = {fibonacci(12)}") 
