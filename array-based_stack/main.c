#include <stdio.h>
#include "stack.h"


void main() {
    Stack *stack = make_stack(6);
    
    for (int i = 0; i < 5; i++) {
        push(stack, i);
    }

    for (int i = 0; i < 15; i++) {
        printf("%d: %d\n", i, pop(stack));
    }

}