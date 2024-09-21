#--------Operators--------

#Arithmatic operators
'''It contains nearly all operations that we can perform with the help of a calculator.

Symbols for such operators : 
print(5 + 7) #add
print(5 - 7) #substract
print(5 * 7) #multiply
print(5 / 7) #float division
print(5 ** 7) #gives the power of 5
print(5 // 7) #integer division
print(5 % 7) #gives remainder'''

#Assignment operators
'''The assignment operator is used to assign values to a variable. In some cases, we have to assign a variable’s value to another variable, in such cases the value of the right operand is assigned to the left operand. Such operators are : 

a = 25
a += 3 #a = a + 1
a -= 3 #a = a - 1
a *= 3 #a = a * 1
a /= 3 #a = a / 1
a **= 2 #a = a ** 1
a //= 4 #a = a // 1
a %= 6 #a = a % 1
#print(a)'''

#Comparison Operators
'''They are also known as relational operators. They compare the values on either side of the operator and decide the relation among them. Commonly used comparison operators : 

b = 3
c = 8
print(b == c)
print(b != c)
print(b <= c)
print(b >= c)
print(b < c)
print(b > c)'''

#Logical Operators
'''Logical operators perform logical AND, OR and NOT, operations. They are usually used in conditional statements to join multiple conditions. AND, OR and NOT keywords are used to perform logical operations. 

Example : 
print(57 and 8)
print(57 or 8)
print(57 not 8)'''

#Identity Operators
'''Identity operator checks if two operands share the same identity or not, which means that they share the same location in memory or different. “is” and “is not” are the keywords used for identity operands.

Examples : 
print(3 is 7)
print(7 is not 7)'''

#Membership Operators
'''Membership operand checks if the value or variable is a part of a sequence or not. The sequence could be string, list, tuple, etc. “in” and “not in” are keywords used for membership operands.

Examples : 
l = [2,4,8,56,32]
print(2 in l)
print(8 not in l)'''

#Bitwise Operators
'''Bitwise operands are used to perform bit by bit operation on binary numbers. First, we have to change the format of the number from decimal to binary and then compare them using AND, OR, XOR, NOT, etc.

# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print(0 & 2)
print(0 | 3)'''
