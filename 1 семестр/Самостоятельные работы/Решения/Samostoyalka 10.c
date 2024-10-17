/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define OUT 0
#define IN 1

void func (int a[], char c);
void func_zero (int a[], int k);
void func_print (int a[]);
void func_print_gist (int a);
void func_max_line (int a[], int k);

int main()
{
    int quant_of_fig[10], fig, state=IN, num[30],
        i=0, k=0, state_number=IN;
    func_zero (num, 30);
    func_zero (quant_of_fig, 10);
    
    /*
    int quant_of_num, number, lines;
    FILE *fp;
    fp=fopen("file.txt", "w");
    lines=rand()%31;    //Количество строк
    for (i=1; i<=i_max; i++){
        quant_of_num=rand()%21;    //Количество чисел в строке
        for (i=1; j<=quant_of_num; i++){
            number=rand();
            fprintf (fp, number);
            number=0;
        }
        fprintf ("\n");
        j_max=0;
    }
    fclose(fp);
    fopen("file,txt", "r");
    //Дальше заменить все функции на аналогичны для чтения с файла
    */
    
    while (((fig=getchar())!='\n')||(state==IN)){
        func(quant_of_fig, fig);
        state=OUT;
        if ((isspace(fig))&&(state_number==IN)){
            i+=1;
            state_number=OUT;
        }
        if (fig=='\n'){
            num[k]+=i;
            k+=1;
            i=0;
        }
        state=OUT;
        if (isdigit(fig)){
            state=IN;
            state_number=IN;    
        }
    }
    func_max_line (num, 30);
    func_print(quant_of_fig);
    return 0;
}

void func (int a[], char c){
    int i;
    for (i=48; i<=57; i++){
        if (i==c){
            a[i-48]+=1;
        }
    }
}

void func_max_line (int a[], int k){
    int i=0, max, f=0;
    max=a[0];
    for (i=1; i<k; i++){
        if (max<a[i])
            max=a[i];
    }
    for (i=0; i<k; i++){
        if (a[i]==max){
            if (f!=0)
                printf (" ");
            printf ("%d", i+1);
            f+=1;
        }
    }
    printf ("\n \n");
}

void func_zero (int a[], int k){
    int i;
    for (i=0; i<k; i++)
        a[i]=0;
}

void func_print (int a[]){
    int i, j, b;
    for (i=0; i<10; i++){
        printf ("%d ", i);
        func_print_gist(a[i]);
        printf(" %d\n", a[i]);
    }
}

void func_print_gist (int a){
    int i, b, c;
    b=a/3;
    if (a%3==2)
        b+=1;
    for (i=1; i<=b; i++)
        printf ("*");
}