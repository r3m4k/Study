/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
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
void print_list (Node_t *head);
void remove_from_beginning (Node_t **head, int k);
void add_in_beginning (Node_t **head, int elem);
void add_in_end (Node_t **head, Node_t **last, int elem);
void remove_from_end (Node_t **head, Node_t **last);
int search (Node_t *head, Node_t **node, int elem);
void del_searched (Node_t *node);


int main()
{
    char elem[4];
    int number;
    Node_t *head=NULL;
    Node_t *last=NULL;
    scanf ("%s", elem);
    while (check(elem, &number)){
        add_in_end (&head, &last, number);
        scanf ("%s", elem);
    }
    print_list (head);
    remove_from_end(&head, &last);
    print_list (head);
    
    Node_t *node=NULL;
    int search_elem;
    scanf ("%d", &search_elem);
    if (search (head, &node, search_elem))
        del_searched (node);
    print_list (head);
    return 0;
}

void del_searched (Node_t *node){
    Node_t *tmp=malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    tmp=node->next;
    node->next=tmp->next;
    free (tmp);
}

int search (Node_t *head, Node_t **node, int elem){
    *node=head;
    while ((*node)->element!=elem){
        if (((*node)->next==NULL)&&((*node)->element!=elem))
            return 0;
        *node=(*node)->next;
    }
    return 1;
}

void add_in_end (Node_t **head, Node_t **last, int elem){
    i=0;
    Node_t *tmp=malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    tmp->next=NULL;
    tmp->element=elem;
    if (*head == NULL)
        *head = tmp;
    else
        (*last)->next = tmp;
    *last = tmp;
}

void add_in_beginning (Node_t **head, int elem){
    Node_t *tmp=malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    tmp->next=*head;
    tmp->element=elem;
    *head=tmp;
}

void remove_from_end (Node_t **head, Node_t **last){
    if (*head == NULL)
        return;
    Node_t *tmp=malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    tmp=*head;
    if (tmp->next == NULL) 
    {
        free(tmp);
        *head = NULL;
        return;
    }
    
    Node_t *tmp_prlast=malloc(sizeof(Node_t));
    if (tmp_prlast == NULL) 
        exit(STACK_OVERFLOW);
    while (tmp->next != NULL)
    {
        tmp_prlast = tmp;
        tmp = tmp->next;
    }
    tmp_prlast->next = NULL;
    free(tmp);
    *last = tmp_prlast;
}

void remove_from_beginning (Node_t **head, int k){
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

void print_list (Node_t *head){
    Node_t *tmp = malloc(sizeof(Node_t));
    if (tmp == NULL) 
        exit(STACK_OVERFLOW);
    if (head==NULL)
        exit;
    tmp=head;
    while (tmp!=NULL){
        printf("%4d", tmp->element);
        tmp=tmp->next;
    }
    printf ("\n");
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

