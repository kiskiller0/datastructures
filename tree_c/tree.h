#ifndef HELPERS_H
#define HELPERS_H

typedef struct node Node;
struct node {
	int val;
	Node *left;
	Node *right;
};


void add(Node **head, int val);
void print_tree(Node *head, int level);

Node *makeNode(int val);

#endif
