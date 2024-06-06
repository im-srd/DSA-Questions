def checkPrime(num):
    for i in range(2, int(num/2)):
        if num%i == 0:
            return False
    return True

# Test Cases 
print(checkPrime(42))
print(checkPrime(2))
print(checkPrime(0))
print(checkPrime(13))