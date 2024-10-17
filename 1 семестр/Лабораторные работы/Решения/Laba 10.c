/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define IN 1
#define OUT 0

void func_zero (int a[], int k);
void func_change (int a[], int b[], int k);
void func_print (int a[], int k);

int main()
{
    int c, res[1024], max=0, state=IN, i=0, word[1024];
    func_zero(word, 1024);
    func_zero(res, 1024);
    while ((c=getchar())!= '\n'){
        if (isalnum(c)){
            putchar (c);
            word[i]=c;
            i++;
            state=IN;
            }
        if (isspace(c) && state==IN){
            putchar ('\n');
            state=OUT;
            if (max<=i){
                max=i;
                func_change(res, word, 1024);
            }
            func_zero(word, 1024);
            i=0;
        }
    }
    if (max<=i){
                max=i;
                func_change(res, word, 1024);
            }
    printf ("\n \n");
    func_print(res, 1024);
    printf ("\n");
    return 0;
}

void func_zero (int a[], int k){
    int i;
    for (i=0; i<k; i++)
        a[i]=0;
}

void func_change(int a[], int b[], int k){
    int i;
    for (i=0; i<k; i++)
        a[i]=b[i];
}

void func_print (int a[], int  k){
    int i=0;
    while ((a[i]!=0)&&(i<=k)){
        printf ("%c", a[i]);
        i++;
    }
}




