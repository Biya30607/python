import math
import random
from datetime import datetime
import os
number = 16
sqrt_number = math.sqrt(number)
factorial_number = math.factorial(5)
print(f"Square root of {number}: {sqrt_number}")
print(f"Factorial of 5: {factorial_number}")


rand_int = random.randint(1, 100)
rand_choice = random.choice(['apple', 'banana', 'cherry'])
print(f"Random integer between 1 and 100: {rand_int}")
print(f"Random choice from list: {rand_choice}")


now = datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


cwd = os.getcwd()
files = os.listdir(cwd)
print(f"Current working directory: {cwd}")
print(f"Files in current directory: {files[:5]}...")  # show only first 5 for brevity
