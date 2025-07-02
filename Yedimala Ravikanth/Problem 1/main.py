class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def operate(self, operation: str):
        operation = operation.lower()

        if operation == 'add':
            return int(self.a + self.b)
        elif operation == 'subtract':
            return int(self.a - self.b)
        elif operation == 'multiply':
            return int(self.a * self.b)
        elif operation == 'divide':
            if self.b != 0:
                return self.a / self.b  
            else:
                return "Division by zero error"
        else:
            return "Invalid operation"

try:
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    calc = Calculator(a, b)
    result = calc.operate(operation)
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric values for a and b.")
