/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int i; 

struct _hashelem{
    int key;
    char name[10];
};

typedef struct node_tag{
    int inf;
    struct _hashelem *HashElem;
    struct node_tag *next;
    struct node_tag *prev;
}Node;

typedef struct list_tag{
    struct node_tag *head;
    struct node_tag *tail;
}List;

int HashFunction (char name[]);
List* createList ();
void filling_HashElem (struct _hashelem *HashElem, int size);
void addFront (List *list, int data);
void Front_print_list (List *list);

Node* search_name (List *HashTable, int key);
Node* search (List *list, int data);
int sizeofList (List *list);
int max (int arr[], int size);

void AddHashElem (List *HashTable[], int lenght);
void RemoveHashElem (List *HashTable[], int lenght);

void delNode (Node *support_node);


int main()
{
    int size = 10, lenght = 13;
    struct _hashelem HashElem[size];
    //struct list_tag HashTable[lenght];
    List *HashTable[lenght];
    for (i=0; i<lenght; i++)
        HashTable[i] = createList (); 
    filling_HashElem (HashElem, size);
    /*for (i=0; i<size; i++){
        (HashElem[i]).key = HashFunction ((HashElem[i]).name);
    }*/
    (HashElem[0]).key = HashFunction ((HashElem[0]).name);
    (HashElem[1]).key = HashFunction ((HashElem[1]).name);
    (HashElem[2]).key = HashFunction ((HashElem[2]).name);
    (HashElem[3]).key = HashFunction ((HashElem[3]).name);
    (HashElem[4]).key = HashFunction ((HashElem[4]).name);
    (HashElem[5]).key = HashFunction ((HashElem[5]).name);
    (HashElem[6]).key = HashFunction ((HashElem[6]).name);
    (HashElem[7]).key = HashFunction ((HashElem[7]).name);
    (HashElem[8]).key = HashFunction ((HashElem[8]).name);
    (HashElem[9]).key = HashFunction ((HashElem[9]).name);
    
    
    for (i=0; i<size; i++)
        printf ("%s -- %d -- %d\n", (HashElem[i]).name, (HashElem[i]).key, (HashElem[i]).key % lenght);
    
    for (i=0; i<lenght; i++)
        addFront (HashTable[i], 0);
    
    for (i=0; i<size; i++)
        addFront (HashTable[(HashElem[i]).key % lenght], (HashElem[i]).key);
    
    
    for (i=0; i<lenght; i++)
        Front_print_list (HashTable[i]);
    /*
    ////////////////////////////////////////
    
    char searched_name[10];
    scanf ("%s", searched_name);
    printf ("%d -- %d\n",HashFunction (searched_name), HashFunction (searched_name) % lenght );
    if (search_name (HashTable[HashFunction (searched_name) % lenght], HashFunction (searched_name)))
        printf ("%s\n", searched_name);
    else 
        printf ("Not Founded\n");
        
    ////////////////////////////////////////
    
    int lenght_list[lenght];
    for (i=0; i<lenght; i++)
        lenght_list[i] = sizeofList (HashTable[i])-1;
        
    printf ("%d\n", max(lenght_list, lenght));  //Максимальное количество элементов 
    int quant_filling=0;
    for (i=0; i<lenght; i++)
        if (lenght_list[i])
            quant_filling+=1;
    printf ("%.2f\n", (float)quant_filling/lenght);    //Коэффицент заполнения
    
    ////////////////////////////////////////
    */
    AddHashElem (HashTable, lenght);
    RemoveHashElem (HashTable, lenght);
    return 0;
}

void AddHashElem (List *HashTable[], int lenght){
    printf ("////////////////////\n\n");
    struct _hashelem HashAdded[1];
    filling_HashElem (HashAdded, 1);
    (HashAdded[0]).key = HashFunction ((HashAdded[i]).name);
    printf ("%s -- %d -- %d\n", HashAdded->name, HashFunction (HashAdded->name), HashFunction (HashAdded->name) % lenght);
    
    addFront (HashTable[HashFunction (HashAdded->name) % lenght], HashFunction (HashAdded->name));
    for (i=0; i<lenght; i++)
        Front_print_list (HashTable[i]);
}

void RemoveHashElem (List *HashTable[], int lenght){
    printf ("////////////////////\n\n");
    struct _hashelem HashRemoved[1];
    filling_HashElem (HashRemoved, 1);
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp->HashElem = &HashRemoved[0];
    tmp = search_name (HashTable[HashFunction (HashRemoved->name) % lenght], HashFunction (HashRemoved->name));
    if (tmp){
        delNode (tmp);
    }
    else 
        printf ("Not Founded\n");
    //free (&HashRemoved[0]);
    for (i=0; i<lenght; i++)
        Front_print_list (HashTable[i]);
}

int max (int arr[], int size){
    int result = arr[0];
    for (i=1; i<size; i++){
        if (arr[i]>result)
            result = arr[i];
    }
    return result;
}

int sizeofList (List *list){
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

Node* search_name (List *HashTable, int key){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp = search(HashTable, key);
    return tmp;
}

Node* search (List *list, int data){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp=list->head;
    if (list->head->inf != 0){
        while ((tmp->inf!=data)&&(tmp!=NULL))
            tmp=tmp->next;
        if (tmp==NULL)
            return NULL;
        else
            return tmp; 
    }
    else
        return NULL;
}

void addFront (List *list, int data) {
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

void Front_print_list (List *list){
    Node *tmp = malloc(sizeof(Node));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    if (list->head==NULL)
        exit;
    tmp=list->head;
    while (tmp!=NULL){
        //if (tmp->inf != 0)
            printf("%4d", tmp->inf);
        tmp=tmp->next;
    }
    printf ("\n");
}

void filling_HashElem (struct _hashelem *HashElem, int size){
    for (i=0; i<size; i++)
        scanf ("%s", (HashElem[i]).name);
}

int HashFunction (char name[]){
    //printf ("+\n");
    int result = 0;
    for (i=0; i<5; i++){
        if (isalnum(name[i])){
            if (islower(name[i]))
                result += (int)name[i]-96;
            else
                result += (int)name[i]-64;
        }
    }
    return result;
}

List* createList (){
    List *tmp = malloc (sizeof(List));
    if (tmp == NULL) 
        exit(EXIT_FAILURE);
    tmp->head=tmp->tail=NULL;
    return tmp;
}

void delNode (Node *support_node){
    support_node->prev->next = support_node->next;
    support_node->next->prev = support_node->prev;
    free (support_node);
}
