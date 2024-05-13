# Trees (Binary)

## TLDR;
You got a head node, containing a value, a pointer to a left node and a pointer to a right node;

```py
class tree:
    def __init__(self, val):
        self.val = val
        self.left=None
        self.right=None
        
    
    def print_all(head, level=3):
        if head:
            print(
                ''.join(
                    ['\t' for _ in range(level)]
                ), end=''
            )
            print(head.val)
            tree.print_all(head.left, level - 1)
            tree.print_all(head.right, level + 1)
            


head = tree(1)
head.left = tree(2)
head.right = tree(3)

tree.print_all(head)
```