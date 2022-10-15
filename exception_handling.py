def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Dividing by zero is meaningless."

print(divide(1, 0))