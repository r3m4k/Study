/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int a, b, c;    //Для задания 1
    int k, m, i;    //Для задания 2
    int x, z;       //Для степеней
    scanf ("%d %d %d", &a, &b, &c);
    scanf ("%d", &m);
    if ((a>b && b>c)||(a<b && b<c))
            {
                printf ("%d\n", b);
            }    
    else if ((b>a && a>c)||(b<a && a<c))
            {
                printf ("%d\n", a); 
            }
    else if ((a>c && c>b)||(a<c && c<b))
            {
                printf ("%d\n", c); 
            }
    else if (a==b && b==c)
            {
                printf ("%d=%d=%d\n", a, b, c);
            }
    else if (a==b && b>c)
            {
                printf ("%d=%d>%d\n", a, b, c); 
            }
    else if (a==b && b<c)
            {
                printf ("%d=%d<%d\n", a, b, c);
            }
    else if (b==c && b>a)
            {
                printf ("%d=%d>%d\n", b, c, a);
            }
    else if (b==c && b<a)
            {
                printf ("%d=%d<%d\n", b, c, a);
            }
    else if (a==c && a>b)
            {
                printf ("%d=%d>%d\n", a, c, b);
            }
    else if (a==c && a<b)
            {
                printf ("%d=%d<%d\n", a, c, b);
            }
    //Задание 2
    printf ("\n");
    k=3;
    i=1;
    while (k<=m)
        {
            k*=3;
            i++;
        }
    printf ("%d\n", i);
    printf ("\n");
    
    //Задание со степенями
    z=1;
    for (x=1; x<10; x++)
        {
            z*=3;
            printf ("  %d  %d\n", x, z);
        }
    for (x=10; x<=15; x++)
        {
            z*=3;
            printf (" %d  %d\n", x, z);
        }
    return 0;
}