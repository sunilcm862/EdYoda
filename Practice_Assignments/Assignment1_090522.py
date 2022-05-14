print("")
print("Finished This assignment 100%")
print("")
# # Assignment 1 - 9th May 2022

# # 1. Take input from the user and check whether it is a positive value or negative value
# # 2. Take input from the user and check whether that value is divisible by 5
# # 3. Take input from the user and check whether that value is divisible by 2 and 5
# # 4. Take 3 values from the user and find the greatest among all
# # 5. Take marks for English, Maths and Science subject and find the total value,
# #  percentage and grade on the bases of it

# #   1. Take input from the user and check whether it is a positive value or negative value
# a = int(input("Enter a number : "))
# if(a>0):
#      print(a,"is Positive number")
# elif(a<0):
#      print(a,"is Negative number")
# else:
#      print(a," is neither Negative Number nor Positive Number")
# #------------------------------------------------------------------------------------------

# # 2. Take input from the user and check whether that value is divisible by 5
# b = int(input("Enter a number : "))
# if(b % 5 == 0):
#      print(b,"is divisible by 5")
# else:
#      print(b,"is not divisible by 5")
# #------------------------------------------------------------------------------------------

# # 3. Take input from the user and check whether that value is divisible by 2 and 5
# c = int(input("Enter a number : "))
# if(c%2 == 0 and c%5 == 0):
#      print(c,"is divisible by 2 and 5")
# else:
#      print(c,"is not divisible by 2 and 5")
# #------------------------------------------------------------------------------------------

# # 4. Take 3 values from the user and find the greatest among all
# a_1 = int(input("Enter 1st number : "))
# b_1 = int(input("Enter 2nd number : "))
# c_1 = int(input("Enter 3rd number : "))
# if(a_1>=b_1 and a_1>=c_1):
#      large = a_1
# elif(b_1>=a_1 and b_1>=c_1):
#      large = b_1
# else:
#      large = c_1

# print("Largest number is ", large)
# #------------------------------------------------------------------------------------------

# 5. Take marks for English, Maths and Science subject and find the total value,
# percentage and grade on the bases of it  

# English = float(input("Enter English marks :"))
# Maths = float(input("Enter Maths marks :"))
# Science = float(input("Enter Science marks :"))

# total = English+Maths+Science
# print("Total Marks : ",total)

# if(English>100 or Maths > 100 or Science > 100 or English < 0 or Maths < 0 or Science < 0):
#      print("Entered marks are not valid")
# else:
#      percentage = total/3
#      print("Percentage : ",percentage,"%")
#      if(percentage>=85):
#           print("A grade")
#      elif(percentage>=60):
#           print("B grade")
#      elif(percentage>=35):
#           print("C frade")
#      else:
#           print("Fail")
# ------------------------------------------------------------------------------------------