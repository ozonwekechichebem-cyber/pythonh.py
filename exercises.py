# # #print first 10 natural numbers using while loop
# # i = 1
# # while i <= 10:
# #     print(i)
# #     i += 1

# #     #Write a Python code to print the following number pattern using a loop.

# # # 1 
# # # 1 2 
# # # 1 2 3 
# # # 1 2 3 4 
# # # 1 2 3 4 5
# # rows = 5
# # for i in range(1, rows + 1):
# #     for j in range(1, i + 1):
# #         print(j, end=' ')
# #     print()

# # print(list(range(0,6))) 


# # #Calculate sum of all numbers from 1 to 10
# # total = 0
# # for number in range(1, 11):
# #     total += number 
# # print("Sum:", total)    


# # #Print multiplication table of a given number
# # num = 2
# # for i in range(1, 11):
# #     product = num * i
# #     print(num, "x", i, "=", product)    


# # #Write a Python program to display only those numbers from a list that satisfy the following conditions

# # # The number must be divisible by five
# # # If the number is greater than 150, then skip it and move to the following number
# # # If the number is greater than 500, then stop the loop
# # numbers = [12, 75, 150, 180, 145, 525, 50]
# # for num in numbers:
# #     if num > 500:
# #         break                   
# #     elif num > 150:
# #         continue
# #     elif num % 5 == 0:
# #         print(num)


# # #Write a Python program to count the total number of digits in a number using a while loop.
# # #For example, the number is 75869, so the output should be 5.

# # num = 75869
# # count = 0   
# # while num != 0:
# #     num //= 10
# #     count += 1
# # print("Total number of digits:", count) 


# # #Write a Python program to print the reverse number pattern using a for loop.

# # # 5 4 3 2 1 
# # # 4 3 2 1 
# # # 3 2 1 
# # # 2 1 
# # # 1
# # rows = 5
# # for i in range(rows, 0, -1):
# #     for j in range(i, 0, -1):
# #         print(j, end=' ')
# #     print() 


# # #Print list in reverse order using a loop
# # list1 = [10, 20, 30, 40, 50]
# # for i in range(len(list1)-1, -1, -1):
# #     print(list1[i], end=' ')    
# #          #or
# # list1 = [10, 20, 30, 40, 50]    
# # #reverse list
# # new_list = reversed(list1)
# # for item in new_list:
# #     print(item, end=' ')


# # #Display numbers from -10 to -1 using for loop
# for num in range(-10, 0):
#     print(num, end=' ') 


# #Display a message “Done” after the successful execution of the for loop
# for i in range(5):
#     print(i)
# else:
#         print("Done!")


# #Print all prime numbers within a range
# # range
# start = 25
# end = 50
# for num in range(start, end + 1):
#     if num > 1:  # prime numbers are greater than 1
#         for i in range(2, int(num**0.5) + 1):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num, end=' ')

# #Display Fibonacci series up to 10 terms
# # first two numbers
# num1, num2 = 0, 1
# print("Fibonacci sequence:")
# # run the loop 10 times
# for i in range(10):
#      #print the next number of the series
#     print(num1, end=' ')
#     #add the last two numbers to get the next number
#     res = num1 + num2
#     #update values
#     num1 = num2
#     num2 = res


# #Write a Python program to use for loop to find the factorial of a given number.
# num = 5
# factorial = 1   
# for i in range(1, num + 1):
#     factorial *= i  
# print("Factorial of", num, "is", factorial)


# #Reverse a integer number
# num = 76542
# rev = 0
# while num > 0:
#     reminder = num % 10
#     rev = (rev * 10) + reminder
#     num = num // 10!
# print("Reversed Number:", rev)


# #Print elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90,100]
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         print(my_list[i], end=' ')  


# print(7 % 3)

# #current working directory
# pwd
# #list files in current directories
# ls
# git init
# ls -a


# #function that allows for input
# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how do you do {name}?")
#     print("Isn't the weather nice today")

# greet_with_name("kizito")

#function with more than 1 input
# def greet_with(name,location): 
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
# greet_with("kizito", "Ado")  

# #function with keyword arguments
# greet_with(name="Angela", location="Ado")

# test_h = 2
# test_w = 4
# coverage = 5
# nums_of_cans = (test_h * test_w)/ coverage
# print(nums_of_cans)
# print(round(nums_of_cans))


test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5
#paint_calc(heigth=test_h, width=test_w, coverage=5)
import math

def paint_calc(heigth,width,coverage):
    area = "height" * " width"
    nums_of_cans = math.ceil(area / coverage)
    print(f"you'll need {nums_of_cans} cans of paint.")


def prime_checker(number):
    is_prime = True
    for i in range(2,number)
      if number % i == 0:
         is_prime = False
      if is_prime:
         print("it's a prime number.")
      else:
         print("it's not a prime number.")     
  