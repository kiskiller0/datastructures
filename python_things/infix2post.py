from stack import Stack, is_alphanum


def infix_to_postfix(s:str):
    operands: frozenset[str] = frozenset(['+', '-', '/', '*'])

    precedence: dict[str, int] = {
            '+': 1,
            '-': 1,
            '*': 3,
            '/': 3
            }

    result: list[str] = []

    operator_stack = Stack[str]()

    for token in s:
        if is_alphanum(token):
            result.append(token)
        elif token in operands:
            if token == '(':
                operator_stack.push(token)
            elif token == ')':
                # keep popping until you reach the opening paranthese
                current_operator = operator_stack.pop()
                while current_operator != ')':
                    result.append(current_operator)
                    current_operator = operator_stack.pop()

    
    print(operator_stack)
    return result


print(
        infix_to_postfix('((A+B)*C-D)*E')
        )
