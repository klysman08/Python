def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_for(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonacci_for_list = [0, 1]
        for i in range(2, n+1):
            fibonacci_for_list.append(fibonacci_for_list[i-1] + fibonacci_for_list[i-2])
        return fibonacci_for_list[n]

def fibonacci_while(n):
    t1=0
    t2=1
    count = 3
    while count <= n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        count += 1
    return t3

numero = int(input("Digite um inteiro n: "))
fibonacci_while(numero)

print(fibonacci(7),fibonacci_for(7),fibonacci_while(7))
