def fibo (n):
    l = [0,1]
    for i in range(n):
        print(l[i], end=',')
        l.append(l[-1]+l[-2])
    print()

# Test cases
fibo(3)
fibo(5)
fibo(10)