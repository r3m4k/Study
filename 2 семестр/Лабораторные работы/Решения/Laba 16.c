/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int i;

int main()
{
    int n;
    scanf ("%d", &n);
    
    struct tMarks{
        int math;
        int phys;
        int inform;
    };
    struct tStudentCard{
        char surname[20];
        char name[10];
        int year;
        struct tMarks marks;
    } pearson[n];
    
    float average_mark[i];
    
    for (i=0; i<n; i++){
        average_mark[i]=(float)(pearson[i].marks.math+pearson[i].marks.phys+pearson[i].marks.inform)/3;
        scanf ("%s", pearson[i].surname);
        scanf ("%s", pearson[i].name);
        scanf ("%d", &pearson[i].year);
        scanf ("%d", &pearson[i].marks.math);
        scanf ("%d", &pearson[i].marks.phys);
        scanf ("%d", &pearson[i].marks.inform);
    }
    
    int min_1=100, n_min_1, min_2=100, n_min_2;
    
    for (i=0; i<n; i++){
        if (pearson[i].year==1){
            if (average_mark[i]<min_1){
                min_1=pearson[i].year;
                n_min_1=i;
            }
        }
        if (pearson[i].year==2){
            if (average_mark[i]<min_2){
                min_2=pearson[i].year;
                n_min_2=i;
            }
        }
    }
    
    for (i=0; i<n; i++){
        printf ("%15s", pearson[i].surname);
        printf ("%15s", pearson[i].name);
        printf ("%5d", pearson[i].year);
        printf ("%5d", pearson[i].marks.math);
        printf ("%5d", pearson[i].marks.phys);
        printf ("%5d", pearson[i].marks.inform); 
        printf ("\n");
    }
    printf ("\n");
    
    printf ("%s %s\n\n", pearson[min_1].surname, pearson[min_1].name);
    printf ("%s %s\n", pearson[min_2].surname, pearson[min_2].name);
    return 0;
}
