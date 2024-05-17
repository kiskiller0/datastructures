from stack import Stack

def param_checker(equation: str) -> bool:
    opening = Stack[int]()

    for i in range(len(equation)):
        if equation[i] == '(':
            opening.push(i)
            i+=1
            continue

        if equation[i] == ')':
            if opening.size() == 0:
                print("the equation is un-balanced, lacking in opening parantheses")
                return False

            print(equation[opening.pop() :i + 1], '\n\n')


        i+=1

    balanced = opening.size() == 0

    print(f'the equation is {"balanced" if balanced else "un-balanced, lacking in closing parantheces"}')

    return balanced

# param_checker(
# '''
#     (defun factorial (n &optional (acc 1))
#     (if (zerop n) acc
#         (factorial (1- n) (* acc n))))
# '''
# )

symbols: dict[str, str] = {
    '(': ')',
    '{': '}',
    '[': ']',
}

closing_symbols = [')', '}', ']']

def duo_checker(equation: str, opening:str,) -> bool:
    closing = symbols[opening]
    openings = Stack[int]()

    for i in range(len(equation)):
        if equation[i]== opening:
            openings.push(i)
        if equation[i] == closing:
            if openings.size() == 0:
                return False
            openings.pop()

        i+=1

    return openings.size() == 0

def duo_checker_generic(equation: str) -> bool:
    openings = Stack[int]()

    for i in range(len(equation)):
        # if the current letter constitutes an opening symbol
        if equation[i] in symbols.keys():
            openings.push(i)

        # if the current letter constitutes a closing symbol
        if equation[i] in closing_symbols:
            if openings.size() == 0:
                return False

            # check if the closing and opening symbols match (according to the dict symbols)
            if symbols[equation[openings.peek()]] != equation[i]:
                print(f'wrong closing symbol, equation un-balanced!')
                return False

            # now pop the opening symbol
            openings.pop()

        i+=1

    return openings.size() == 0

lisp_code_sample = '''
        (defun factorial (n &optional (acc 1))
        (if (zerop n) acc
            (factorial (1- n) (* acc n))))
    '''

print(duo_checker_generic(lisp_code_sample))
print(duo_checker_generic("((((({{{{({(})}}}}))))))"))


def dec_to_bin(dec: int) -> str:
    # tbh I don't understand the algorithm now, maybe revisit after some number theory in the future
    rem_stack = Stack[int]()

    while dec > 0:
        rem_stack.push(dec % 2)
        dec //= 2
    
    bin_string:str = ""

    while rem_stack.size() > 0:
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


def dec_to_base(base:int, dec: int) -> str:
    # tbh I don't understand the algorithm now, maybe revisit after some number theory in the future
    rem_stack = Stack[int]()

    while dec > 0:
        rem_stack.push(dec % base)
        dec //= base
    
    base_x_string:str = ""

    while rem_stack.size() > 0:
        base_x_string = base_x_string + map_number(rem_stack.pop())

    return base_x_string

def map_number(num: int) -> str:
    if num > ord('z') + 10:
        print('error!')
        raise ValueError("value is above normal alphabet! are you trying to speak with aliens ?\ntry using the entire ASCII table")

    if num > 9:
        return chr((num - 10) + ord('a'))
    return str(num)


print(dec_to_base(8, 25))
print(dec_to_base(16, 256))
print(dec_to_base(26, 26))
print(dec_to_base(16, 11))
print(dec_to_base(16, 11))

for i in range(200):
    print(f'digit {i} is mapped to: {map_number(i)}')

print(f'done')



