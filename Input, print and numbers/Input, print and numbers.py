#1. How to read and write in Python 3
"""

print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # two stars are used for exponentiation (2 to the power of 16)
print(37 / 3)  # single forward slash is a division
print(37 // 3)  # double forward slash is an integer division
        # it returns only the quotient of the division (i.e. no remainder)
print(37 % 3)  # percent sign is a modulus operator
        # it gives the remainder of the left value divided by the right value

"""
#2. Sum of numbers and strings
"""
a = input("A: ")
b = input("B: ")
s = a + b
#a and b is string.
print("sum of this two string :",s)

c = int(input("C: "))
d = int(input("D: "))
s2 = c + d
#c and d is number now.
print("Sum of this two number is: ",s2)

"""
#3. Power of any number with Python
"""
print(2 ** 5)
"""
#4. Division
"""
#Normal division
print(37/3)
#Integer division
print(37 // 3)
#Remainder of division
print(37 % 3)
"""
#5. Print input
"""
print("Text that you type : ",input("Type smt. "))
print('Hi ' + input('What is your name? ')+ '!')
"""
#6. Number to String
"""
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')

"""

