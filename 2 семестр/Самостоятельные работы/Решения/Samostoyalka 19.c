/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

typedef struct _nodetree{
    int data;
    struct _nodetree *right;
    struct _nodetree *left;
    struct _nodetree *parent;
}Node;

void insert(Node **root, int data);

void inOrderTravers(Node* root);
void postOrderTravers(Node* root);

void removeNode(Node *target);
Node* findMinNode (Node* root);
Node* findMaxNode (Node* root);

Node* search (Node *root, int value);

int height(Node *node);
int max (int a, int b);
int Sum_One(Node *root);

Node* createNodeTree (Node *parent, int data);
int check (char elem[], int *number);

int main()
{
    Node *root = NULL;
    char elem[4];
    scanf ("%s", elem);
    int number;
    while (check(elem, &number)){
        insert (&root, number);
        scanf ("%s", elem);
    }
    postOrderTravers (root);
    printf ("\n");
    //printf ("%d\n", Sum_One(root));
    int searched_value;
    scanf ("%d", &searched_value);
    Node *searched = search (root, searched_value);
    
    if (searched != NULL){
        removeNode (searched);
        postOrderTravers (root);
        printf ("\n%d\n", Sum_One(root));
    }
    else
        printf ("!\n");
    
    return 0;
}


void removeNode(Node *target) {
    if (target->left && target->right) {
        Node *localMax = findMaxNode(target->left);
        target->data = localMax->data;
        removeNode(localMax);
        return;
    } else if (target->left) {
        if (target == target->parent->left) {
            target->parent->left = target->left;
        } else {
            target->parent->right = target->left;
        }
    } else if (target->right) {
        if (target == target->parent->right) {
            target->parent->right = target->right;
        } else {
            target->parent->left = target->right;
        }
    } else {
        if (target == target->parent->left) {
            target->parent->left = NULL;
        } else {
            target->parent->right = NULL;
        }
    }
    free(target);
}

Node* findMaxNode (Node *root) {
    if (root == NULL) {
        exit;
    }
    if (root->right) {
        return findMaxNode (root->right);
    }
    return root;
}

Node* search (Node *root, int value){
    if (!root) {
        return NULL;
    }
    if (root->data > value) {
        search (root->left, value);
    } else if (root->data < value) {
        search (root->right, value);
    } else {
        return root;
    }
}

int height(Node *node){
    if (!node)
        return 0;
 
    int h_l = height(node->left);
    int h_r = height(node->right);
 
    return max(h_l, h_r) + 1;
}

int max (int a, int b){
    if (a<=b)
        return b;
    else 
        return a;
}

int Sum_One(Node *root) {
	int sum_right, sum_left; 
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp = root;
	if (tmp != NULL) {
		sum_right = Sum_One(tmp->right);
		sum_left = Sum_One(tmp->left);
		if ((tmp->left == NULL && tmp->right != NULL) || (tmp->left != NULL && tmp->right == NULL)) 
		    return tmp->data + sum_right + sum_left;
		else return sum_right + sum_left;
	}
}

void insert(Node **root, int data) {
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);

    if (*root == NULL) {
        *root = createNodeTree(NULL, data);
        return;
    }
     
    tmp = *root;
    while (tmp) {
        if (data >= tmp->data) {
            if (tmp->right) {
                tmp = tmp->right;
                continue;
            } else {
                tmp->right = createNodeTree(tmp, data);
                return;
            }
        } else if (data < tmp->data) {
            if (tmp->left) {
                tmp = tmp->left;
                continue;
            } else {
                tmp->left = createNodeTree(tmp, data);
                return;
            }
        } else {
            exit;
        }
    }
}
 
void inOrderTravers(Node* root) {
    if (root) {
        inOrderTravers(root->left);
        printf("%d ", root->data);
        inOrderTravers(root->right);
    }
}
 
void postOrderTravers(Node* root) {
    if (root) {
        postOrderTravers(root->left);
        postOrderTravers(root->right);
        printf("%d ", root->data);
    }
}

Node* createNodeTree (Node *parent, int data){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp->left = tmp->right = NULL;
    tmp->data = data;
    tmp->parent = parent;
    return tmp;
}

int check (char elem[], int *number){
    int f=1;
    *number=0;
    if ((elem[0]>=48)&&(elem[0]<=57)){
        for (i=3; i>=0; i--){
            if ((int)elem[i]!=0){
                *number+=((int)elem[i]-48)*f;
                f*=10;
            }
        }
        return 1;
    }
    else 
        return 0;
}