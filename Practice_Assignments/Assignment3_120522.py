# # print("")
# # print("not Finished This assignment 100%")
# # print("")
# # Assignment 3 - 12th May 2022

# # 1. Take input from a user and check whether it is a palindrome or not
# #  (121 121  = palindrome)
# # 2. Take input from the user and check whether it is an even number or an odd number 
# # (% operator not allowed here)
# # 3. Take the range from the user and print all the prime numbers within that range
# # 4. Take input from the user and print the sum of those digits (Input = 456, Output = 14 )

# # 5. Logically print   
# #    a. *****
# #    b.   *
# #         *
# #         *
# #         *
# #         *

# #--------------------------------------------1----------------------------------------------
# 1. Take input from a user and check whether it is a palindrome or not
# #  (121 121  = palindrome)

# a=int(input("Enter number : "))
# c=a
# rev=0
# while a>0:
#      b=a%10
#      rev=rev*10+b
#      a=a//10
# if(c==rev):
#      print(c," is palindrome")
# else:
#      print(c,"is not palindrome")

# #--------------------------------------------2  VVImp----------------------------------------------
# # 2. Take input from the user and check whether it is an even number or an odd number 
# # (% operator not allowed here)

# #>>>>>> true or false method
# a = int(input("Enter a number : "))
# print(a&1)
# if((a&1) ==0):
#      print("even")
# else:
#      print("odd")

# #------------------------------------------------------------------------------------------
# 3. Take the range from the user and print all the prime numbers within that range

# x = int(input("Enter a number : "))
# y = int(input("Enter a number : "))
