#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

// implementing a fixed size stack using arrays
// Badreddine, 11/05/2024

#include "stack.h"

Stack *make_stack(int size) {
    Stack *stack = malloc(sizeof(Stack));
    stack->array = malloc(size * sizeof(int));
    stack->index = 0;
    stack->size = size;

    return stack;
}

void push(Stack *stack, int val) {
    if (stack -> index >= stack -> size) {
        // remove the first element, relocate n - 1
        for (int i = 0; i < stack -> index - 1; i++) {
            stack -> array[i] = stack -> array[i + 1];
        }
    }

    stack -> array [stack -> index ++] = val;
}

int pop(Stack *stack) {
    if (stack->index == 0) {
        return INT_MAX;
    }

    return stack -> array [--stack -> index];
}