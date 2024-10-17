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

void func_double (int **a, int k);
void func_zero (int **a, int k);
void func_print (int **a, int k);
void func_random (int **a, int k);
void func_del (int **a, int k);
void func_add (int **a, int k);
void func_write (int **a, int k);   //Для записи в файл
void func_read (int **a, int k);    //ля чтения из файла

int main()
{
    int n_1, *p;
    printf ("Введите число n: ");
    scanf ("%d", &n_1);
    p=(int*)calloc (n_1, sizeof(int));
    if (p == NULL) 
        exit(EXIT_FAILURE);
    for (i=0; i<n_1; i++)
        p[i]=rand()%50+1;    //Заполнение массива случайными числами от 1 до 50
    func_double (&p, n_1);
    func_print (&p, 2*n_1);   
    free (p);
    
    //Конец 1 части задания
    
    int *w, n_2, f;
    printf ("Введите количество элементов массива: ");
    scanf ("%d", &n_2);
    w=(int*)calloc (n_2, sizeof(int));
    func_random (&w, n_2);  
    func_print (&w, n_2);
    /*
    Функцию ввода чисел с клавиатуры лень писать, 
    да и это немного бесполезно, хоть знаю, как это делать.
    Просто для нормальной работы кода нужно будет писать if условие 
    на то, каким способом заполнять массив.
    Это должно быть реализовано примерно как далее.
    */
    printf ("Производить удаление элемента со сдвигом?\n");
    printf ("Если да, то введите 1, если нет, то введите 0\n", &f);
    scanf ("%d", &f);
    if (f==0){
        printf ("\n");
        goto label_1;
    }
    else{
        func_del(&w, n_2);
        n_2-=1;
    }
    label_1:
    printf ("Производить добавление элемента со сдвигом?\n");
    printf ("Если да, то введите 1, если нет, то введите 0\n", &f);
    scanf ("%d", &f);
    if (f==0){
        printf ("\n");
        goto label_2;
    }
    else{
        func_add(&w, n_2);
        n_2+=1;
    }
    label_2:
    func_print (&w, n_2);
    free (w);
    //Конец 2-ой части
    return 0;
}

void func_double (int **a, int k){
    int *q;
    q=(int*)realloc(*a, 2*k*sizeof(int));
    if (q == NULL) 
        exit(EXIT_FAILURE);
    else{
        for (i=0; i<k; i++)
            q[k+i]=q[i];
    }
    func_zero(&q, k);
}


void func_print (int **a, int k){
    for (i=0; i<k; i++)
        printf ("%4d", i+1);
    printf ("\n");
    for (i=0; i<k; i++)
        printf ("%4d", (*a)[i]);
    printf ("\n\n");
}

void func_random (int **a, int k){
    int b, c;
    printf ("Введите диапозон от и до: ");
    scanf ("%d %d", &b, &c);
    printf ("\n");
    for (i=0; i<k; i++)
        (*a)[i]=rand()%(c-b+1)+b;
}

void func_del (int **a, int k){
    int num;
    printf ("\nВведите номер элемента, который необходимо удалить: ");
    scanf ("%d", &num);
    for (i=0; i<(k-num); i++)
        (*a)[num-1+i]=(*a)[num+i];
    (*a)=(int*)realloc(*a, (k-1)*sizeof(int));
    printf ("\n");
}

void func_add (int **a, int k){
    int *q, element, num; 
    q=(int*)realloc(*a, (k+1)*sizeof(int));
    if (q == NULL) 
        exit(EXIT_FAILURE);
    else {
        printf ("\nВведите номер элемента, куда необходимо добавить элемент: ");
        scanf ("%d", &num);
        printf ("Введите значение элемента: ");
        scanf ("%d", &element);
        for (i=k; i>num-1; i--)
            q[i]=q[i-1];
        q[num-1]=element;
    }
    printf ("\n");
}

void func_zero (int **a, int k){
    for (i=0; i<k; i++)
        (*a)[i]=0;
}


/*void func_write (int **a, int k){  //Для записи в файл
    FILE *fp;
    fp=fopen("myfile.txt", "w");
    if ( (fp = fopen("myfile.txt","w")) == NULL ) {
        printf("Не удается открыть файл.\n");
        exit(1); //завершение программы с возвратом кода ошибки 1 
    }
    for (i=0; i<k; i++){
        fprintf (fp, (*a)[i]);
        fprintf (fp, " ");
    }
    fclose (fp);
}


void func_read (int **a, int k){    //Для чтения из файла
    FILE *fp'
    fp=fopen("myfile.txt", "r");
    if ( (fp = fopen("myfile.txt","r")) == NULL ) {
        printf("Не удается открыть файл.\n");
        exit(1); // завершение программы с возвратом кода ошибки 1
    }
    for (i=0; i<k; i++)
        fscanf(fp, (*a)[]);
    fclose(fp);
}

*/
