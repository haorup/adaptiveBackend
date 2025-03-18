"""
Python Debugging Question Bank (Expanded Version)
Contains various types of problems:
- Syntax Problems
- Loop Problems
- String Problems
- Mixed Problems
- Basic Problems
- Type Conversion Problems
- Operator Precedence Problems
- Control Flow Problems
- Exception Handling Problems
- File I/O Problems
- Function Problems
- List Problems
- Algorithm Problems
- Data Structure Problems

Includes three difficulty levels: Easy, Medium, Hard
Answers contain only the line of code that needs to be corrected
"""

# Question bank structured storage
question_bank = {
    0: [],  # Easy level questions
    1: [],  # Medium level questions
    2: []   # Hard level questions
}

# ====================== Syntax Problems ======================
# Easy level syntax problems
question_bank[0].extend([
    {
        "id": "syntax_easy1",
        "category": "Syntax",
        "text": """# Problem: Basic function definition and call syntax
def calculate(x, y)  # Error: Missing colon
    return x + y
    
result = calculate(5, 3)
print(result)

# Expected Output: 8""",
        "answer": """def calculate(x, y):""",
        "hint": "All function definitions require a colon",
        "knowledge_point": "Function definition syntax in Python"
    },
    {
        "id": "syntax_easy2",
        "category": "Syntax",
        "text": """# Problem: Basic if-statement syntax
number = 10
if number > 5  # Error: Missing colon
    print("Number is greater than 5")

# Expected Output: Number is greater than 5""",
        "answer": """if number > 5:""",
        "hint": "If statements require a colon",
        "knowledge_point": "Control flow syntax in Python"
    }
])

# Medium level syntax problems
question_bank[1].extend([
    {
        "id": "syntax_medium1",
        "category": "Syntax",
        "text": """# Problem: Function definition with default parameters
def process_data(data, options)  # Error: Missing colon
    if type(data) != list:  # Error: Non-Pythonic type checking
        raise TypeError("Data must be a list")
    return [x * 2 for x in data]

# Expected Output: TypeError: process_data() missing 1 required positional argument: 'options'""",
        "answer": """def process_data(data, options=None):""",
        "hint": "Function needs colon and proper parameter defaults",
        "knowledge_point": "Function definition and parameter handling"
    },
    {
        "id": "syntax_medium2",
        "category": "Syntax",
        "text": """# Problem: Try-except block syntax
def divide_numbers(a, b):
    try  # Error: Missing colon
        result = a / b
        return result
    except ZeroDivisionError  # Error: Missing colon
        print("Cannot divide by zero")
        return None

# Expected Output: Cannot divide by zero""",
        "answer": """    try:""",
        "hint": "Both try and except blocks need colons",
        "knowledge_point": "Exception handling syntax"
    }
])

# Hard level syntax problems
question_bank[2].extend([
    {
        "id": "syntax_hard1",
        "category": "Syntax",
        "text": """# Problem: Class definition with inheritance
class DataProcessor(BaseProcessor)  # Error 1: Missing colon
    def __init__(self, data)  # Error 2: Missing colon
        self.data = self.process(data)  # Error 3: Method called before definition

    def process():  # Error: Missing self parameter
        return sorted(self.data)

# Expected Output: Properly initialized DataProcessor object""",
        "answer": """class DataProcessor(BaseProcessor):""",
        "hint": "Check class and method definition syntax, method parameters",
        "knowledge_point": "Class definition and inheritance syntax"
    },
    {
        "id": "syntax_hard2",
        "category": "Syntax",
        "text": """# Problem: Decorator function syntax
def validate_input  # Error 1: Missing parentheses and colon
    def decorator(func)  # Error 2: Missing colon
        def wrapper(*args, **kwargs)  # Error 3: Missing colon
            if len(args) == 0:
                raise ValueError("No arguments provided")
            return func(*args, **kwargs)
    return decorator  # Error: Incorrect indentation""",
        "answer": """def validate_input():""",
        "hint": "Check function definitions and indentation",
        "knowledge_point": "Decorator syntax and nested functions"
    }
])

# ====================== Loop Problems ======================
# Easy level loop problems
question_bank[0].extend([
    {
        "id": "loop_easy1",
        "category": "Loop",
        "text": """# Problem: Basic for loop counter
def count_up_to(n):
    for i in range(n):  # Error: Wrong range
        print(i)
        
# Test Input: n = 5
# Expected Output: 1 2 3 4 5
# Actual Output: 0 1 2 3 4""",
        "answer": """for i in range(1, n + 1):""",
        "hint": "range(n) starts from 0, consider using range(1, n+1)",
        "knowledge_point": "Range function in for loops"
    },
    {
        "id": "loop_easy2",
        "category": "Loop",
        "text": """# Problem: Simple while loop
def print_even_numbers(n):
    i = 0
    while i <= n:  # Error: Condition causes printing of 0
        print(i)
        i += 2
        
# Test Input: n = 6
# Expected Output: 2 4 6
# Actual Output: 0 2 4 6""",
        "answer": """i = 2""",
        "hint": "Start from 2 instead of 0",
        "knowledge_point": "While loop initialization"
    },
    {
        "id": "loop_easy3",
        "category": "Loop",
        "text": """# Simple Loop Control (Easy)
counter = 1
total = 0
while counter < 5:    # Error
    total += counter
print(total)
# Expected output: 15
# Actual output: 10""",
        "answer": """while counter <= 5:""",
        "hint": "Change the loop condition to include 5",
        "knowledge_point": "While loop condition"
    }
])

# Medium level loop problems
question_bank[1].extend([
    {
        "id": "loop_medium1",
        "category": "Loop",
        "text": """# Problem: Nested loop with pattern
def print_triangle(n):
    for i in range(n):
        for j in range(i):  # Error: Wrong range for pattern
            print('*', end='')
        print()  # New line after each row

# Test Input: n = 4
# Expected Output:
# *
# **
# ***
# ****
# Actual Output:
# 
# *
# **
# ***""",
        "answer": """for j in range(i + 1):""",
        "hint": "Second range should be range(i+1)",
        "knowledge_point": "Nested loops and pattern printing"
    },
    {
        "id": "loop_medium2",
        "category": "Loop",
        "text": """# Problem: Loop with conditional break
def find_first_multiple(numbers, factor):
    found = None
    for num in numbers:
        if num % factor:  # Error: Wrong condition for finding multiple
            found = num
            break
            
    return found if found else "No multiple found"

# Test Input: numbers = [1, 3, 5, 6, 7, 8], factor = 3
# Expected Output: 6
# Actual Output: 1""",
        "answer": """if num % factor == 0:""",
        "hint": "Check remainder equals zero for multiples",
        "knowledge_point": "Break statement and condition checking"
    },
    {
        "id": "loop_medium3",
        "category": "Loop",
        "text": """# Counting Loop with Condition (Medium)
target = 10
count = 0
num = 1
while num < target:    # Error
    num += 2
    count += 1
print(count)
# Expected output: 5""",
        "answer": """while num <= target:""",
        "hint": "Fix the loop condition to include the target value",
        "knowledge_point": "While loop condition and counter logic"
    }
])

# Hard level loop problems
question_bank[2].extend([
    {
        "id": "loop_hard1",
        "category": "Loop",
        "text": """# Problem: Complex nested loops with matrix
def process_matrix(matrix):
    rows = len(matrix)
    result = []
    
    for i in range(rows):
        for j in range(rows):  # Error 1: Should use len(matrix[i])
            sum = 0
            for k in range(j):  # Error 2: Wrong range for summation
                sum += matrix[i][k]
        result.append(sum)  # Error 3: Wrong indentation
        
    return result

# Test Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Expected Output: [0, 1, 3, 0, 4, 9, 0, 7, 15]""",
        "answer": """for j in range(len(matrix[i])):""",
        "hint": "Check loop ranges and indentation",
        "knowledge_point": "Matrix traversal and nested loops"
    },
    {
        "id": "loop_hard2",
        "category": "Loop",
        "text": """# Problem: Loop with dynamic conditions
def find_sequence(numbers):
    length = len(numbers)
    current_seq = 1
    max_seq = 1
    
    i = 0
    while i < length - 1:  # Error 1: Wrong range
        while numbers[i+1] = numbers[i] + 1:  # Error 2: Assignment instead of comparison
            current_seq += 1
            i += 1
        if current_seq > max_seq
            max_seq = current_seq  # Error 3: Missing colon in if statement
        current_seq = 1
        
    return max_seq

# Test Input: numbers = [1, 2, 3, 5, 6, 7, 8, 10]
# Expected Output: 4 (longest sequence: 5,6,7,8)""",
        "answer": """while numbers[i+1] == numbers[i] + 1:""",
        "hint": "Check loop conditions and syntax",
        "knowledge_point": "Dynamic conditions and sequence tracking"
    },
    {
        "id": "loop_hard3",
        "category": "Loop",
        "text": """# Bubble Sort Implementation (Hard)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i): # Error
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr""",
        "answer": """for j in range(n-i-1):""",
        "hint": "Adjust loop range to avoid index out of bounds error",
        "knowledge_point": "Bubble sort algorithm implementation and list indexing"
    }
])

# ====================== String Problems ======================
# Easy level string problems
question_bank[0].extend([
    {
        "id": "string_easy1",
        "category": "String",
        "text": """# Problem: Basic string methods
text = "hello world"
print(text.Capital())  # Error: Incorrect method name

# Expected Output: Hello World""",
        "answer": """print(text.title())""",
        "hint": "Python string method is capitalize() or title()",
        "knowledge_point": "String capitalization methods"
    },
    {
        "id": "string_easy2",
        "category": "String",
        "text": """# Problem: String concatenation
first = "Hello"
last = "World"
message = first + " " + last  # Error: Missing space between strings

# Expected Output: Hello World""",
        "answer": """message = first + " " + last""",
        "hint": "Add spaces when concatenating strings",
        "knowledge_point": "String concatenation with spaces"
    }
])

# Medium level string problems
question_bank[1].extend([
    {
        "id": "string_medium1",
        "category": "String",
        "text": """# Problem: String formatting with multiple variables
def format_user_info(name, age, city):
    info = "Name: %s, Age: %d, City: %s" % name, age, city  # Error: Incorrect tuple formatting
    return info.capitalize

# Expected Output: Name: John, Age: 25, City: New York""",
        "answer": """info = f"Name: {name}, Age: {age}, City: {city}" """,
        "hint": "Use proper tuple parentheses for % formatting or f-strings",
        "knowledge_point": "String formatting with multiple variables"
    },
    {
        "id": "string_medium2",
        "category": "String",
        "text": """# Problem: String slicing and methods
def clean_and_extract(text):
    words = text.split()  # Error: No splitting character specified
    first_word = words[0].strip('.,!?')  # Error: Incomplete punctuation list
    return first_word.lower

# Expected Output: hello (for input text: "Hello, World!")""",
        "answer": """return first_word.lower()""",
        "hint": "Specify split character and remember () for method calls",
        "knowledge_point": "String splitting, stripping, and case conversion"
    }
])

# Hard level string problems
question_bank[2].extend([
    {
        "id": "string_hard1",
        "category": "String",
        "text": """# Problem: Complex string processing
def process_name_list(names):
    # Error 1: Incorrect join method usage
    formatted_names = " ".join(name.strip.capitalize for name in names)
    # Error 2: Wrong method chaining
    unique_names = set(formatted_names.split).sort()
    # Error 3: Incorrect list comprehension syntax
    return [name for name in unique_names if len(name) > 3]

# Test input: ["john ", " jane", "bob  ", "ALICE"]
# Expected Output: ['Alice', 'Jane', 'John']""",
        "answer": """formatted_names = [name.strip().capitalize() for name in names]""",
        "hint": "Check method calls and comprehension syntax",
        "knowledge_point": "String method chaining, list comprehension, and set operations"
    },
    {
        "id": "string_hard2",
        "category": "String",
        "text": """# Problem: Advanced string formatting and validation
def format_phone_number(number):
    # Error 1: Incorrect string method usage
    cleaned = number.removeall('-').removeall(' ')
    # Error 2: Wrong string slicing syntax
    area_code = cleaned[0:3:]
    # Error 3: Missing format specifiers
    return f"({area_code}) {cleaned[3:6]}-{cleaned[7:]}"

# Test input: "123-456-7890"
# Expected Output: (123) 456-7890""",
        "answer": """cleaned = number.replace('-', '').replace(' ', '')""",
        "hint": "Use replace method and correct string slicing",
        "knowledge_point": "String cleaning, slicing, and formatting"
    }
])

# ====================== Mixed Problems ======================
# Mixed problems
question_bank[1].extend([
    {
        "id": "mixed_medium1",
        "category": "Mixed",
        "text": """# Problem: Process student scores until passing score found
def find_first_passing(student_data):
    passing_student = None
    for name, scores in student_data:  # Error: Wrong dict iteration
        avg = sum(scores.values) / len(scores)  # Error: Missing parentheses
        if avg >= 60:
            passing_student = (name, avg)
            break
    return passing_student

# Test Input: 
students = {
    'John': {'math': 55, 'english': 65, 'science': 70},
    'Alice': {'math': 40, 'english': 50, 'science': 45},
    'Bob': {'math': 70, 'english': 75, 'science': 80}
}

# Expected Output: ('Bob', 75.0)""",
        "answer": """for name, scores in student_data.items():""",
        "hint": "Use .items() for dict iteration and proper method calls",
        "knowledge_point": "Dictionary iteration, tuple packing, break statement"
    },
    {
        "id": "mixed_medium2",
        "category": "Mixed",
        "text": """# Problem: Process sales records and update inventory
def update_inventory(inventory, sales_records):
    i = 0
    updated_items = {}
    
    while i < len(sales_records)  # Error 1: Missing colon
        product, quantity = sales_records[i]  # Tuple unpacking
        if product in inventory.keys  # Error 2: Missing parentheses
            updated_items[product] = inventory[product] - quantity
        i += 1  # Error 3: Increment in wrong position
    
    return updated_items

# Test Input:
inventory = {'apple': 100, 'banana': 150, 'orange': 200}
sales = [('apple', 20), ('banana', 30), ('orange', 25)]

# Expected Output: {'apple': 80, 'banana': 120, 'orange': 175}""",
        "answer": """while i < len(sales_records):""",
        "hint": "Check syntax and method calls",
        "knowledge_point": "While loop, tuple unpacking, dictionary operations"
    },
    {
        "id": "mixed_medium3",
        "category": "Mixed",
        "text": """# Problem: Find matching pairs in nested structure
def find_pairs(matrix, target):
    pairs = []
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i])  # Error 1: Missing colon
            if matrix[i][j] + matrix[i][j+1] == target  # Error 2: Missing colon
                pairs.append((matrix[i][j], matrix[i][j+1]))
                break  # Error 3: Break in wrong position
            j += 1
    return pairs

# Test Input:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3]
]
target = 10

# Expected Output: [(3, 7), (9, 1)]""",
        "answer": """while j < len(matrix[i]) - 1:""",
        "hint": "Check syntax and ensure proper indexing",
        "knowledge_point": "Nested loops, break statement, tuple creation"
    }
])

# ====================== Basic Problems ======================
# Basic problems
question_bank[0].extend([
    {
        "id": "basic_easy1",
        "category": "Basic",
        "text": """# String Operations (Easy)
message = "hello world"
print(message.upper) # Missing parentheses for method call
# Expected Output: HELLO WORLD""",
        "answer": """print(message.upper())""",
        "hint": "Method calls require parentheses",
        "knowledge_point": "String methods and function calls"
    },
    {
        "id": "basic_easy2",
        "category": "Basic",
        "text": """# Variable Name and Type Conversion (Medium)
name = "Alice"
age = 30
print("Name: " + name + ", Age: " + age)
# Expected Output: Name: Alice, Age: 30""",
        "answer": """print("Name: " + name + ", Age: " + str(age))""",
        "hint": "Convert number to string for concatenation",
        "knowledge_point": "Type conversion and string concatenation"
    },
    {
        "id": "basic_easy3",
        "category": "Basic",
        "text": """# Simple Input Processing (Easy)
age = input("Enter your age: ")
print("Age: " + age + 1)
# Expected Output: Age: 21 (assuming user enters 20)""",
        "answer": """age = int(input("Enter your age: "))""",
        "hint": "Convert input string to integer for arithmetic operations",
        "knowledge_point": "Type conversion with user input"
    }
])

# ====================== Type Conversion Problems ======================
# Type conversion problems
question_bank[1].extend([
    {
        "id": "typeconv_medium1",
        "category": "TypeConversion",
        "text": """# Data Type Conversion (Medium)
num_str = "123"
num_int = int(num_str)
print(num_str + 1)
# Expected Output: 124""",
        "answer": """print(int(num_str) + 1)""",
        "hint": "Convert string to integer before addition",
        "knowledge_point": "Type conversion and numeric operations"
    },
    {
        "id": "typeconv_medium2",
        "category": "TypeConversion",
        "text": """# Complex Type Conversion (Hard)
price_str = "25.99"
quantity = 3
tax_rate = "0.08"
total = price_str * quantity * (1 + tax_rate)
print("Total with tax: $" + total)
# Expected Output: Total with tax: $84.21""",
        "answer": """price_float = float(price_str)""",
        "hint": "Convert strings to appropriate numeric types",
        "knowledge_point": "Mixed type conversion and calculations"
    }
])

# ====================== Operator Precedence Problems ======================
# Operator precedence problems
question_bank[0].extend([
    {
        "id": "operator_easy1",
        "category": "OperatorPrecedence",
        "text": """# Simple Operator Precedence (Easy)
result = 5 + 2 * 3
print(result)
# Expected Output: 11""",
        "answer": """result = 5 + (2 * 3)""",
        "hint": "Multiplication has higher precedence than addition",
        "knowledge_point": "Basic operator precedence rules"
    }
])

question_bank[1].extend([
    {
        "id": "operator_medium1",
        "category": "OperatorPrecedence",
        "text": """# Multiple Operations (Medium)
x = 10
y = 5
z = 2
result = x + y * z ** 2
print(result)
# Expected Output: 30""",
        "answer": """result = x + (y * (z ** 2))""",
        "hint": "Exponentiation has highest precedence, followed by multiplication, then addition",
        "knowledge_point": "Complex operator precedence"
    }
])

question_bank[2].extend([
    {
        "id": "operator_hard1",
        "category": "OperatorPrecedence",
        "text": """# Complex Operations with Mixed Types (Hard)
a = "5"
b = 2
c = "3"
result = a + b * c
# Expected Output: 11 (as integer)""",
        "answer": """result = int(a) + (b * int(c))""",
        "hint": "Convert strings to integers and apply proper operator precedence",
        "knowledge_point": "Mixed type conversion and operator precedence"
    }
])

# ====================== Control Flow Problems ======================
# Control flow problems
question_bank[0].extend([
    {
        "id": "controlflow_easy1",
        "category": "ControlFlow",
        "text": """# Problem: Simple if-else condition
def check_score(score):
    if score >= 90:
        print("A")
    if score >= 80:  # Error: Using if instead of elif
        print("B")
    if score >= 70:
        print("C")
    else:
        print("F")

# Test Input: score = 85
# Expected Output: B
# Actual Output: B C""",
        "answer": """elif score >= 80:""",
        "hint": "Use elif for mutually exclusive conditions",
        "knowledge_point": "if-elif-else chain"
    },
    {
        "id": "controlflow_easy2",
        "category": "ControlFlow",
        "text": """# Problem: Basic for loop
def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2:  # Error: Wrong condition for even numbers
            total += num
    return total

# Test Input: [1, 2, 3, 4, 5, 6]
# Expected Output: 12 (2 + 4 + 6)
# Actual Output: 9 (1 + 3 + 5)""",
        "answer": """if num % 2 == 0:""",
        "hint": "Check the condition for even numbers (num % 2 == 0)",
        "knowledge_point": "Condition for even numbers"
    }
])

question_bank[1].extend([
    {
        "id": "controlflow_medium1",
        "category": "ControlFlow",
        "text": """# Problem: Nested loop with break
def find_first_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                break  # Error: Break only exits inner loop
        return numbers[i]  # Error: Return should be after duplicate found
    return None

# Test Input: [1, 2, 3, 2, 4, 1]
# Expected Output: 2
# Actual Output: 1""",
        "answer": """return numbers[i]  # Moving this line inside the inner loop after the if condition""",
        "hint": "Consider using a flag or different loop structure",
        "knowledge_point": "Break statement scope and return placement"
    },
    {
        "id": "controlflow_medium2",
        "category": "ControlFlow",
        "text": """# Problem: Try-except with multiple exceptions
def divide_and_convert(a, b):
    try:
        result = a / b
        return int(result)
    except:  # Error: Too broad exception clause
        return "Error"

# Test Input 1: a=5, b=0
# Test Input 2: a=5.5, b=2
# Expected Output 1: "Division by zero"
# Expected Output 2: 2""",
        "answer": """except ZeroDivisionError:
        return "Division by zero"
    except ValueError:
        return "Conversion error\"""",
        "hint": "Handle specific exceptions separately",
        "knowledge_point": "Exception handling specificity"
    }
])

question_bank[2].extend([
    {
        "id": "controlflow_hard1",
        "category": "ControlFlow",
        "text": """# Problem: Complex nested control flow
def process_data(data_list):
    results = []
    try:
        for item in data_list:
            if not isinstance(item, dict):  # Error 1: Wrong type check
                continue
            
            if item.get('status') = 'active':  # Error 2: Assignment instead of comparison
                if item.get('value', 0) > 100
                    results.append(item)  # Error 3: Missing colon
            
    except TypeError as e:
        return f"Error processing data: {str(e)}"
    
    return sorted(results, key=lambda x: x['value'])

# Test Input: [
#     {'status': 'active', 'value': 150},
#     {'status': 'inactive', 'value': 200},
#     {'status': 'active', 'value': 120},
#     'invalid_item'
# ]
# Expected Output: [
#     {'status': 'active', 'value': 120},
#     {'status': 'active', 'value': 150}
# ]""",
        "answer": """if item.get('status') == 'active':""",
        "hint": "Check syntax for conditions and type verification",
        "knowledge_point": "Nested conditions, error handling, and type checking"
    },
    {
        "id": "controlflow_hard2",
        "category": "ControlFlow",
        "text": """# Problem: State machine implementation
def process_workflow(tasks):
    current_state = 'START'
    processed = []
    
    while tasks:
        task = tasks.pop[0]  # Error 1: Wrong method syntax
        
        if current_state in 'START':  # Error 2: Incorrect string comparison
            next_state = task.get('type', 'INVALID')
        elif current_state == 'PROCESSING'
            if task['status'] = 'complete':  # Error 3: Assignment instead of comparison
                next_state = 'COMPLETED'
                processed.append(task)
            
        current_state = next_state
    
    return processed

# Test Input: [
#     {'type': 'PROCESSING', 'status': 'pending'},
#     {'type': 'PROCESSING', 'status': 'complete'},
#     {'type': 'COMPLETED', 'status': 'done'}
# ]
# Expected Output: [{'type': 'PROCESSING', 'status': 'complete'}]""",
        "answer": """task = tasks.pop(0)""",
        "hint": "Check list methods and comparison operators",
        "knowledge_point": "State machines, method calls, and condition checking"
    }
])

# ====================== Exception Handling Problems ======================
# Exception handling problems
question_bank[0].extend([
    {
        "id": "exception_easy1",
        "category": "Exception",
        "text": """# Problem: Basic exception handling
def divide_numbers(a, b):
    try:
        result = a / b
    except:  # Error: Too broad exception clause
        print("Error occurred")
    return result

# Test Input: a=10, b=0
# Expected Output: "Division by zero error\"""",
        "answer": """except ZeroDivisionError:
        print("Division by zero error")
        return None""",
        "hint": "Use specific exception type (ZeroDivisionError)",
        "knowledge_point": "Specific exception handling"
    },
    {
        "id": "exception_easy2",
        "category": "Exception",
        "text": """# Problem: Missing exception variable
def convert_to_int(text):
    try:
        number = int(text)
        return number
    except ValueError as:  # Error: Missing exception variable name
        print("Conversion failed")
        return None

# Test Input: "abc"
# Expected Output: "Conversion failed\"""",
        "answer": """except ValueError as e:""",
        "hint": "Provide a name for the exception variable",
        "knowledge_point": "Exception variable syntax"
    }
])

question_bank[1].extend([
    {
        "id": "exception_medium1",
        "category": "Exception",
        "text": """# Problem: Multiple exception handling
def process_data(data):
    try:
        if type(data) is not list:
            raise TypeError("Data must be a list")
        result = sum(data)
        return result
    except TypeError:
        print("Type error occurred")
    except:  # Error: Bare except after specific except
        print("Other error occurred")
    finally:
        print("Processing complete")

# Test Input: [1, "2", 3]
# Expected Output: TypeError and "Processing complete\"""",
        "answer": """except Exception as e:
        print("Other error occurred:", str(e))""",
        "hint": "Use specific exceptions before general ones",
        "knowledge_point": "Exception order and finally clause"
    },
    {
        "id": "exception_medium2",
        "category": "Exception",
        "text": """# Problem: Exception in context manager
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        raise  # Error: Bare raise without context
    finally:
        file.close()  # Error: File already closed by context manager

# Test Input: "nonexistent.txt"
# Expected Output: FileNotFoundError with proper context""",
        "answer": """except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find file: {filename}") from e""",
        "hint": "Remove unnecessary close and keep exception context",
        "knowledge_point": "Context managers and exception propagation"
    }
])

question_bank[2].extend([
    {
        "id": "exception_hard1",
        "category": "Exception",
        "text": """# Problem: Custom exception hierarchy
class DatabaseError(Exception)  # Error 1: Missing colon
    pass

class ConnectionError(DatabaseError):  
    def __init__(self, message)  # Error 2: Missing colon
        super().__init__(message)

def connect_database(connection_string):
    try:
        if not connection_string:
            raise ConnectionError
        # Simulate connection
        return True
    except ConnectionError as error  # Error 3: Missing colon
        raise DatabaseError("Connection failed") from error

# Test Input: ""
# Expected Output: DatabaseError with proper context""",
        "answer": """class DatabaseError(Exception):""",
        "hint": "Check syntax and exception chaining",
        "knowledge_point": "Custom exception hierarchy and exception chaining"
    },
    {
        "id": "exception_hard2",
        "category": "Exception",
        "text": """# Problem: Complex exception handling with cleanup
def process_files(filenames):
    opened_files = []
    try:
        for name in filenames
            file = open(name, 'r')  # Error 1: Missing colon
            opened_files.append(file)
    except FileNotFoundError as e
        print(f"File {name} not found")  # Error 2: Missing colon
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        for file in opened_files  # Error 3: Missing colon
            file.close()

# Test Input: ["file1.txt", "nonexistent.txt", "file2.txt"]
# Expected Output: Proper error handling and all opened files closed""",
        "answer": """for name in filenames:""",
        "hint": "Check syntax and ensure proper cleanup",
        "knowledge_point": "Resource management and cleanup"
    }
])

# ====================== File I/O Problems ======================
# File I/O problems
question_bank[0].extend([
    {
        "id": "fileio_easy1",
        "category": "FileIO",
        "text": """# Problem: Basic file reading
file = open('data.txt')  # Error: No file mode specified
content = file.read()
file.close()

# Test Case: Reading from 'data.txt'
# Expected Output: Content of file""",
        "answer": """file = open('data.txt', 'r')""",
        "hint": "Specify read mode 'r' when opening file",
        "knowledge_point": "File opening modes"
    },
    {
        "id": "fileio_easy2",
        "category": "FileIO",
        "text": """# Problem: File writing without closing
def write_message(filename, message):
    file = open(filename, 'w')
    file.write(message)
    # Error: Missing file close

# Test Case: write_message('output.txt', 'Hello')
# Expected Output: File with content 'Hello'""",
        "answer": """file.close()""",
        "hint": "Always close files after writing",
        "knowledge_point": "File resource management"
    }
])

question_bank[1].extend([
    {
        "id": "fileio_medium1",
        "category": "FileIO",
        "text": """# Problem: CSV file processing
def process_csv(filename):
    with open(filename, 'r') as file:
        header = file.readline()
        for line in file:
            fields = line.split(',')  # Error: Not handling newline characters
            data = {
                'name': fields[0],
                'age': fields[1],
                'city': fields[2]
            }
            process_record(data)

# Test Case: CSV file with 'name,age,city\\nJohn,25,NY\\n'
# Expected Output: Processed data without \\n""",
        "answer": """fields = line.strip().split(',')""",
        "hint": "Strip newline characters and handle field cleanup",
        "knowledge_point": "CSV line processing"
    },
    {
        "id": "fileio_medium2",
        "category": "FileIO",
        "text": """# Problem: File appending with error handling
def append_log(filename, message):
    try:
        file = open(filename, 'a')
        file.write(message)
    except IOError:
        print("Error writing to file")
    finally:
        file.close()  # Error: file might not be defined

# Test Case: append_log('log.txt', 'New message')
# Expected Output: Appended message or error handling""",
        "answer": """file = None
    try:""",
        "hint": "Initialize file variable before try block",
        "knowledge_point": "Exception handling with files"
    }
])

question_bank[2].extend([
    {
        "id": "fileio_hard1",
        "category": "FileIO",
        "text": """# Problem: Binary file processing
def process_binary_file(filename):
    try:
        with open(filename, 'rb') as file  # Error 1: Missing colon
            header = file.read(4)  # Error 2: Not converting bytes to int
            size = int.from_bytes(header)  # Error 3: Wrong bytes to int conversion
            
            data = file.read(size)
            return process_data(data)
    except IOError as e:
        print(f"Error processing file: {e}")
        return None

# Test Case: Binary file with 4-byte header indicating data size
# Expected Output: Processed binary data""",
        "answer": """with open(filename, 'rb') as file:""",
        "hint": "Check syntax and proper byte conversion methods",
        "knowledge_point": "Binary file handling and byte conversion"
    },
    {
        "id": "fileio_hard2",
        "category": "FileIO",
        "text": """# Problem: Multi-file processing with locks
import fcntl

def process_multiple_files(input_files, output_file):
    output = open(output_file, 'w')  # Error 1: No context management
    
    for file in input_files
        try:  # Error 2: Missing colon
            with open(file, 'r') as f:
                fcntl.flock(f, fcntl.LOCK_EX)
                content = f.readlines
                process_and_write(content, output)  # Error 3: Missing parentheses
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)

# Test Case: Multiple input files to be processed and combined
# Expected Output: Combined processed content in output file""",
        "answer": """with open(output_file, 'w') as output:""",
        "hint": "Use context managers and proper method calls",
        "knowledge_point": "File locking and resource management"
    }
])

# ====================== Function Problems ======================
# Function problems
question_bank[0].extend([
    {
        "id": "function_easy1",
        "category": "Function",
        "text": """# Problem: Basic function definition
def calculate_average(numbers)  # Error: Missing colon
    total = sum(numbers)
    return total/len(numbers)

# Test Input: [1, 2, 3, 4, 5]
# Expected Output: 3.0""",
        "answer": """def calculate_average(numbers):""",
        "hint": "Function definition requires a colon",
        "knowledge_point": "Function definition syntax"
    },
    {
        "id": "function_easy2",
        "category": "Function",
        "text": """# Problem: Function parameter usage
def greet(name, greeting)  # Error: No default value
    print(greeting + " " + name)

# Test Input: greet("John")
# Expected Output: "Hello John\"""",
        "answer": """def greet(name, greeting="Hello"):""",
        "hint": "Provide default value for greeting parameter",
        "knowledge_point": "Default parameters"
    }
])

question_bank[1].extend([
    {
        "id": "function_medium1",
        "category": "Function",
        "text": """# Problem: Function arguments handling
def process_user_data(user_id, name, email, age):
    data = {
        'id': user_id
        'name': name,
        'email': email,
        'age': age if type(age) == int else 0  # Error: Wrong type checking
    }
    return data

# Test Input: process_user_data(1, "John", "john@email.com", "25")
# Expected Output: {'id': 1, 'name': 'John', 'email': 'john@email.com', 'age': 25}""",
        "answer": """'id': user_id,""",
        "hint": "Use isinstance() for type checking and try converting string to int",
        "knowledge_point": "Type checking and data processing"
    },
    {
        "id": "function_medium2",
        "category": "Function",
        "text": """# Problem: Function with *args
def calculate_total(*args, tax_rate):  # Error: Non-default argument follows default argument
    subtotal = sum(args)
    return subtotal * (1 + tax_rate)

# Test Input: calculate_total(10, 20, 30, tax_rate=0.1)
# Expected Output: 66.0""",
        "answer": """def calculate_total(tax_rate, *args):""",
        "hint": "Put non-default parameters before *args",
        "knowledge_point": "Variable arguments and keyword arguments"
    }
])

question_bank[2].extend([
    {
        "id": "function_hard1",
        "category": "Function",
        "text": """# Problem: Function with multiple return values and error handling
def process_data(data_list):
    results = {}
    try:
        for item in data_list
            if not isinstance(item, (int, float))  # Error 1: Missing colon
                continue
            
            value = item * 2,5  # Error 2: Invalid number format
            results.append(value)  # Error 3: Using append on dictionary
            
        return results
    except TypeError as e:
        return None

# Test Input: [1, "2", 3.5, "text", 4]
# Expected Output: {1: 2.5, 3.5: 8.75, 4: 10.0}""",
        "answer": """for item in data_list:""",
        "hint": "Check syntax and dictionary operations",
        "knowledge_point": "Error handling and data processing"
    },
    {
        "id": "function_hard2",
        "category": "Function",
        "text": """# Problem: Decorator function implementation
def validate_input(func)  # Error 1: Missing colon
    def wrapper(*args, **kwargs)  # Error 2: Missing colon
        if len(args) = 0:  # Error 3: Assignment instead of comparison
            raise ValueError("No arguments provided")
        return func(*args, **kwargs)
    return wrapper

@validate_input
def process_numbers(numbers):
    return sum(numbers)

# Test Input: process_numbers([1, 2, 3])
# Expected Output: 6""",
        "answer": """def validate_input(func):""",
        "hint": "Check function definition syntax and comparison operators",
        "knowledge_point": "Decorator syntax and function wrapping"
    }
])

# ====================== List Problems ======================
# List problems
question_bank[0].extend([
    {
        "id": "list_easy1",
        "category": "List",
        "text": """# Problem: Basic list appending
numbers = [1, 2, 3, 4]
numbers.append([5, 6])  # Error: Appending list instead of elements

# Test Input: numbers = [1, 2, 3, 4]
# Expected Output: [1, 2, 3, 4, 5, 6]""",
        "answer": """numbers.extend([5, 6])""",
        "hint": "Use extend for adding multiple elements",
        "knowledge_point": "List methods append vs extend"
    },
    {
        "id": "list_easy2",
        "category": "List",
        "text": """# Problem: List slicing
fruits = ['apple', 'banana', 'cherry', 'date']
last_two = fruits[-2, -1]  # Error: Incorrect slice syntax

# Test Input: fruits = ['apple', 'banana', 'cherry', 'date']
# Expected Output: ['cherry', 'date']""",
        "answer": """last_two = fruits[-2:]""",
        "hint": "Use proper slice notation with colon",
        "knowledge_point": "List slicing syntax"
    }
])

question_bank[1].extend([
    {
        "id": "list_medium1",
        "category": "List",
        "text": """# Problem: List comprehension with filtering
def filter_process_numbers(numbers):
    # Error: Incorrect list comprehension logic
    results = [num // 2 if num % 2 == 0 for num in numbers]
    # Add only positive numbers after division
    positive_nums = [n for n in results if n > 0]
    return sorted(positive_nums)

# Test Input: [1, 2, 3, 4, 5, 6, 7, 8]
# Expected Output: [1, 2, 3, 4]""",
        "answer": """results = [num // 2 for num in numbers if num % 2 == 0]""",
        "hint": "Check the syntax for conditional in list comprehension",
        "knowledge_point": "List comprehension with conditional logic"
    },
    {
        "id": "list_medium2",
        "category": "List",
        "text": """# Problem: Nested list operations
def process_matrix(matrix):
    # Error: Incorrect nested list processing
    flattened = [num for row in matrix for num in row if num > 0]
    # Calculate row sums
    row_sums = [sum(row) for rows in matrix]
    return flattened, row_sums

# Test Input: [[1, -2, 3], [-4, 5, 6], [7, 8, -9]]
# Expected Output: 
# Flattened: [1, 3, 5, 6, 7, 8]
# Row sums: [2, 7, 6]""",
        "answer": """row_sums = [sum(row) for row in matrix]""",
        "hint": "Check variable names and comprehension syntax",
        "knowledge_point": "Nested list comprehension and operations"
    }
])

question_bank[2].extend([
    {
        "id": "list_hard1",
        "category": "List",
        "text": """# Problem: Complex list processing with multiple operations
def process_student_scores(student_data):
    # Error 1: Incorrect dictionary comprehension in list context
    scores = {student['name']: student['scores'] for student in student_data}
    # Error 2: Wrong average calculation
    averages = [sum(scores) / len(scores) for scores in scores.items()]
    # Error 3: Incorrect sorting syntax
    ranked_students = sorted(averages, key=lambda x: x[1], reversed=True)
    
    return ranked_students[:3]  # Return top 3 students

# Test Input: [
#     {'name': 'John', 'scores': [85, 90, 78]},
#     {'name': 'Alice', 'scores': [92, 88, 95]},
#     {'name': 'Bob', 'scores': [76, 85, 82]}
# ]
# Expected Output: [('Alice', 91.67), ('John', 84.33), ('Bob', 81.00)]""",
        "answer": """scores = {s['name']: sum(s['scores'])/len(s['scores']) for s in student_data}""",
        "hint": "Check comprehension syntax and sorting parameters",
        "knowledge_point": "Dictionary comprehension, list operations, and sorting"
    },
    {
        "id": "list_hard2",
        "category": "List",
        "text": """# Problem: Advanced list manipulation with custom sorting
def custom_sort_and_group(items):
    # Error 1: Incorrect grouping syntax
    groups = [item for item in items group by item.type]
    # Error 2: Wrong sorting method call
    sorted_groups = groups.sort(key=lambda x: len(x))
    # Error 3: Incorrect list flattening
    result = [item for group in sorted_groups for items in group]

    return result

# Test Input: [
#     {'type': 'A', 'value': 1}, 
#     {'type': 'B', 'value': 2},
#     {'type': 'A', 'value': 3},
#     {'type': 'B', 'value': 4}
# ]
# Expected Output: [
#     {'type': 'A', 'value': 1},
#     {'type': 'A', 'value': 3},
#     {'type': 'B', 'value': 2},
#     {'type': 'B', 'value': 4}
# ]""",
        "answer": """groups = {}
    for item in items:
        groups.setdefault(item['type'], []).append(item)""",
        "hint": "Use dictionary for grouping and proper sorting method",
        "knowledge_point": "List grouping, sorting, and flattening"
    }
])

# ====================== Algorithm Problems ======================
# Algorithm problems
question_bank[2].extend([
    {
        "id": "algorithm_hard1",
        "category": "Algorithm",
        "text": """# Binary Search Variations (Hard)
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] > x: # Error: Should be arr[mid] == x
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    return -1

# Test Input: arr = [1, 2, 3, 4, 5], x = 3
# Expected Output: 2 (index of x in arr)""",
        "answer": """if arr[mid] == x:""",
        "hint": "Check the equality condition in binary search",
        "knowledge_point": "Binary search algorithm implementation"
    },
    {
        "id": "algorithm_hard2",
        "category": "Algorithm",
        "text": """# Binary Search in Rotated Array (Hard)
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]: # Error
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Test Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Expected Output: 4""",
        "answer": """if nums[low] <= nums[mid]:""",
        "hint": "Check condition for determining which half is sorted",
        "knowledge_point": "Binary search in rotated array"
    },
    {
        "id": "algorithm_hard3",
        "category": "Algorithm",
        "text": """# Graph Traversal - BFS (Hard)
def bfs(graph, start):
    visited = set()
    queue = [] # Error: Should use deque()
    visited.add(start)
    queue.append(start)
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Test Input: Simple graph with vertices 0-4
# Expected Output: BFS traversal starting from vertex 0""",
        "answer": """from collections import deque
    queue = deque()""",
        "hint": "Use deque for efficient queue operations",
        "knowledge_point": "BFS graph traversal with efficient data structures"
    },
    {
        "id": "algorithm_hard4",
        "category": "Algorithm",
        "text": """# BFS Shortest Path (Hard)
def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append((start, 0))
    while queue:
        vertex, distance = queue.popleft()
        if vertex == end:
            return distance
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance)) # Error: Should be distance + 1
    return -1

# Test Input: Graph with shortest path of length 2
# Expected Output: 2""",
        "answer": """queue.append((neighbor, distance + 1))""",
        "hint": "Increment distance when adding neighbors to the queue",
        "knowledge_point": "BFS shortest path tracking"
    }
])

# ====================== Data Structure Problems ======================
# Data structure problems
question_bank[2].extend([
    {
        "id": "datastructure_hard1",
        "category": "DataStructure",
        "text": """# Binary Tree Level Order Traversal (Hard)
def level_order_traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.pop() # Error: Should be popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Test Input: Binary tree with 7 nodes
# Expected Output: Level order traversal result""",
        "answer": """node = queue.popleft()""",
        "hint": "Use popleft() for FIFO queue behavior in BFS",
        "knowledge_point": "Tree traversal with appropriate data structures"
    },
    {
        "id": "datastructure_hard2",
        "category": "DataStructure",
        "text": """# Linked List Reversal (Hard)
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Test Input: Linked list with nodes 1->2->3->4->5
# Expected Output: Reversed linked list 5->4->3->2->1""",
        "answer": """curr = next_node""",
        "hint": "Use the saved next_node variable",
        "knowledge_point": "Linked list traversal and reversal"
    },
    {
        "id": "datastructure_hard3",
        "category": "DataStructure",
        "text": """# Selection Sort Implementation (Hard)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] = arr[min_idx]  # Error: Incorrect swap
        arr[min_idx] = arr[i]
    return arr

# Test Input: [64, 25, 12, 22, 11]
# Expected Output: [11, 12, 22, 25, 64]""",
        "answer": """arr[i], arr[min_idx] = arr[min_idx], arr[i]""",
        "hint": "Use Python's tuple assignment for swapping values",
        "knowledge_point": "Array swapping and sorting algorithms"
    }
])

# Return the updated question bank
print("Python Debugging Question Bank completed, containing the following categories:")
categories = set(question["category"] for level in question_bank.values() for question in level)
for category in sorted(categories):
    print(f"- {category}")

print("\nTotal number of questions:", sum(len(level) for level in question_bank.values()))