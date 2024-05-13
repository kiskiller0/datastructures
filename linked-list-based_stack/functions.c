#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

// implementing a fixed size stack using arrays
// Badreddine, 11/05/2024

#include "stack.h"


Node *make_node(int val) {
    Node *node = malloc(sizeof(Node));
    node->val = val;
    return node;
}

Stack *make_stack(int size) {
    Stack *stack = malloc(sizeof(Stack));
    stack->index = 0;

    return stack;
}

void push(Stack *stack, int val) {
    if (! stack -> head) {
        stack -> head = make_node(val);
        stack -> head -> previous = NULL; // head has no previous.
        stack -> tail = stack -> head;
    }
    stack -> tail -> next = make_node(val);
    stack -> tail -> next -> previous = stack -> tail;
    stack -> tail = stack -> tail -> next;
}

int pop(Stack *stack) {
    // if (!stack) {return 111111;}
    int val = stack->tail->val;
    Node *previous_tail = stack->tail->previous;
    free(stack->tail);
    stack->tail = previous_tail;

    return val;
}