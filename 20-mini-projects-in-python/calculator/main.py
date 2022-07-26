from art import logo

print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    """
    Main calculator function
    """
    continue_loop = True
    try:
        num1 = float(input('What\'s the first number?: '))
        result = num1
        while continue_loop:
            num1 = result
            for operator in operations:
                print(operator)
            operator = input('Pick an operation: ').lower()
            num2 = float(input('What\'s the next number?: '))
            function = operations[operator]
            result = function(num1, num2)
            print(f'{num1} {operator} {num2} = {result}\n')
            choice = input(f'Type "y" to continue calculating with {result}, type "n"'
                           + ' to start a new calculator or type "q" to quit: ').lower()
            if choice == 'n':
                calculator()
            elif choice == 'q':
                continue_loop = False
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt not allowed.')
        calculator()
    except Exception as ex:
        print(f'\n{ex}')
        calculator()


calculator()
