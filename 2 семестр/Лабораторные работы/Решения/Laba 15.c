/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i, j;

void func_zero (int a[], int k);

int main()
{
    int n, m;
    scanf ("%d %d", &n, &m);
    int arr_first[n][m];
    for (i=0; i<n; i++){
        for (j=0; j<m; j++){
            //arr[i][j]=rand()%19+1;
            scanf ("%d", &arr_first[i][j]);
        }
    }
    
    int arr[n][m];
    for (i=0; i<n; i++){
        if (i%2==0){
            for (j=0; j<m; j++){
                arr[i][j]=arr_first[i][j];
            }
        }
        if (i%2==1){
            for (j=0; j<n; j++){
                arr[i][j]=arr_first[i][n-1-j];
            }
        }
    }
    for (i=0; i<n; i++){
        for (j=0; j<m; j++){
            printf ("%3d", arr[i][j]);
        }
        printf ("\n");
    }    
    printf ("\n");
    
    int sum[n];
    func_zero (sum, n);
    for (i=0; i<n; i++){
        for (j=0; j<m; j++){
            sum[i]+=arr[i][j];
        }
    }
    int max_sum, k=1;
    max_sum=sum[0];
    for (i=1; i<n; i++){
        if (max_sum<sum[i]){
            max_sum=sum[i];
            k=i+1;
        }
    }
    printf ("%d\n", k);

    int min, max, q, h, f, s;
    f = 0;
    s = 0;
    for(i=0; i<n; i++){
        for(j=0; j<m; j++){
            if(j==0){
                min=arr[i][j];
                q=j;
            }
            if(arr[i][j] < min){
                min =arr[i][j];
                q = j;
            }
        }
        for(h = 0; h < n; h++){
            if(h == 0){
            max = arr[h][q];
            }
            if(arr[h][q]>max){
                max =arr[h][q];
            }
        }
        if (min == max){
            f = 1;
            break;
        }
    }
    if(f == 1){
        for(i = 0;i < n; i++){
            for(j = 0;j < m; j++){
                if(arr[i][j] == min){
                    s++;
                }
            }
        }
        if(s == 1){
            printf("%d", min);
        }
        else{
            printf("%d %d", min, s);
        }
    }
    else{
        printf("-");
    }
    printf("\n");
        
    return 0;
}

void func_zero (int a[], int k){
    int i;
    for (i=0; i<k; i++)
        a[i]=0;
}
