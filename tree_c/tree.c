#include "tree.h"
#include <stdio.h>

int main() {

  Node *h1 = makeNode(1);
  Node *h2 = makeNode(2);
  Node *h3 = makeNode(3);
  Node *h4 = makeNode(4);
  Node *h5 = makeNode(5);

  h1->left = h2;
  h1->right = h3;
  h3->left = h4;
  h4->left = h5;

  print_tree(h1, 1);
  return 0;
  printf("%d", h1->val);
  printf("%d", h1->left->val);
  printf("%d", h1->right->val);
  // printf("%d", h1->left->val);
  // printf("%d", h1->left->val);

  return 0;
}
