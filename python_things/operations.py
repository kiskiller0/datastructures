from stack import Stack

operations: set[str] = {'+', '-', '/', '*'}

def is_space(sym: str) -> bool:
    return  True if sym == ' ' else True if sym == '\t' else True if sym == '\n' else False

def parse_equation(equation: str):
    operands = Stack[str]()
    operators = Stack[str]()

    for sym in equation:
        if is_space(sym):
            continue
        if sym in operations:
            operators.push(sym)
            continue
        
        if (operands.size() > 1):
            print(f'why do you have {operands.size()} args already ?')

        operands.push(sym)

    # now executing the ops:
    # assuming we have a hashtable of {operator: num operands}

    while operands.size() != 0 and operators.size() != 0:
        op = operators.pop()

        arg1 = int(operands.pop())
        arg2 = int(operands.pop())

        if op == '+':
            operands.push(str(arg1+arg2))

        if op == '-':
            operands.push(str(arg1+arg2))

        elif op == '*':
            operands.push(str(arg1*arg2))

        elif op == '/':
            operands.push(str(arg1/arg2))

    # at the end, we should have no operations, and one operand
    if operators.size() > 0 or operands.size() > 1:
        raise ValueError("equation unbalanced")

    return operands.pop()

print(parse_equation("3 + 4 * 2 + 3"))
