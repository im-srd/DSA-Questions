def fact(num):
    if num == 0:
        return 1
    if num == 1:
        return num
    if num < 0:
        return '??NO ANSWER??'
    return num*fact(num-1)

# Test Cases
print('Factorial of 5 is',fact(5))
print('Factorial of -5 is',fact(-5))
print('Factorial of 0 is',fact(0))
