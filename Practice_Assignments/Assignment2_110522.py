# print("")
# print("not Finished This assignment 100%")
# print("")
# #          Assignment 2 - 11th May 2022

# # 1. Take input from the user and find the factorial (using while loop)
# # 2. Take input from the user and print the table of that value (3 * 1 = 3)
# # 3. Take input from the user and reverse the value (input = 789 , output = 987)
# # 4. Take input from the user and check whether it is an even number or an odd number
# # 5. Take the range from the user and print all the even numbers within that range
# #    Start  10
# #    End     20
# #-----------------------------------4---------------------------------------------------
# # 4. Take input from the user and check whether it is an even number or an odd number
# a = input("Enter a number : ")
# a= int(a)
# if(a%2 == 0):
#      print(a,"Number is Even number")
# else:
#      print(a,"is odd number")

# #-------------------------------------5-------------------------------------------------
# # 5. Take the range from the user and print all the even numbers within that range
# #   Start  10
# #   End     20

a=int(input("Start : "))
b= int(input("End : "))
c=0
lst=list(range(a,b+1))
print(lst)
for i in lst:
     if(i%2 == 0):
          print(i,"is Even number")
          c +=1

print(c)
# ------------------------------------------------------------------------------------------
     