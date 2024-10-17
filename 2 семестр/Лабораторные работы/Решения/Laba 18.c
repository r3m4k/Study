/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

typedef struct node_tag{
    int inf;
    struct node_tag *next;
    struct node_tag *prev;
}Node;

typedef struct list_tag{
    struct node_tag *head;
    struct node_tag *tail;
}DblList;

DblList* createList ();
int check (char elem[], int *number);

void addFront (DblList *list, int data);
void addBack (DblList *list, int data);

void Front_print_list (DblList *list);
void Back_print_list (DblList *list);

void delFront (DblList *list);
void delBack (DblList *list);

int sizeofList (DblList *list);

int main()
{
    DblList *list = createList();
    char elem[4];
    int number;
    scanf ("%s", elem);
    while (check(elem, &number)){
        //addFront (list, number);
        addBack (list, number);
        scanf ("%s", elem);
    }
    
    Front_print_list (list);
    //Back_print_list (list);
    for (i=0; i<2; i++)
        delFront (list);
    //delBack (list);
    Front_print_list (list);
    
    printf ("%d\n", sizeofList(list));
    return 0;
}

void delFront (DblList *list){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp=list->head;
    list->head=list->head->next;
    list->head->prev=NULL;
    free (tmp);
}

void delBack (DblList *list){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp=list->tail;
    list->tail=list->tail->prev;
    list->tail->next=NULL;
    free (tmp);
}

void addFront (DblList *list, int data) {
    Node *tmp = (Node*) malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp->inf = data;
    tmp->next = list->head;
    tmp->prev = NULL;
    if (list->head) {
        list->head->prev = tmp;
    }
    list->head = tmp;
    if (list->tail == NULL) {
        list->tail = tmp;
    }
}

void addBack (DblList *list, int data){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp->inf = data;
    tmp->next = NULL;
    tmp->prev = list->tail;
    if (list->tail) {
        list->tail->next = tmp;
    }
    list->tail = tmp;
 
    if (list->head == NULL) {
        list->head = tmp;
    }
}

void Front_print_list (DblList *list){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    if (list->head==NULL)
        exit;
    tmp=list->head;
    while (tmp!=NULL){
        printf("%4d", tmp->inf);
        tmp=tmp->next;
    }
    printf ("\n");
}

void Back_print_list (DblList *list){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    if (list->tail==NULL)
        exit;
    tmp=list->tail;
    while (tmp!=NULL){
        printf ("%4d", tmp->inf);
        tmp=tmp->prev;
    }
    printf ("\n");
}

int sizeofList (DblList *list){
    int size=0;
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp=list->head;
    while (tmp){
        size++;
        tmp=tmp->next;
    }
    return size;
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

DblList* createList (){
    DblList *tmp = malloc (sizeof(DblList));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp->head=tmp->tail=NULL;
    return tmp;
}
