# An Armstrong number is a special kind of number in math. It's a number that equals the sum of its digits, each raised to a power equals to number of digits. For example, if you have a number like 153, it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153

def armstrong(num):
    sum = 0
    num_list = list(str(num)) # Converting num(int) -> num(str) -> num(list)
    for i in num_list:
        sum += pow(int(i),len(str(num))) # Converting i(str) -> i(int)
    return num==sum

# Test Cases
print('Is 153 an Armstrong Number ? ',armstrong(153))