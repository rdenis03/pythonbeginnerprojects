def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "No possible operation . Can't divide"
    return a/b

#dicitionar de operatii cum functioneaza practic 1,2,3,4 sunt niste chei care definesc numele operatiei si functia acesteia
operations ={
    '1':{'name': "Addition", "func": addition},
    '2':{'name':"Substraction","func": substraction},
    '3':{'name': 'Multiply', 'func': multiply},
    '4':{'name':'Division', 'func': division}
}
print("Simple calculator")

for key, op in operations.items():
    print(f'Print {key}. {op['name']}')

user_input = input("Select operation ").strip()
if user_input in operations:
    print(f'You have selected {operations[user_input]['name']}')
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: " ))
    except ValueError:
        print("Error, enter valid numbers! ")
    else:
        result = operations[user_input]["func"](num1,num2)
        print('Result', result)
else:
    print("No selected operation")