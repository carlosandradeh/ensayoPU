#Fibonacci recursivo

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Ejemplo: Generar los primeros 10 términos de la secuencia de Fibonacci
n = 10
fib_sequence = fibonacci(n)
print(fib_sequence)

