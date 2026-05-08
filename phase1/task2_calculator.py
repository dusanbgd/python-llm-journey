# Task 2: Calculator + Loops

# 1. A function (your first one!)
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return "Unknown operator"

# 2. A loop — keeps the calculator running until user quits
print("Simple Calculator — type 'quit' to exit\n")

while True:
    user_input = input("Enter calculation (e.g. 10 + 5): ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    # Split input into parts
    parts = user_input.split()
    
    if len(parts) != 3:
        print("Format must be: number operator number")
        continue
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    
    result = calculate(num1, num2, operator)
    print(f"Result: {result}\n")