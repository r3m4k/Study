#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m[40], p[40], k, max=0, 
        i, j, f;
    for (i=0; i<13; i++){
        scanf ("%d", &m[i]);
        p[i]=1;
    }    
    
    for (j=39; j>-1; j--){
        for (f=j-1; f>-1; f--){
            if (m[j]==m[f])
                p[j]+=1;
        }
    }

    for (i=0; i<40; i++){
        if (p[i]>max)
            max=p[i];
    }
    
    for (i=0; i<40; i++){
        if (p[i]==max)
            k+=1;
    }
    printf ("%d\n", k);
    for (i=0; i<40; i++){
        if (p[i]==max)
            printf ("%d ", m[i]);
    }
    return 0;
}
