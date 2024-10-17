/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

struct _train_info{
    char town_departure [15];
    char town_arrival [15];
    int train_num;
    int distance;
    int average_speed;
    int quant_of_stops;
};

void func_print (struct _train_info *a, int n);
void func_filling_struct (struct _train_info *a, int n);
int func_travel_time (struct _train_info *a, int index);

int main()
{
    int n=10;
    //scanf ("%d", &n);
    //func_filling_struct (struct tPearsonCard *a, int n);
    struct _train_info Train_info [10] = {
        {"Moskow", "Adler", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Ekaterinburg", "Adler", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Moskow", "Ekaterinburg", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Peterburg", "Moskow", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Kaliningrad", "Moskow", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Moskow", "Omsk", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Moskow", "Peterburg", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Omsk", "Tyla", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Tyla", "Vladivostok", rand()%999+1, rand()%1000+1000, rand()%40+50, rand()%29+1},
        {"Moskow", "Vladivostok", rand()%999+1, rand()%1000+3000, rand()%40+50, rand()%29+1}
    };
        
    func_print (Train_info, n);
    int result, flag=0, value, result_index;
    for (i=0; i<n; i++){
        if ((Train_info[i]).town_departure[0] == 'M'){
            value = func_travel_time(Train_info, i);
            printf ("%s %s %d - %d\n", (Train_info[i]).town_departure, (Train_info[i]).town_arrival, 
                (Train_info[i]).train_num, value);
            if (flag == 0){
                result = value;
                flag++;
            }
            if (result > value){
                result = value;
                result_index = i;
            }
        }
    }
    
    printf ("\n%s %s %d\n", (Train_info[result_index]).town_departure, 
        (Train_info[result_index]).town_arrival, (Train_info[result_index]).train_num);
    return 0;
}

void func_print (struct _train_info *a, int n){
    for (i=0; i<n; i++)
        printf ("%15s %14s %4d %4d %4d %4d\n", (a[i]).town_departure, (a[i]).town_arrival, (a[i]).train_num,
            (a[i]).distance, (a[i]).average_speed, (a[i]).quant_of_stops);
    printf ("\n");
}

int func_travel_time (struct _train_info *a, int index){
    return ((a[index]).distance/(a[index]).average_speed + 10*(a[index]).quant_of_stops);
}

void func_filling_struct (struct _train_info *a, int n){
    for (i=0; i<n; i++){
        scanf ("%s", (a[i]).town_departure);
        scanf ("%s", (a[i]).town_arrival);
        scanf ("%d", &(a[i]).train_num);
        scanf ("%d", &(a[i]).distance);
        scanf ("%d", &(a[i]).average_speed);
        scanf ("%d", &(a[i]).quant_of_stops);
    }
}




