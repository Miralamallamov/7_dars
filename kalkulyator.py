def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    # foydalanuvchidan operatsiyani so'rash
    operation = input("matemalik amalni tanlang (+, -, *, /): ")

    # birin ketin faydalanuvchidan raqamlarni so’rash
    num1 = float(input("1- raqamni kiriting: "))
    num2 = float(input("2- raqamni kiriting: "))

    # operatsiyani bajarish
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Xato: noto'g'ri operatsiya tanlandi.")
        continue

    # natijani chiqaramiz
    print(f"Результат: {result}\n")
