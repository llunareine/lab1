# Solve Problems using loops

import math
# 1
# x = input()
# for i in range(1, int(x) + 1):
#     print(" Number is : " + str(i) + " and cube of the " + str(i) + " is " + str(int(math.pow(i,3))))

# 2
# mylist = [input() for i in range(0,5)]
# mylist.reverse()
# for i in mylist:
#     print(i)

# 3
# f = 1
# x = input()
# for i in range(1, int(x) + 1):
#     f = f * i
# print(f)


# 4
# f = 0
# x = input()
# for i in range(1, int(x) + 1):
#     f = f + i
# print(f)

# 5
# x = input()
# original = x
# mylist = []
# for i in range(len(str(x))):
#     mylist.append(str(int(x) % 10))
#     x = int(x) / 10
# if original == ''.join(mylist):
#     print("True Palindrome")
# else:
#     print("False Not palindrome")

# Solve Problems using nested loops
# 1
# x = input()
# for i in range(int(x),0, -1):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print("")

# 2
# x = input()
# for i in range(1, int(x) + 1):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print('')


# Solve problems using regular or lambda functions

# 1
# get_discount = lambda a, b : a - (a * b / 100)
# print(get_discount(int(input()),int(input())))

# 2
# def sum_numbers(n):
#    if int(n) <= 1:
#        return n
#    else:
#        return int(n) + sum_numbers(int(n)-1)
# num = input()
# if int(num) < 0:
#    print("enter a positive number")
# else:
#    print("sum_numbers", sum_numbers(num))

# 3
# def is_triplet(a,b,c):
#     if pow(a,2) + pow(b,2) == pow(c,2) or pow(a,2) + pow(c,2) == pow(b,2) or pow(b,2) + pow(c,2) == pow(a,2):
#         print("true")
#     else:
#         print("false")
# is_triplet(int(input()),int(input()),int(input()))
