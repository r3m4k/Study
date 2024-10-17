/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <math.h>

int a, b, c;
double x1, x2, f,
        *p_x1=&x1, *p_x2=&x2, *p_f=&f;
        
void func (int m, int n, int k);
int main()
{   
    scanf ("%d %d %d", &a, &b, &c);
    func (a, b, c);
    printf ("%.0lf\n", f);
    if (x1!=0)
    printf ("%.6lf\n", x1);
    if (x2!=0)
    printf ("%.6lf\n", x2);
    return 0;
}
void func (int m, int n, int k)
{
    double D;
    D=n*n-(4*m*k);
    if (m==0){
        *p_x1=-k/n;
        *p_f=1;
    }
    else if (D<0){
        *p_f=2;
    }
    else if (D==0){
        *p_f=3;
        *p_x1=(n*n)/(2*m);
    }
    else if (D>0){
        *p_f=0;
        *p_x1=((-n)-sqrt(D))/(2*m);
        *p_x2=((-n)+sqrt(D))/(2*m);
    }
}