# #lamba function for x = 2a/d - 3c
# result = lambda a, d, c: ((2 * a) / d) - 3 * c
# #let's say
# a, c, d = 6, 4, 3
# x = result(a, d, c)
# print(x)
# print(round(x))


# def my_results(a, d, c):
#     return (lambda a, d, c: ((2 * a) / d) - 3 * c)(a, d, c)
# my_results(6,3,4)
# print(my_results(6,3,4))

# def my_results():
#     return lambda a, d, c: ((2 * a) / d) - 3 * c

# calc = my_results()  # get the lambda
# print(calc(6, 3, 4)) 

def my_results(a, d, c):
    return (2 * a) / d - 3 * c

print(my_results(6, 3, 4))  
print(round(my_results(6, 3, 4)))  