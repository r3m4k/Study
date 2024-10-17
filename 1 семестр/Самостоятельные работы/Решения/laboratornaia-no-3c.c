/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
     int i, j, q, z, k, c, a, b;
     const long int m = 2147483647;
     scanf("%d", &k);
    
     printf ("9\n");
     printf("\n");
     
     a=1;
    c=0;
    z=1;
 while(a!=0){
     b=2*a-1;
     z=b;
     for(j=2; j<=k; j=j+1){
         if(m/z>b)
         b=b*z;
         else{
         printf("%d\n", c);
         printf("%d\n", a-1);
         printf("*\n");
         goto fuck;
         }
     }
     
     if(m-b>c)
     c=c+b;
     else 
     break;
    
    a=a+1;
 }
 a-=1;
 printf("%d\n", c);
 printf("%d\n", a);
 printf("+\n");
 fuck: 

    return 0;
}