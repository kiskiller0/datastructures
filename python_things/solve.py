from stack import Stack
from operations import is_space


operators_symbols = ('+', '-', '/', '*')

def postfixit(equation:str) -> str:
    
    # what are we doing, TLDR;
    # a + b * c = a b c * + = (begin from left, until you hit an operator)
    # a + b * c + d = a bc* d+ + = (begin from left, until you hit an operator)
    #                         pop it and read two operands
    #                         now apply the operator to them and push them
    #                         repeat ...

    operators = Stack[str]() # needs to be FIFO
    operands = Stack[str]() # LIFO, so we need to reverse it later


    for symbol in equation:
        if is_space(symbol):
            continue

        if symbol in operators_symbols:
            operators.push(symbol)
            continue

        operands.push(symbol)
        

    return str( operands.toString() + ''.join(operators.array ))


print(postfixit(' a + b * c'))
