def variable_example():
    example_variable = "This is an example variable."
    return example_variable
print(variable_example())


# def scope_test():
#     a = "local_outcome"
#     print(a)
# scope_test()

# def scope_test():
#     a = "local_outcome"
# scope_test()
# print(a)


def outer_func():
    x = 5   # variable in the outer function

    def inner_func():
        nonlocal x   # tells Python to use the x from outer_func
        x = 10       # modifies outer_func's variable
        print("Inside inner_func, x =", x)

    print("Before calling inner_func, x =", x)
    inner_func()
    print("After calling inner_func, x =", x)

outer_func()


# Helper function for divisibility check
def is_divisible(n, i):
    return n % i == 0

# Lambda for prime check
is_prime = lambda n: n > 1 and all(not is_divisible(n, i) for i in range(2, int(n**0.5) + 1))

# Test
print(is_prime(2))   # True
print(is_prime(9))   # False
print(is_prime(17))  # True
print(is_prime(20))  # False

#or one line
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Test
print(is_prime(2))   # True
print(is_prime(9))   # False
print(is_prime(17))  # True
print(is_prime(20))  # False


students = [
    {'name': 'Alice', 'score': 90},
    {'name': 'Bob', 'score': 75},
    {'name': 'Charlie', 'score': 85}
]

# 1. Sort by score (ascending)
sorted_students = sorted(students, key=lambda s: s['score'])

# 2. Filter score >= 80
filtered_students = filter(lambda s: s['score'] >= 80, sorted_students)

# 3. Map to just names
names = list(map(lambda s: s['name'], filtered_students))

print(names)
