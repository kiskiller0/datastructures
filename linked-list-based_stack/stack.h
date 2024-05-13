#ifndef STACK_H
#define STACK_H

#include "stack.h"


struct node {
    int val;
    struct node * previous;
    struct node * next;
};

typedef struct node Node;

struct stack {
    Node *head;
    Node *tail;
    int index;
};

typedef struct stack Stack;

Node *make_node(int val);
Stack *make_stack();
void push(Stack *head, int val);
void printAll(Stack *head);
int pop(Stack *head);

#endif