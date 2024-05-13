#include <stdio.h>
#include "stack.h"


int main() {
    Stack *stack = make_stack();
    
    for (int i = 0; i < 15; i++) {
        push(stack, i);
    }

    for (int i = 0; i < 15; i++) {
        printf("%d: %d\n", i, pop(stack));
    }

}