Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x, y):
...     return x + y
... 
... def subtract(x, y):
...     return x - y
... 
... def multiply(x, y):
...     return x * y
... 
... def divide(x, y):
...     if y == 0:
...         raise ValueError("Cannot divide by zero")
...     return x / y
... 
... def evaluate_expression(expression):
...     try:
...         # Split the input into operands and operator
...         tokens = expression.split()
...         if len(tokens) != 3:
...             raise ValueError("Invalid input format. Use: operand1 operator operand2")
...         
...         operand1 = float(tokens[0])
...         operator = tokens[1]
...         operand2 = float(tokens[2])
...         
...         if operator == '+':
...             result = add(operand1, operand2)
...         elif operator == '-':
...             result = subtract(operand1, operand2)
...         elif operator == '*':
...             result = multiply(operand1, operand2)
...         elif operator == '/':
...             result = divide(operand1, operand2)
...         else:
...             raise ValueError("Unsupported operator. Use +, -, *, or /")
...         
        return result
    except ValueError as e:
        return f"Error: {e}"

def main():
    print("Text-based Calculator")
    print("Enter an expression in the format: operand1 operator operand2")
    print("Example: 2 + 3")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        user_input = input("Enter expression: ")
        if user_input.lower() == 'exit':
            break
        result = evaluate_expression(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
