# Handling multiple exceptions in Python
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of dividing {a} by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division performed successfully.")
    finally:
        print("Finished attempting to divide numbers.")    

# Test cases
# divide_numbers(10, 2)  # Valid case
divide_numbers(10, 0)  # ZeroDivisionError
# divide_numbers(10, "a")  # TypeError

# Handling multiple exceptions in Python with else and finally
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except IOError:
        print("Error: An I/O error occurred while reading the file.")
    else:
        print("File read successfully.")
    finally:
        print("Finished attempting to read the file.")




def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Qunatity must be in number")    

process_order("ginger",2)
process_order("masala","two")
process_order("masala",5)





