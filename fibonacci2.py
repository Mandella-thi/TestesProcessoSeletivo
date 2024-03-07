def fibonacci_teste(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

x = int(input("Digite o número que deseja testar na sequência de Fibonacci: "))

if fibonacci_teste(x):
    print("O número pertence à sequência de Fibonacci.")
else:
    print("O número não pertence à sequência de Fibonacci.")