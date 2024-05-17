from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.array: list[T] = []

    def peek(self) -> T:
        return self.array[-1]
    
    def pop(self) -> T:
        return self.array.pop()
    
    def push(self, val: T):
        self.array.append(val)

    def size(self) -> int:
        return len(self.array)
    
    def is_empty(self) -> bool:
        return len(self.array) == 0

    def toString(self) -> str:
        # TODO(bader): make a copy of the original stack, modify the copy, toString shouldn't mutate data
        l: list[str] = ['' for _ in range(self.size())]
        
        i = 1
        while self.size() > 0:
            l[-i] = str(self.pop())
            i += 1

        return ''.join(l)

    def clone(self):
        stack = Stack[T]()
        for i in range(self.size()):
            stack.push(self.array[i])

        return stack

    def __repr__(self):
        return '[' + ', '.join(self.array) + ']'


# class Reversable(Stack[T]):
#    
#     def __init__(self):
#         super().__init__()
#
#     def reverse(self) -> list[T]:
#         s_reversed = Stack[T]()
#         while not self.is_empty():
#             s_reversed.push(self.pop())
#         return s_reversed.array



# def reverse_string(s: str) -> str:
#
#     stack = Stack[str]()
#
#     for letter in s:
#         stack.push(letter)
#
#     str_list:list[str] = []
#
#     while not stack.is_empty():
#         str_list.append(stack.pop())
#    
#
#
#     return ''.join(str_list)

def is_alphanum(s):
    return ord(s) >= ord('a') and ord(s) <= ord('z') or ord(s) >= ord('A') and ord(s) <= ord('Z') or ord(s) >= ord('0') and ord(s) <= ord('9')
