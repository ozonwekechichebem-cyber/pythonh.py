# #a = 20
# #b = 40
# #result = a + b
# #print(result)
# #result = b - a
# #print("The result of the subtraction is:", result)
# #result = a * b
# #print("The result of the multiplication is:", result)
# #result = a / b
# #print("The result of the division is:", result)


# #lenght = 128 
# #width = 64
# #area = lenght * width
# #print("The area of the rectangle is:", area)


# #x = 5
# #y = 10
# #print("Before swapping x is ", x , "y is:", y)

# #y, x = x, y

# #print("After swapping x is:", x, "y is:", y)



# #number = 100

# #if number % 2 == 3:
#  #   print("True") 
# #else:
#  #   print("False")

# # salary = 50000
# # bonus = 0.1 ("10%")
# # new_salary = salary + (salary * bonus)
# # new_salary = (50000 + 5000)
# # print("The old salary is:", 50000)
# # print("The new salary is:", 55000)



# #name = "I/O spine"
# #address = "opposite secretariat junction"
# #firstName = "kizito"
# #lastName = "cassius"
# #data = "my name is" + " " + firstName + " " + lastName  + ", " +  "I am a student of" + " " + name + ", " + "which is located at" + " " + address + "."
# #print (data)
 



# # kizito_fruits = ('mango','watermelon','orange','avacado','cashew','cashew')
# # print(kizito_fruits.index('cashew'))
# # print(kizito_fruits.count('cashew'))

# # #dict of students
# # law_student = {"cythnia":25,"martha":19,"stephen":22,"ben":20}
# # print(law_student)
# # law_student.update({"ben":21})  #update the age of ben
# # print(law_student)
# # law_student["kizito"] = 23   #add a new student
# # print(law_student)

# # squad_list = [8,10,17,2,9]
# # squad_list[1] = 108
# # print(squad_list)
# #squad_tuples = (8,10,17,2,9)
# #squad_tuples[1] = 108
# #print(squad_tuples)
# #squad_list changed but squad_tuples did not change because tuples are immutable


# #dictionary of house items and their prices


# #this is kizito law school
# student_listname = input("this is kizito law school:")
# # Split into list of words
# words = student_listname.split()
# # Print result
# # print("Number of words:", len(words))
# # print("First word:", words[0])
# # print("Last word:", words[-1])

# # word = "banana"
# # word_tuple = tuple(word)

# # print("Tuple:", word_tuple)
# # print("Third element:", word_tuple[2])
# # if"a" in word_tuple:
# #  print("yes, 'a' in word_tuple")

# #  word = [20,30,40,50,60]
# #  #convert to tuple
# #  word_tuple = tuple(word)
# #  # Print results
# # print("Tuple:", word_tuple)
# # print("Maximum:", max(word_tuple))
# # print("Minimum:", min(word_tuple))

# # kizito = "expression"
# # kizito.count("kizito")
# # print(kizito.count)


# # students = ["John", "Mary", "Paul"]
# # scores = [85, 92, 78]
# # student_scores = dict(zip(students, scores))
# # print(student_scores)


# # products = {"apple": 100, "banana": 60, "orange": 80}

# # product_list = list(products.items())
# # print(product_list)


# # numbers = [10, 25, 5, 40, 15]

# # largest = max(numbers)
# # smallest = min(numbers)
# # average = sum(numbers) / len(numbers)

# # print("Largest number:", largest)
# # print("Smallest number:", smallest)
# # print("Average:",average)


# sentence = "kizito law school has all it take to be great"
# words = sentence.split()
# word_count = {}
# # Count word frequencies
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# # Find the most frequent word
# most_frequent = max(word_count, key=word_count.get)

# print("Most frequent word:", most_frequent)
# print("Frequency:", word_count[most_frequent])


# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "Diana": 90
# }
# # Find student with highest mark
# top_student = max(students, key=students.get)
# print("Top student:", top_student, "with mark", students[top_student])

# # Convert dictionary to list of tuples and sort by marks
# sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
# print("Sorted list of students by marks:", sorted_students)


# #lamba function for x = 2a/d - 3c
# result = lambda a, d, c: (2 * a) / d - 3 * c
# #let's say
# a, c, d = 6, 4, 3
# x = result(a, d, c)
# print(x)
# print(round(x))


def my_results(a, d, c):
    return (lambda a, d, c: ((2 * a) / d) - 3 * c)(a, d, c)
my_results(6,3,4)
print(my_results(6,3,4))

# weight_as_int = int(weight)
# height_as_float = float(height)
# bmi = weight_as_int / (height_as_float ** 2)
# # or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# #if the bill was $150.00, split between 5 people, with 12% tip.
# #Each person should pay (150.00 / 5) * 1.12 = 33.60
# #Round the result to 2 decimal places = 33.60
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))  
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")   


# print("welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.") 


# if "number" % 2 == 0:
#     print("This is an even number.")    
# else:
#     print("This is an odd number.")   


bmi = 22
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")



    #on every year that is evenly divisible by 4
      #except every year that is evenly divisible by 100
        #unless the year is also evenly divisible by 400   
year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")



if height >= 120:
    print("You can ride the rollercoaster!")    
    age = int(input("What is your age? "))
    if age < 12:
      print("Child tickets are $5.")
    elif age <= 18:
        print("Youth tickets are $7.")
    else:
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
#welcome to the pizza delivery service!
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")    
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#small pizza = $15
#medium pizza = $20
#large pizza = $25
#pepperoni for small pizza = +$2
#pepperoni for medium or large pizza = +$3  
#extra cheese for any size pizza = + $1 
if size == "S":
    bill = 15
elif size == "M":
        bill = 20
else:
        bill = 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3 
if extra_cheese == "Y":
            bill += 1
print(f"Your final bill is: ${bill}.") 


print("welcome to the love calculator")
name1 = input("kizito chebis \n")
name2 = input("mercy cynthia \n")

combined_string =name1 + name2
lower_case_string = combined_string.lower

t = lower_case_string.count("t")
r = lower_case_string.count("r")            
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")        
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e
love_score = str(true) + str(love)
print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.") 
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.") 
else:
    print(f"Your score is {love_score}.")   

welcome to treasure island you mission is to find the treasure.
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n')
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")     
else:
    print("You fell into a hole. Game Over.")   


import random
random_integer = random.randint(1, 10)
print(random_integer)

import random
random_float = random.random()
print(random_float)     

import random
random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:

    print("Tails")
    