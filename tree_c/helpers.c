#include "tree.h"
#include <stdio.h>
#include <stdlib.h>

void add(Node **head, int val)
{
  if (!*head)
  {
    *head = makeNode(val);
    return;
  }

  /*
   * recursively traverse the tree till you find the position of val
   * */

  if (!(*head)->left)
  {
    (*head)->left = makeNode(val);
    return;
  }

  if (!(*head)->right)
  {
    (*head)->right = makeNode(val);
    return;
  }

  // else:
  add(&(*head)->left, val);
  add(&(*head)->right, val);
}

void print_tree(Node *head, int level)
{
  if (head)
  {
    for (int i =0; i < level; i++) {putchar('\t');}

    printf("%d\n", head->val);
    // recurse
    print_tree(head->left, level - 1);
    print_tree(head->right, level + 1);

    return;
  }
}

Node *makeNode(int val)
{
  Node *node = malloc(sizeof(Node));
  if (node)
  {
    node->left = NULL;
    node->right = NULL;
    node->val = val;
  }
  return node;
}
