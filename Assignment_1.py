#!/usr/bin/env python
# coding: utf-8

# Q1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# 
# ANS: 
#         VALUES: 'hello', -87.8, 6
#         EXPRESSIONS: -, +, /
# 

# 

# Q2. What is the difference between string and variable?
# 
# ANS: Variables is the property that can take up any value or data. Data values can be of different types 
#     such as integer, float or strings.
#     However, string is a type of data that can be stored in a variable. Strings usually represented within "" 
#     or '' and it composed of alphabets or numbers.
# 
#     For ex: X = "Chirag"
#     X is the variable which holds the string value "Chirag".

# 

# Q3. Describe three different data types.
# 
# ANS: 
#     1. Numeric Data Type: holds numeric values like
#     (a) int: contains signed integer values. (eg- 5,-245)
#     (b) float: holds floating numbers, accurate up to 15 decimal places. (eg - 2.45,-6.19)
#     (c) complex: holds complex numbers. (eg - 2+3j)
#         
#     2. String Data Type:
#         Strings is formed with the sequenced characters/alphabets or numbers enclosed within 
#         single('')/double("") quotes.
#         (eg - "This is a string.", "56")
#         
#     3. List Data Type:
#         List contains heterogenous data(such as string, int or float) values inside it within a larger bracket[],
#         separated by commas(,).
#         Usual notation of representing list is (list() or list =[]).
#         Lists are mutable objects means there values can be replaced with another value inside the list
#         at different location.
#         (eg - [5,23,46.5, "List", (34,6)])
#         

# 

# Q4. What is an expression made up of? What do all expressions do?
# 
# ANS: An expression is made up with the combination of operands and operators and it produces some value after
#     being interpreted by the python interpreter. Expressions are evaluated based on the precedence of operator.
#     eg. [x = 25+ 5.9 - 6] evaluated to 24.9 when we print the value of x.
#     
#     Different types of expression in python are:
#     1. Constant Expressions
#     2. Arithmetic Expressions
#     3. Integral Expressions
#     4. Floating Expressions
#     5. Relational Expressions
#     6. Logical Expressions
#     7. Bitwise Expressions
#     8. Combinational Expressions

# 

# Q5. This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?
# 
# ANS: A statement in Python is used for creating variables or for showing results while expressions in python
#     produces some value after being interpreted by the python interpreter.
#     A statement can be an expression while an expression can't be a statement.	
#     
#     Example Statement: x = 8
#                        print(x)   [output=8]
#     
#     Example Expression: x = 25 + 5.9 - 6    [output =24.9]
# 

# 

# Q6. After running the following code, what does the variable bacon contain?
#     bacon = 22
#     bacon + 1
# 
# ANS: The variable bacon contains 22 as the expression(bacon + 1) was not assigned to bacon variable.

# 

# Q7. What should the values of the following two terms be?
#     'spam' + 'spamspam'
#     'spam' * 3
# 
# ANS: The value of two terms would be the same('spamspamspam').

# 

# Q8. Why is eggs a valid variable name while 100 is invalid?
# 
# ANS: Variable name can't start with numbers but it can be started with any character/alphabet or underscore(_).
#     That's why 'eggs' is a valid variable name while 100 is invalid.

# 

# Q9. What three functions can be used to get the integer, floating-point number, or string
# version of a value?
# 
# ANS: For integer: int()
#      For floating-point number: float()
#      For string: str()
#      when value passed in these functions, they will return the respective data type values.

# 

# Q10. Why does this expression cause an error? How can you fix it?
#     'I have eaten'+ 99 + 'burritos.'
# 
# ANS: This expression gives an error 'an only concatenate str (not "int") to str', means string can't be
#     concatenate with the integer.
#     To rectify it, first we need to convert int(99) to string value by using str(99) and then after 
#     concatenation it will give the required expression.['I have eaten99burritos.']
#     
#     'I have eaten'+ str(99) + 'burritos.'
# 

# In[ ]:




