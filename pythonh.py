# # # # # #word = "python"
# # # # # #print(word[1])
# # # # # #print(word[2:5])
# # # # # #print("t"in word)
# # # # # #print("python" in word)

# # # # # # text = "day by day"
# # # # # # print(text.upper())
# # # # # # print(text.lower())
# # # # # # print(text.replace("day","night"))
# # # # # # print(text.split(" text"))

# # # # # # x =20
# # # # # # print(type(x))
# # # # # # y = str(x)
# # # # # # print(type(y))
# # # # # # num = "25"
# # # # # # print(int(num)+ 10)

# # # # # # fruits = ["apple", "banana", "cherry"]
# # # # # # print(fruits[1])
# # # # # # fruits = ["apple", "banana", "cherry"]
# # # # # # fruits[1] = "orange"
# # # # # # print(fruits)  # ['apple', 'orange', 'cherry']
# # # # # # numbers = [1, 2, 3, 4, 5]
# # # # # # numbers.append(6)
# # # # # # print(numbers)  # [1, 2, 3, 4, 5, 6]
# # # # # # numbers.insert(2, 10)
# # # # # # print(numbers)  # [1, 2, 10, 3, 4, 5, 6]
# # # # # # numbers.remove(4)
# # # # # # print(numbers)  # [1, 2, 10, 3, 5, 6]
# # # # # # fruits = ["apple", "banana", "cherry"]
# # # # # # for fruit in fruits:
# # # # # #     print(fruit)
# # # # # # squares = [x**2 for x in range(10)]
# # # # # # print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# age = 36
# text = "My name is John, and I am {age}" 
# print(text)
# price = 59
# text = f"The price is {price} dollars"
# print(text)
# price = 49
# text = f"The price is {price:.2f} dollars"
# print(text)
# text = f"The price is {20 * 49} dollars"
# print(text)



# # # # # def myfunc(n):
# # # # #     return lambda a : a * n
# # # # # mydoubler = myfunc(2)
# # # # # print(mydoubler(11))


# # # # # number1 = 20
# # # # # number2 = 30
# # # # # product = number1 * number2
# # # # # if product <= 1000:
# # # # #     result = product
# # # # # else:
# # # # #     result = number1 + number2
# # # # # print("result:", result)

# # # # # #iterate through the first 10 numbers
# # # # # previous_number = 0
# # # # # for current_number in range(10):
# # # # #     sum_numbers = current_number + previous_number
# # # # # print("Current Number:",current_number, "Previous Number:",previous_number, "Sum:",sum_numbers)

# # # # # #Accept strings from user
# # # # # user_str = input("programming:")
# # # # # #display characters at even index positions
# # # # # print("characters at even index positions:")
# # # # # for i in range(0, len(user_str),2):
# # # # #     print(user_str[1], end="")

# # # # # #accept strings from user
# # # # # user_str = input("programming:")
# # # # # # Accept value of n
# # # # # n = int(input("3:"))
# # # # # #remove characters from 0 to n
# # # # # new_string = user_str[n:3]
# # # # # #display result
# # # # # print("new string:", new_string)


# # # # # x = [10,20,30,40,10]
# # # # # y = [75,65,35,75,30]

# # # # # def check_frist_last(num_list):
# # # # #     #check if list is not empty
# # # # #     if len(num_list) == 0:
# # # # #         return False
# # # # #     return num_list[0] == num_list[-1]
# # # # # #text cases
# # # # # print(check_frist_last(x)) #Output: True
# # # # # print(check_frist_last(y)) #Output: false

# # # # # #list of numbers
# # # # # numbers = [10,23,45,66,75,90,32,50]
# # # # # print("Numbers divisible by 5 are:")
# # # # # for num in numbers:
# # # # #     if num % 5 == 0:
# # # # #         print(num)

# # # # # #Create a virtual environment named 'myfirstproject':
# # # # #  C:\Users\Your Name> python -m venv myfirstproject
# # # # # #Activate the virtual environment:
# # # # # C:\Users\Your Name> myfirstproject\Scripts\activat
# # # # # #Install 'cowsay' in the virtual environment:
# # # # # (myfirstproject) C:\Users\Your Name> pip install cowsay
# # # # # #Execute test.py in the virtual environment:
# # # # # (myfirstproject) C:\Users\Your Name> python test.py
# # # # # #Deactivate the virtual environment:
# # # # # (myfirstproject) C:\Users\Your Name> deactivate
# # # # # #Normal command line interface:
# # # # # C:\Users\Your Name>
# # # # # #to excute outside the venv
# # # # # C:\Users\Your Name> python test.py
# # # # # #Delete myfirstproject from the command line interface:
# # # # # C:\Users\Your Name> rmdir /s /q myfirstproject


# # # # Total = 0
# # # # for number in range(1,101):
# # # #     Total += number
# # # # print("The sum is:", Total)

# # # # total2 = 0
# # # # for number in range(1,101):
# # # #     if number % 2 == 0:
# # # #         total2 += number
# # # # print("The sum of even numbers is:", total2)

# # # # for number in range(1,101):
# # # #     if number % 3 == 0 and number % 5 == 0:
# # # #      print("FizzBuzz")   
# # # #     elif number % 3 == 0:
# # # #         print("Fizz")
# # # #     elif number % 5 == 0:   
# # # #         print("Buzz")
# # # #     else:
# # # #             print(number)

# # #     #welcome to the password generator!
# # #     # how many letters would you like in your password?
# # #     # how many symbols would you like?
# # #     # how many numbers would you like?
# # # print("Here is your password:") 
# # #         # 4g$2jk8&P@1q

# # # import random
# # # letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'    
# # # numbers = '0123456789'
# # # symbols = '!@#$%^&*()_+'
# # # nr_letters = int(input("How many letters would you like in your password?\n"))
# # # nr_symbols = int(input("How many symbols would you like?\n"))
# # # nr_numbers = int(input("How many numbers would you like?\n"))

# # #    #eazy level
# # # password = ""
# # # #nr_letters = 4
# # # for char in range(1, nr_letters + 1):
# # #     #1 - 4  
# # #     ramdom_char = random.choice(letters)  
# # #     password += ramdom_char
    
# # # for char in range(1, nr_symbols + 1):
# # #     ramdom_char = random.choice(symbols)  
# # #     password += random.choice(symbols)  

# # # for char in range(1, nr_numbers + 1):
# # #     ramdom_char = random.choice(numbers)  
# # #     password += random.choice(numbers)

# # # print(password)

# # # #hard level
# # # password_list = []
# # # for char in range(1, nr_letters + 1):
# # #     password_list.append(random.choice(letters))        
# # # for char in range(1, nr_symbols + 1):
# # #     password_list.append(random.choice(symbols))    
# # # for char in range(1, nr_numbers + 1):
# # #     password_list.append(random.choice(numbers))    
# # # random.shuffle(password_list)
# # # print(password_list)    


# # # #with statement
# # # with open("demofile.txt", "r") as f:
# # #  print(f.read())

# # # #close the file
# # # f = open("demofile.txt", "r")
# # # print(f.readline())
# # # f.close()

# # # #read only first 5 characters
# # # with open("demofile.txt", "r") as f:
# # #   print(f.read(5))

# # # #read one line from the file
# # #   with open("demofile.txt") as f:
# # #     print(f.readline()) 

# # #  #read two lines from the file
# # #   with open("demofile.txt") as f:
# # #     print(f.readline())
# # #     print(f.readline())     

# # # #read all lines in a loop
# # # with open("demofile.txt") as f:
# # #   for x in f:
# # #     print(x)

# # # #append content to a file
# # #     with open("demofile.txt", "a") as f:
# # #         f.write("Now the file has more content!")

# # # #open and read the file after the appending:
# # # with open("demofile.txt") as f:
# # #   print(f.read())   

# # # #overwrite the content of a file
# # #   with open("demofile.txt", "w") as f:
# # #     f.write("Woops! I have deleted the content!")

# # # #open and read the file after the overwriting:
# # # with open("demofile.txt") as f:
# # #   print(f.read())


# # #   #This will create a new file:
# # # f = open("myfile.txt", "x")
# # # #If the file already exist, an error will be raised.


# # # #Remove the file "demofile.txt":
# # # import os
# # # os.remove("demofile.txt")


# # # #Check if file exists, then delete it:
# # # import os
# # # if os.path.exists("demofile.txt"):
# # #   os.remove("demofile.txt")
# # # else:
# # #   print("The file does not exist")


# # #   #Remove the folder "myfolder":  delete folder
# # # import os
# # # os.rmdir("myfolder")



# # # To install numpy, run the following command in your terminal:
# # # pip install numpy
# # import numpy as np  
# # arr = np.array([1, 2, 3, 4, 5])
# # print(arr)
# # print(type(arr))  
# # print(arr.shape)
# # print(arr[0]) 
# # print(arr[1:4])
# # print(arr[::2])   
# # print(arr.dtype)
# # print(arr.ndim)   
# # print(arr.size)
# # print(arr.itemsize)
# # print(arr.nbytes)  

# # # Create a 2D array (matrix)  
# # matrix = np.array([[1, 2, 3], [4, 5, 6]])
# # print(matrix) 


# # #Check how many dimensions the arrays have:
# # import numpy as np
# # a = np.array(42)
# # b = np.array([1, 2, 3, 4, 5])
# # c = np.array([[1, 2, 3], [4, 5, 6]])
# # d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# # print(a.ndim)
# # print(b.ndim)
# # print(c.ndim)
# # print(d.ndim)

# # rows = 5
# # for i in range(1 + rows + 1):
# #     for j in range(1 + i + 1):
# #         print(j, end=' ')

# # Joining a list of strings
# words = ["Hello", "World", "Python"]
# sentence = " ".join(words)
# print(sentence)  # Output: Hello World Python

# # With different separators
# path = "/".join(["usr", "local", "bin"])
# print(path)  # Output: usr/local/bin



# word_list = ["Banana", "Apple", "Orange"]
# import random
# chosen_word = random.choice(word_list)
# #let random.choice be "guess"
# guess = input("guess a fruit:").lower
# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")

# #if the empty list is called display
# #  for each letter in the chosen word add a "_" to 'display'
# # if the letter  in the chosen word is "apple" display should be ["_","_","_","_","_"] represinting each letter in guess
# #       

# strings = ["my", "world", "apple", "pear"]
# lengths = map(len, strings)
# print(list(lengths))  # Output: [2, 5, 5, 4]

# strings = ["my", "world", "apple", "pear"]
# lengths = map(lambda x: x + "s", strings)
# print(list(lengths))  # Output: [2, 5, 5, 4]

# strings = ["my", "world", "apple", "pear"]
# def add_s(strings):  
#     return strings + "s"
# lengths = map(add_s, strings)
# print(list(lengths))  # Output: [2, 5, 5, 4]

# def longer_than_4(strings):
#     return len(strings) > 4
# strings = ["my", "world", "apple", "pear"]
# filtered = filter(longer_than_4, strings)
# print(list(filtered))  # Output: ['world', 'apple']

# #list comprehension
# nums = [54, 23, 66, 12, 34, 89]
# evens = []
# for nums in nums:
#     if nums % 2 == 0:
#         evens.append(nums)
# print(evens)  # Output: [54, 66, 12, 34]
# #or
# nums = [54, 23, 66, 12, 34, 89]
# evens = [num for num in nums if num % 2 == 0]   
# print(evens)  # Output: [54, 66, 12, 34]


# numbers: list[int] = [1, 2, 3, 4, 5]
# squared: list[int] = [pow(numbers,2)  for number in numbers]
# print(squared)  # Output: [1, 4, 9, 16, 25]

# numbers: list[int] = [1, 2, 3, 4, 5]
# squared: list[int] = [pow(numbers,2)  for number in numbers if number > 2]
# print(squared)  # Output: [9, 16, 25]  

# #generator comprehension
# from typing import Generator
# data: range = range(10_000)
# squared_gen: Generator[int, None, None] = (pow(numbers,2) for x in data)
# print(squared_gen)  # Output: <generator object <genexpr> at 0 
# print(next(squared_gen))  # Output: 0
# print(next(squared_gen))  # Output: 1               
# print(next(squared_gen))  # Output: 4
# print(next(squared_gen))  # Output: 9

# #set comprehension
# values: list[int] = [1, 2, 3, 2, 4, 5, 1, 3]
# filtered_set: set[int] = {x for x in values if x % 2 == 0}
# print(filtered_set)  # Output: {2, 4}

# #dictionary comprehension
# data: list[tuple[str, int]] = [("apple", 1), ("banana", 2), ("orange", 3)]
# fruit_dict: dict[str, int] = {key: value for key, value in data}
# print(fruit_dict)  # Output: {'apple': 1, 'banana': 2, 'orange': 3}