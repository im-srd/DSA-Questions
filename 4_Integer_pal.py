def intPal(num):
    return str(num)== (str(num))[::-1]

# Test Cases
print('Is 12321 a Palindrome ? ',intPal(12321))
print('Is 123421 a Palindrome ? ',intPal(123421))