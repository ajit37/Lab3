#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: avirk18

def operate(number1, number2, operator):
    if operator == 'add':
        output = number1 + number2
        return output 
    elif operator == 'subtract':
        output = number1 - number2
        return output
    elif operator == 'multiply':
        output = number1 * number2
        return output
    else:
        return('Error: function operator can be "add", "subtract", or "multiply"')
    # Place logic in this function

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
