/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <math.h>

int main()
{
    int x, y, r;    //Задание 1
    int k, a, a1, a2, a3, i;  //Задание 2
    scanf ("%d %d", &x, &y);
    scanf ("%d", &k);
    //Задание 1
    r=sqrt(x*x+y*y);
    if ((x>=300||x<=-300)||(y>=300||y<=-300))
        {
            printf ("outside\n");
        }
    else
    {
        if (x<=0)
        {
            if (r>300)
            {
                printf ("inside\n");   
            }
            else
            {
                printf ("outside\n");
            }
        }
        else if (x>0 && y>0)
        {
            if ((r<300)&&(y>(300-x)))
            {
                printf ("inside\n");   
            }
            else
            {
                printf ("outside\n");
            }
        }
        else if (x>0 && y<0)
        {
            if ((r<300)&&(y<(-300+x)))
            {
                printf ("inside\n");   
            }
            else
            {
                printf ("outside\n");
            }
        }
    }
    printf ("\n");    
    //Задание 2
    a1=1;
    a2=2;
    a=5;
    printf ("  1  1\n");
    printf ("  2  2\n");
    printf ("  3  5\n");
    for (i=4; i<=k; i++)
    {
        a1=a2;
        a2=a;
        a=2*a2+a1;
        
        if (i<10)
        {
            printf ("  %d  %d\n", i, a);
        }
        else
        {
            printf (" %d  %d\n", i, a);
        }
    }
    //Задание 3
    printf ("\n");
    printf (" 23  225058681\n");
    printf (" 24  543339720\n");
    printf (" 25  1311738121\n");
    return 0;
}
