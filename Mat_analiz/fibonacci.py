def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))

print('-----------------------------------------------------------------------------------')

n = 30
counter1 = 0
counter2 = 1
for i in range(n):
    counter2 = counter1 + counter2
    counter1 = counter2 - counter1
    print(counter1, end=' ')


