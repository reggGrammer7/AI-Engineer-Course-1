# Pure function example(RECOMMENDED)
def pure_chai(cups):
    return cups * 10



# Impure function example(NOT RECOMMENDED)
total_chai = 0
def impure_chai(cups):
    global total_chai
    total_chai += cups * 10
    return total_chai


# Recursive function example
def pour_chai(n):
    print(n)
    if n ==0:
        return "No chai to pour"
    return pour_chai(n-1)
print(pour_chai(3))

# Lambda function example
add = lambda x, y: x + y
print(add(5, 3))

# Using lambda with filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using lambda with map
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)







