"""
Python Debugging Question Bank (Expanded and Enhanced Version)
This file contains a debugging question bank for Python.
Each question now includes three levels of hints:
  - Level 1 (Minimal Prompt): General guidance without revealing the solution.
  - Level 2 (Guided Questioning): Socratic-style hint prompting critical thinking.
  - Level 3 (Detailed Explanation): A conceptual breakdown of the error type.
Questions are organized into 3 difficulty levels: Easy (level 0), Medium (level 1), and Hard (level 2).
Categories include: Syntax, Loop, String, Mixed, Basic, TypeConversion, OperatorPrecedence, ControlFlow, Exception, FileIO, Function, List, Algorithm, DataStructure.
"""

question_bank = {
    0: [],  # Easy level questions
    1: [],  # Medium level questions
    2: []   # Hard level questions
}

# ====================== Syntax Problems ======================

# --- Easy level syntax problems ---
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
        "hints": {
            "level1": "Review the function definition syntax.",
            "level2": "What punctuation does Python require at the end of a function header?",
            "level3": "In Python, every function definition must end with a colon to indicate the start of the function body. Omitting the colon results in a SyntaxError."
        },
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
        "hints": {
            "level1": "Check your if statement syntax.",
            "level2": "What symbol is needed after the if condition in Python?",
            "level3": "In Python, an if statement must end with a colon, which signals the beginning of the block of code to execute if the condition is true."
        },
        "knowledge_point": "Control flow syntax in Python"
    }
])

# --- Medium level syntax problems ---
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
        "hints": {
            "level1": "Review function definition syntax.",
            "level2": "How can you provide a default value for a parameter and ensure correct punctuation in a function header?",
            "level3": "In Python, when defining a function with optional parameters, you must include a colon at the end and use default values (e.g. options=None) so that the function is defined correctly."
        },
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
        "hints": {
            "level1": "Check the try and except syntax.",
            "level2": "What do both try and except statements require to properly define their blocks?",
            "level3": "Both try and except statements in Python require a colon at the end. Missing colons in these blocks will result in syntax errors."
        },
        "knowledge_point": "Exception handling syntax"
    }
])

# --- Hard level syntax problems ---
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
        "hints": {
            "level1": "Review class and method syntax.",
            "level2": "What are the required syntactical elements for a class definition and its methods?",
            "level3": "A class definition in Python must end with a colon, and methods inside a class must have 'self' as the first parameter. Also, method calls must occur after the method is defined."
        },
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
        "hints": {
            "level1": "Check decorator syntax.",
            "level2": "What punctuation is required when defining a function that acts as a decorator?",
            "level3": "When writing decorator functions, each function definition must include parentheses (if applicable) and end with a colon. Proper indentation is also critical to define nested functions correctly."
        },
        "knowledge_point": "Decorator syntax and nested functions"
    }
])

# ====================== Loop Problems ======================

# --- Easy level loop problems ---
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
        "hints": {
            "level1": "Examine the range function usage.",
            "level2": "What range should be used if you need a counter starting at 1 up to n?",
            "level3": "The range() function by default starts at 0, so to include the number n, use range(1, n+1) to generate numbers from 1 to n."
        },
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
        "hints": {
            "level1": "Review the while loop initialization.",
            "level2": "If you do not want to include 0, what should be the starting value of your counter?",
            "level3": "In this case, initializing the counter to 2 prevents 0 from being printed. Adjust the initialization accordingly to meet the expected output."
        },
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
        "hints": {
            "level1": "Examine the while loop condition.",
            "level2": "How can you modify the condition to ensure the loop includes the value 5?",
            "level3": "Using 'while counter <= 5' ensures that the loop includes the case when counter equals 5, meeting the expected output."
        },
        "knowledge_point": "While loop condition"
    }
])

# --- Medium level loop problems ---
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
        "hints": {
            "level1": "Review the inner loop's range.",
            "level2": "What adjustment to the range function ensures the correct number of stars are printed per row?",
            "level3": "By using range(i+1), you correctly generate the number of iterations to print an increasing number of stars for each row in the triangle pattern."
        },
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
        "hints": {
            "level1": "Check the condition for identifying multiples.",
            "level2": "What should be the correct condition to check if a number is a multiple of the factor?",
            "level3": "The condition should use 'if num % factor == 0:' to verify that the remainder is zero, confirming that the number is a multiple of the factor."
        },
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
        "hints": {
            "level1": "Review the loop condition logic.",
            "level2": "How can you modify the while loop to ensure that the target value is considered?",
            "level3": "Using 'while num <= target:' includes the case when num equals the target, ensuring the loop performs as expected."
        },
        "knowledge_point": "While loop condition and counter logic"
    }
])

# --- Hard level loop problems ---
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
        "hints": {
            "level1": "Review the nested loop indices.",
            "level2": "What change in the range of the inner loop will correctly iterate through each element in the matrix row?",
            "level3": "Instead of using range(rows), the inner loop should iterate with range(len(matrix[i])) to correctly access each element in the current row. Also, indentation must be adjusted for summation accumulation."
        },
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
        "hints": {
            "level1": "Examine the while loop condition and comparison operator.",
            "level2": "What correction is needed to properly compare adjacent elements in the list?",
            "level3": "The while loop should use '==' for comparison instead of '=', which is used for assignment. This ensures the condition correctly checks if the next number is exactly one greater than the current."
        },
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
        "hints": {
            "level1": "Check the loop boundary in the bubble sort algorithm.",
            "level2": "What adjustment to the range function can prevent accessing an out-of-range index?",
            "level3": "By using 'for j in range(n-i-1):', you ensure that the inner loop does not access an index that is out of range during the swap process."
        },
        "knowledge_point": "Bubble sort algorithm implementation and list indexing"
    }
])

# ====================== String Problems ======================

# --- Easy level string problems ---
question_bank[0].extend([
    {
        "id": "string_easy1",
        "category": "String",
        "text": """# Problem: Basic string methods
text = "hello world"
print(text.Capital())  # Error: Incorrect method name

# Expected Output: Hello World""",
        "answer": """print(text.title())""",
        "hints": {
            "level1": "Review string capitalization methods.",
            "level2": "What is the correct method to capitalize each word in a string?",
            "level3": "In Python, 'title()' converts the first character of each word to uppercase, providing the desired output. Alternatively, 'capitalize()' can be used for a single word."
        },
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
        "hints": {
            "level1": "Check string concatenation.",
            "level2": "How can you ensure that a space is inserted between two concatenated strings?",
            "level3": "Using 'first + \" \" + last' correctly inserts a space between the two strings, yielding the expected result."
        },
        "knowledge_point": "String concatenation with spaces"
    }
])

# --- Medium level string problems ---
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
        "hints": {
            "level1": "Review string formatting.",
            "level2": "How can you correctly format multiple variables into a string?",
            "level3": "Using f-strings or properly parenthesized tuple formatting ensures that each variable is inserted into the string at the correct position."
        },
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
        "hints": {
            "level1": "Review string slicing and method calls.",
            "level2": "Why is it important to include parentheses when calling a method in Python?",
            "level3": "Parentheses are necessary to execute a method call. Omitting them means referencing the method object itself, not its returned value. Also, specifying the split character properly ensures correct string manipulation."
        },
        "knowledge_point": "String splitting, stripping, and case conversion"
    }
])

# --- Hard level string problems ---
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
        "hints": {
            "level1": "Examine the string processing steps.",
            "level2": "How can list comprehension be used to correctly process and format each name in the list?",
            "level3": "Using a list comprehension with method chaining allows you to strip whitespace and capitalize each name correctly. This ensures that all names are formatted consistently."
        },
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
        "hints": {
            "level1": "Review string cleaning methods.",
            "level2": "What string methods can be used to remove unwanted characters before slicing?",
            "level3": "The 'replace()' method can remove unwanted characters such as '-' and spaces. Once cleaned, proper slicing can extract the correct parts of the string for formatting."
        },
        "knowledge_point": "String cleaning, slicing, and formatting"
    }
])

# ====================== Mixed Problems ======================

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
        "hints": {
            "level1": "Review dictionary iteration methods.",
            "level2": "What method allows you to iterate over key-value pairs in a dictionary?",
            "level3": "Using .items() in a dictionary iteration lets you access both keys and values, ensuring correct processing of each student's scores."
        },
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
        "hints": {
            "level1": "Examine the while loop syntax.",
            "level2": "What punctuation is needed to correctly define a while loop?",
            "level3": "A while loop in Python must end with a colon. Also, proper method calls (like inventory.keys()) require parentheses."
        },
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
        "hints": {
            "level1": "Review nested loop conditions.",
            "level2": "How should the while loop condition be adjusted to prevent index errors?",
            "level3": "Using 'while j < len(matrix[i]) - 1:' ensures that you do not access an index out of range when checking pairs of elements."
        },
        "knowledge_point": "Nested loops, break statement, tuple creation"
    }
])

# ====================== Basic Problems ======================

question_bank[0].extend([
    {
        "id": "basic_easy1",
        "category": "Basic",
        "text": """# String Operations (Easy)
message = "hello world"
print(message.upper) # Missing parentheses for method call
# Expected Output: HELLO WORLD""",
        "answer": """print(message.upper())""",
        "hints": {
            "level1": "Review function/method calls.",
            "level2": "What is necessary when calling a function or method in Python?",
            "level3": "In Python, you must include parentheses when calling a function or method to execute it, otherwise you reference the function object itself."
        },
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
        "hints": {
            "level1": "Review type conversion for string concatenation.",
            "level2": "How can you convert a number to a string to allow concatenation with other strings?",
            "level3": "By using the str() function, you convert a number to a string, ensuring that concatenation is performed correctly."
        },
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
        "hints": {
            "level1": "Check type conversion for user input.",
            "level2": "Why is it important to convert input from input() to an integer when performing arithmetic?",
            "level3": "input() returns a string, so to perform arithmetic operations, you must convert it to an integer using int()."
        },
        "knowledge_point": "Type conversion with user input"
    }
])

# ====================== Type Conversion Problems ======================

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
        "hints": {
            "level1": "Review type conversion.",
            "level2": "How can you convert a string containing digits to an integer?",
            "level3": "Using int() converts a string of digits into an integer, allowing arithmetic operations like addition to be performed correctly."
        },
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
        "hints": {
            "level1": "Review numeric type conversion.",
            "level2": "What conversions are needed to correctly perform arithmetic on strings representing numbers?",
            "level3": "Convert price and tax rate from strings to float to ensure accurate multiplication and addition during calculation."
        },
        "knowledge_point": "Mixed type conversion and calculations"
    }
])

# ====================== Operator Precedence Problems ======================

# --- Easy level operator precedence problems ---
question_bank[0].extend([
    {
        "id": "operator_easy1",
        "category": "OperatorPrecedence",
        "text": """# Simple Operator Precedence (Easy)
result = 5 + 2 * 3
print(result)
# Expected Output: 11""",
        "answer": """result = 5 + (2 * 3)""",
        "hints": {
            "level1": "Check operator precedence.",
            "level2": "What is the natural order of operations in Python for addition and multiplication?",
            "level3": "Multiplication is performed before addition in Python's operator precedence rules. Using parentheses can clarify the intended order of operations."
        },
        "knowledge_point": "Basic operator precedence rules"
    }
])

# --- Medium level operator precedence problems ---
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
        "hints": {
            "level1": "Review operator precedence.",
            "level2": "How are exponentiation, multiplication, and addition prioritized in Python?",
            "level3": "Python evaluates exponentiation (**) first, then multiplication, and finally addition. Parentheses help enforce the intended order of operations."
        },
        "knowledge_point": "Complex operator precedence"
    }
])

# --- Hard level operator precedence problems ---
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
        "hints": {
            "level1": "Check mixed type operations.",
            "level2": "How can you ensure that string values are correctly used in arithmetic expressions?",
            "level3": "Convert the string values to integers before performing arithmetic operations to ensure proper operator precedence is applied."
        },
        "knowledge_point": "Mixed type conversion and operator precedence"
    }
])

# ====================== Control Flow Problems ======================

# --- Easy level control flow problems ---
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
        "hints": {
            "level1": "Review if-elif-else structure.",
            "level2": "What change is needed to prevent multiple conditions from triggering in a chain of if statements?",
            "level3": "Using 'elif' ensures that once a condition is met, the remaining conditions are skipped, thereby preventing multiple outputs."
        },
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
        "hints": {
            "level1": "Review modulus operation for even numbers.",
            "level2": "How do you correctly check if a number is even using the modulus operator?",
            "level3": "The condition 'num % 2 == 0' evaluates to True when a number is even, ensuring that only even numbers are summed."
        },
        "knowledge_point": "Condition for even numbers"
    }
])

# --- Medium level control flow problems ---
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
        "hints": {
            "level1": "Review loop structure and placement of return.",
            "level2": "How does the placement of the return statement affect the outcome of the nested loops?",
            "level3": "The return statement should be placed only after a duplicate is found within the inner loop, ensuring the function does not exit prematurely."
        },
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
        "hints": {
            "level1": "Review exception handling.",
            "level2": "Why should exceptions be handled specifically rather than using a bare except?",
            "level3": "Handling specific exceptions, such as ZeroDivisionError and ValueError, provides more precise error handling and prevents unintended error catching."
        },
        "knowledge_point": "Exception handling specificity"
    }
])

# --- Hard level control flow problems ---
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
        "hints": {
            "level1": "Review nested condition syntax.",
            "level2": "What corrections are necessary for proper condition checking in nested structures?",
            "level3": "The error stems from using assignment '=' instead of comparison '==' in conditionals and missing colons after if statements. Correct syntax is essential for proper flow control."
        },
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
        "hints": {
            "level1": "Review list method usage.",
            "level2": "How can you correctly call a method to pop the first element of a list?",
            "level3": "Using 'pop(0)' instead of pop[0] is necessary to properly remove and return the first element from the list. Also, ensure comparisons use '==' rather than '='."
        },
        "knowledge_point": "State machines, method calls, and condition checking"
    }
])

# ====================== Exception Handling Problems ======================

# --- Easy level exception handling problems ---
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
        "hints": {
            "level1": "Review exception clauses.",
            "level2": "What is the advantage of specifying the exception type rather than using a bare except?",
            "level3": "Specifying an exception type like ZeroDivisionError ensures that only expected errors are caught, leading to better error management and debugging."
        },
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
        "hints": {
            "level1": "Check exception syntax.",
            "level2": "Why is it important to bind the exception to a variable in an except clause?",
            "level3": "Binding the exception to a variable using 'as e' allows you to access the exception details, which aids in debugging and logging."
        },
        "knowledge_point": "Exception variable syntax"
    }
])

# --- Medium level exception handling problems ---
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
        "hints": {
            "level1": "Review multiple exception handling.",
            "level2": "Why should general exceptions be placed after specific ones in exception handling?",
            "level3": "Specific exceptions should be caught before a general exception clause to avoid masking the details of the actual error, enabling more precise error handling."
        },
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
        "hints": {
            "level1": "Review file handling with exceptions.",
            "level2": "What is the effect of manually closing a file when using a context manager?",
            "level3": "When using a 'with' statement, the file is automatically closed after the block is executed. Manually closing the file can cause errors, so it's best to let the context manager handle it."
        },
        "knowledge_point": "Context managers and exception propagation"
    }
])

# --- Hard level exception handling problems ---
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
        "hints": {
            "level1": "Review custom exception syntax.",
            "level2": "What syntax errors are present in the custom exception definitions?",
            "level3": "Ensure that class definitions and methods include colons, and use proper exception chaining with 'from error' to provide context for the exception."
        },
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
        "hints": {
            "level1": "Review file handling syntax.",
            "level2": "How should the loop be structured to ensure files are properly closed even when an error occurs?",
            "level3": "Using a try-finally block ensures that cleanup code is executed regardless of whether an error occurs. The loop should correctly iterate over filenames with proper syntax."
        },
        "knowledge_point": "Resource management and cleanup"
    }
])

# ====================== File I/O Problems ======================

# --- Easy level file I/O problems ---
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
        "hints": {
            "level1": "Review file opening modes.",
            "level2": "What mode should be specified when you intend to read a file?",
            "level3": "When opening a file for reading, you must use the 'r' mode to indicate that the file is being read, which prevents unintended write operations."
        },
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
        "hints": {
            "level1": "Review file handling best practices.",
            "level2": "Why is it important to close a file after performing write operations?",
            "level3": "Closing a file ensures that all data is properly written and resources are released. Neglecting to close a file can lead to data corruption and resource leaks."
        },
        "knowledge_point": "File resource management"
    }
])

# --- Medium level file I/O problems ---
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
        "hints": {
            "level1": "Review CSV file processing.",
            "level2": "How can you ensure that newline characters do not affect field values when processing CSV data?",
            "level3": "Using the strip() method removes newline characters from each line, allowing you to accurately split the CSV fields."
        },
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
        "hints": {
            "level1": "Review exception handling with file operations.",
            "level2": "How can you ensure that the file variable is defined even if an error occurs during file opening?",
            "level3": "Initializing the file variable before the try block prevents reference errors in the finally block, ensuring that file.close() is only called if the file was successfully opened."
        },
        "knowledge_point": "Exception handling with files"
    }
])

# --- Hard level file I/O problems ---
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
        "hints": {
            "level1": "Review binary file processing.",
            "level2": "What syntax is required when opening a file in binary mode?",
            "level3": "Using 'with open(filename, 'rb') as file:' ensures that the file is opened in binary mode, and proper conversion methods (like int.from_bytes) must be used to convert binary data."
        },
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
        "hints": {
            "level1": "Review file locking and context management.",
            "level2": "How can you use context managers to ensure files are properly managed when processing multiple files?",
            "level3": "Using a context manager (the 'with' statement) ensures that files are properly opened and closed, and that methods are called with the correct syntax."
        },
        "knowledge_point": "File locking and resource management"
    }
])

# ====================== Function Problems ======================

# --- Easy level function problems ---
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
        "hints": {
            "level1": "Check function definition syntax.",
            "level2": "What punctuation does a function definition in Python require at the end of its header?",
            "level3": "Every Python function definition must end with a colon, indicating the start of the function body. Omitting the colon results in a SyntaxError."
        },
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
        "hints": {
            "level1": "Review function parameters.",
            "level2": "How can you define a function that provides a default value for a parameter?",
            "level3": "Setting a default value (e.g., greeting='Hello') in the function definition ensures that if the argument is omitted, the function still has a valid value to use."
        },
        "knowledge_point": "Default parameters"
    }
])

# --- Medium level function problems ---
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
        "hints": {
            "level1": "Review dictionary creation and type checking.",
            "level2": "What is the correct way to iterate over a dictionary's items and check the type of a variable?",
            "level3": "Using .items() to iterate over a dictionary and isinstance() for type checking ensures that you process each key-value pair correctly and handle type conversions appropriately."
        },
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
        "hints": {
            "level1": "Review function parameter ordering.",
            "level2": "How should parameters be ordered when using *args along with non-default parameters?",
            "level3": "In Python, non-default parameters must come before *args to avoid ambiguity and ensure that all arguments are passed correctly to the function."
        },
        "knowledge_point": "Variable arguments and keyword arguments"
    }
])

# --- Hard level function problems ---
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
        "hints": {
            "level1": "Review loop and dictionary operations.",
            "level2": "How does the incorrect use of dictionary methods affect the output of the function?",
            "level3": "Appending to a dictionary is not valid; instead, you should build a dictionary by assigning key-value pairs. Also, the syntax in the loop must be corrected for proper iteration."
        },
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
        "hints": {
            "level1": "Review decorator syntax.",
            "level2": "What changes are necessary to correctly define a decorator function?",
            "level3": "The decorator function should have proper parentheses and colons, and the condition should use '==' for comparison, not '='."
        },
        "knowledge_point": "Decorator syntax and function wrapping"
    }
])

# ====================== List Problems ======================

# --- Easy level list problems ---
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
        "hints": {
            "level1": "Review list methods.",
            "level2": "What is the difference between append and extend when adding elements to a list?",
            "level3": "append() adds its argument as a single element, while extend() iterates over its argument and adds each element individually."
        },
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
        "hints": {
            "level1": "Review list slicing syntax.",
            "level2": "How do you correctly slice a list to obtain the last two elements?",
            "level3": "Using 'fruits[-2:]' slices the list from the second-to-last element to the end, returning the last two elements."
        },
        "knowledge_point": "List slicing syntax"
    }
])

# --- Medium level list problems ---
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
        "hints": {
            "level1": "Review list comprehension syntax.",
            "level2": "How can you include a condition within a list comprehension?",
            "level3": "By placing the condition after the iteration variable (e.g. 'for num in numbers if num % 2 == 0'), you filter the elements directly in the comprehension."
        },
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
        "hints": {
            "level1": "Review nested list processing.",
            "level2": "How can you correctly calculate row sums in a matrix?",
            "level3": "By iterating directly over each row using the correct variable name, you ensure that the sum is computed for each individual row."
        },
        "knowledge_point": "Nested list comprehension and operations"
    }
])

# --- Hard level list problems ---
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
        "hints": {
            "level1": "Review dictionary and list comprehension.",
            "level2": "How can you compute averages using a dictionary comprehension?",
            "level3": "By iterating over the list of students and calculating the average of scores using sum() and len(), you can create a dictionary mapping student names to their average scores."
        },
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
        "hints": {
            "level1": "Review list grouping techniques.",
            "level2": "How can you group items by a specific key using a dictionary?",
            "level3": "By using a dictionary's setdefault() method, you can group items by their type and then sort them accordingly."
        },
        "knowledge_point": "List grouping, sorting, and flattening"
    }
])

# ====================== Algorithm Problems ======================

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
        "hints": {
            "level1": "Review binary search conditions.",
            "level2": "What condition should be checked to determine if the middle element equals the target?",
            "level3": "The condition should use 'if arr[mid] == x:' to verify equality, ensuring that the binary search works as expected."
        },
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
        "hints": {
            "level1": "Review binary search in a rotated array.",
            "level2": "How can you determine if the left half of the array is sorted?",
            "level3": "By comparing nums[low] and nums[mid] using '<=' you can decide which half of the array is correctly sorted and adjust the search range."
        },
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
        "hints": {
            "level1": "Review BFS queue implementation.",
            "level2": "Why might a deque be more efficient than a list for queue operations in BFS?",
            "level3": "A deque provides O(1) time complexity for popping elements from the left, making it more efficient for breadth-first search than a list."
        },
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
        "hints": {
            "level1": "Review BFS shortest path logic.",
            "level2": "What should be modified in the tuple added to the queue to correctly track distance?",
            "level3": "When adding neighbors to the queue, the distance should be incremented (i.e., distance + 1) to correctly reflect the number of steps taken."
        },
        "knowledge_point": "BFS shortest path tracking"
    }
])

# ====================== Data Structure Problems ======================

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
        "hints": {
            "level1": "Review BFS traversal in trees.",
            "level2": "What method should be used to dequeue the next node in a FIFO manner?",
            "level3": "In a breadth-first traversal, using deque's popleft() ensures that nodes are processed in the order they were added."
        },
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
        "hints": {
            "level1": "Review linked list reversal.",
            "level2": "What variable should be used to progress through the linked list after reassigning pointers?",
            "level3": "After storing the next node in a temporary variable, you must update the current pointer to that saved variable (next_node) to continue the reversal."
        },
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
        "hints": {
            "level1": "Review selection sort swapping.",
            "level2": "How can you swap two elements in a list in Python in a single statement?",
            "level3": "Using Python's tuple assignment (a, b = b, a) swaps the values without needing a temporary variable, making the code concise and error-free."
        },
        "knowledge_point": "Array swapping and sorting algorithms"
    }
])

# ====================== Summary Output ======================

print("Python Debugging Question Bank completed, containing the following categories:")
categories = set(question["category"] for level in question_bank.values() for question in level)
for category in sorted(categories):
    print(f"- {category}")

print("\nTotal number of questions:", sum(len(level) for level in question_bank.values()))
