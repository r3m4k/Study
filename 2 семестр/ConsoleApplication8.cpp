#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

typedef struct tree {
	int key;
	struct tree* left;
	struct tree* right;
}Tree;

void Add(Tree** root, int i);
void inOrder(Tree* root);
void postOrder(Tree* root);
int count(Tree* root);
int Sum_One(Tree* root);

int main() {
	int i = 0;
	char c[10];
	Tree* root = NULL;
	Tree* t, * tp, * p;

	while (1) {
		scanf("%s", c);
		if (c[0] == 'n') break;
		p = (Tree*)malloc(sizeof(Tree));
		p->key = atoi(c);
		if (i == 0) {
			p->left = NULL;
			p->right = NULL;
			root = p;
		}
		else {
			Add(&root, p->key);
		}
		i++;
	}

	//printf("%d\n", count(root)-1);

	/*inOrder(root);
	printf("\n");*/
	postOrder(root);
	printf("\n");

	printf("%d\n", Sum_One(root));

	return 0;
}

void Add(Tree** root, int i) {
	Tree * tp, *t, * p = (*root);
	
	if (*root == NULL) {
		p = (Tree*)malloc(sizeof(Tree));
		p->key = i;
		p->left = NULL;
		p->right = NULL;
		(*root) = p;
	}
	else {
		if (i < p->key) 
			Add(&(p->left), i);
		else
			Add(&(p->right), i);
	}
}

void inOrder(Tree* root) {
	Tree* p = root;
	if (p != NULL) {
		inOrder(p->left);
		printf("%3d ", p->key);
		inOrder(p->right);
	}
	else return;
}

void postOrder(Tree* root) {
	Tree* p = root;
	if (p != NULL) {
		postOrder(p->left);
		postOrder(p->right);
		printf("%3d ", p->key);
		
	}
	else return;
}

void breadth_first(Tree* root) {
	if (root == NULL) {
		return;
	}

	// Создаем очередь для обхода в ширину и помещаем корень в очередь
	struct Tree** queue = (struct Tree**)malloc(sizeof(struct Tree*));
	int front = 0;
	int rear = 0;
	queue[rear] = root;
	rear++;

	while (front < rear) {
		// Извлекаем узел из очереди и выводим его значение
		struct Tree* current = queue[front];
		front++;
		printf("%d ", current->data);

		// Помещаем потомков текущего узла в очередь
		if (current->left != NULL) {
			queue = (struct Node**)realloc(queue, (rear + 1) * sizeof(struct Node*));
			queue[rear] = current->left;
			rear++;
		}
		if (current->right != NULL) {
			queue = (struct Node**)realloc(queue, (rear + 1) * sizeof(struct Node*));
			queue[rear] = current->right;
			rear++;
		}
	}

	free(queue);
}

int count(Tree* root) {
	int i_right, i_left; Tree* p = root;
	if (p != NULL) {
		i_right = count(p->right);
		i_left = count(p->left);
		if (i_right > i_left) {
			return i_right+1;
		}else return i_left+1;
	}
}

int Sum_One(Tree* root) {
	int sum_right, sum_left; Tree* p = root;

	if (p != NULL) {
		sum_right = Sum_One(p->right);
		sum_left = Sum_One(p->left);
		if ((p->left == NULL && p->right != NULL) || (p->left != NULL && p->right == NULL)) return p->key + sum_right + sum_left;
		else return sum_right + sum_left;
	}
}