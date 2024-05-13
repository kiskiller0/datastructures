

#ifndef STACK_H
#define STACK_H

#include "stack.h"

struct stack {
    int *array;
    int index;
    int size;
};

typedef struct stack Stack;

void push(Stack *head, int val);
void printAll(Stack *head);
int pop(Stack *head);
Stack *make_stack(int val);

#endif