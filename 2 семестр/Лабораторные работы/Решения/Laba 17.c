/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#define STACK_OVERFLOW  -100

int i;

typedef struct node_tag{
    int element;
    struct node_tag *next;
}Node_t;

int check (char elem[], int *number);
void add_in_steck (Node_t **head, int elem);
void print_steck (Node_t **head);
int steck_sum (Node_t **head);
void remove_from_steck (Node_t **head, int k);


int main()
{
    char elem[4];
    int number;
    Node_t *head=NULL;
    scanf ("%s", elem);
    while (check(elem, &number)){
        add_in_steck(&head, number);
        scanf ("%s", elem);
    }
    int k=2;
    remove_from_steck (&head, k);
    print_steck (&head);
    printf("\n%d\n", steck_sum(&head));
    return 0;
}

void remove_from_steck (Node_t **head, int k){
    Node_t *tmp = malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    if (head==NULL)
        exit;
    for (i=0; i<k; i++){
        if (head==NULL)
        exit;
        tmp=*head;
        *head=tmp->next;
        free (tmp);
    }
}

int steck_sum (Node_t **head){
    int sum=0;
    Node_t *tmp = malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    if (head==NULL)
        exit;
    tmp=*head;
    while (tmp!=NULL){
        sum+=tmp->element;
        tmp=tmp->next;
    }
    return sum;
}

void add_in_steck (Node_t **head, int elem){
    Node_t *tmp=malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    tmp->next=*head;
    tmp->element=elem;
    *head=tmp;
}

void print_steck (Node_t **head){
    Node_t *tmp = malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    if (head==NULL)
        exit;
    tmp=*head;
    while (tmp!=NULL){
        printf("%4d", tmp->element);
        tmp=tmp->next;
    }
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


