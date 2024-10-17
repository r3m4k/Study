/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

struct tAdress{
        char town[20];
        char street[15];
        int home_num;
        int flat_num;
    };
    struct tPearsonCard{
        char surname[15];
        char name[10];
        struct tAdress adress;
        char sport[10];
        int score;
    };
    
void func_filling_struct (struct tPearsonCard *a, int n);
int func_sort_sport (struct tPearsonCard *a, int n, char **sport);

int main()
{
    int n=24; //Количество участников в полуфинале
    //scanf ("%d", &n);
    struct tPearsonCard pearson [24]={
        {"Ivanov", "Ivan", {"Moscow", "Kashirskaya", rand()%99+1, rand()%249+1}, "Boxing", rand()%49+50},
        {"Shirokiy", "Artem", {"Saint-Peterburg", "Sadovaya", rand()%99+1, rand()%249+1}, "Boxing", rand()%49+50},
        {"Smyslov", "Vsevolod", {"Kaliningrad", "Lenina", rand()%99+1, rand()%249+1}, "Boxing", rand()%49+50},
        {"Voronkov", "Nikita", {"Ekaterinburg", "Okskaya", rand()%99+1, rand()%249+1}, "Boxing", rand()%49+50},
        {"Galeev", "Tamirlan", {"Kaliningrad", "Kashirskaya", rand()%99+1, rand()%249+1}, "Boxing", rand()%49+50},
        
        {"Sidorov", "Alexsandr", {"Saint-Peterburg", "Nevskiy", rand()%99+1, rand()%249+1}, "Sprint", rand()%49+50},
        {"Melnikov", "Denis", {"Moscow", "Lenina", rand()%99+1, rand()%249+1}, "Sprint", rand()%49+50},
        {"Dadyshina", "Darya", {"Ekaterinburg", "Lovaya", rand()%99+1, rand()%249+1}, "Sprint", rand()%49+50},
        {"Deygrosh", "Danila", {"Saint-Peterburg", "Dal'nyay", rand()%99+1, rand()%249+1}, "Sprint", rand()%49+50},
        {"Tarasov", "Igor", {"Omsk", "Dnevnaya", rand()%99+1, rand()%249+1}, "Sprint", rand()%49+50},
        {"Golodnyak", "Alexsandr", {"Kaliningrad", "Romanovskaya", rand()%99+1, rand()%249+1}, "Sprint", rand()%49+50},
        
        {"Ytkina", "Irina", {"Ekaterinburg", "Gagarina", rand()%99+1, rand()%249+1}, "Tennis", rand()%49+50},
        {"Gribcov", "Alexsandr", {"Saint-Peterburg", "Nevskiy", rand()%99+1, rand()%249+1}, "Tennis", rand()%49+50},
        {"Merdeev", "Ilmar", {"Kaliningrad", "Lublino", rand()%99+1, rand()%249+1}, "Tennis", rand()%49+50},
        {"Socolov", "Andey", {"Moscow", "Shovrino", rand()%99+1, rand()%249+1}, "Tennis", rand()%49+50},
        {"Bastencov", "Danila", {"Saint-Peterburg", "Rubnaya", rand()%99+1, rand()%249+1}, "Tennis", rand()%49+50},
        {"Kalinina", "Elisaveta", {"Vladivostok", "Klinskaya", rand()%99+1, rand()%249+1}, "Tennis", rand()%49+50},
        {"Lebedev", "Nicolay", {"Moscow", "Artilleriskaya", rand()%99+1, rand()%249+1}, "Tennis", rand()%49+50},
        
        {"Nesterenco", "Maxim", {"Saint-Peterburg", "Vostochnaya", rand()%99+1, rand()%249+1}, "Fencing", rand()%49+50},
        {"Kim", "Pavel", {"Moscow", "Gagarina", rand()%99+1, rand()%249+1}, "Fencing", rand()%49+50},
        {"Semenov", "Andey", {"Omsk", "Lenina", rand()%99+1, rand()%249+1}, "Fencing", rand()%49+50},
        {"Romanovskiy", "Roman", {"Saint-Peterburg", "Merdeeva", rand()%99+1, rand()%249+1}, "Fencing", rand()%49+50},
        {"Makey", "Artem", {"Ykutsk", "Vernandscog", rand()%99+1, rand()%249+1}, "Fencing", rand()%49+50},
        {"Gan", "Evgeniy", {"Moscow", "Arbat", rand()%99+1, rand()%249+1}, "Fencing", rand()%49+50}
    };
    struct tPearsonCard *arp[n];
    
    for (i=0; i<n; i++)
        arp[i]=&pearson[i];
    
    //func_filling_struct (*arp, n);

    char *sport;
    sport=(char*)calloc(n, sizeof(char));
    if (sport==NULL)
        exit (EXIT_FAILURE);
    int k = func_sort_sport (*arp, n, &sport);
    for (i=0; i<n; i++){
        printf ("%15s %9s %16s %14s %3d %4d %9s %2d\n", pearson[i].surname, pearson[i].name, pearson[i].adress.town, 
        pearson[i].adress.street, pearson[i].adress.home_num, pearson[i].adress.flat_num, pearson[i].sport, pearson[i].score);
    }
    int q;  //Число финалистов
    //printf ("Введите число финалистов: ");
    //scanf ("%d", &q);
    q=2;
    int j, f=0, s=0, t;
    char word[10];
    //1 пункт
    for (i=0; i<k; i++){
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i])
                s+=1;
        }
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i]){
                for (f=0; f<10; f++)
                    word[f]=pearson[j].sport[f];
                    break;
            }
        }
        f=0;
        int arr[s];     //Массив очков участников
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i]){
                arr[f]=pearson[j].score;
                f+=1;
            }
        }
        //Сортировка
        for (f=0; f<s; f++){    
            for (j=0; j<s-f-1; j++){
                if (arr[j]<arr[j+1]){
                    t=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
            }
        } 
        printf ("%s %d\n", word, arr[q-1]);
        s=0; f=0;
        
    }
    printf ("\n");
    //2 пункт
    for (i=0; i<k; i++){
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i])
                s+=1;
        }
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i]){
                for (f=0; f<10; f++)
                    word[f]=pearson[j].sport[f];
                    break;
            }
        }
        f=0;
        int arr[s];     //Массив очков участников
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i]){
                arr[f]=pearson[j].score;
                f+=1;
            }
        }
        //Сортировка
        for (f=0; f<s; f++){    
            for (j=0; j<s-f-1; j++){
                if (arr[j]<arr[j+1]){
                    t=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
            }
        } 
        printf ("%s\n", word);
        for (j=0; j<n; j++){
            if ((pearson[j].sport[0]==sport[i])&&(pearson[j].score>=arr[q-1]))
                printf (" %s\n", pearson[j].surname);
        }
        s=0; f=0;
    }
    printf ("\n");
    //3 пункт
    char town[n];
    int l=0, total=0;
    for (i=0; i<k; i++){
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i]){
                s+=1;
            }
        }
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i]){
                for (f=0; f<10; f++)
                    word[f]=pearson[j].sport[f];
                    break;
            }
        }
        f=0;
        int arr[s];     //Массив очков участников
        for (j=0; j<n; j++){
            if (pearson[j].sport[0]==sport[i]){
                arr[f]=pearson[j].score;
                f+=1;
            }
        }
        //Сортировка
        for (f=0; f<s; f++){    
            for (j=0; j<s-f-1; j++){
                if (arr[j]<arr[j+1]){
                    t=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
            }
        } 
        for (j=0; j<n; j++){
            if ((pearson[j].sport[0]==sport[i])&&(pearson[j].score>=arr[q-1])){
                town[l]=pearson[j].adress.town[0];
                l+=1;
            }
        }
        total+=q;
        s=0; f=0;
    }

    for (i=0; i<total; i++){
        for (j=0; j<total-i-1; j++){
            if (town[j]>town[j+1]){
            t=town[j];
            town[j]=town[j+1];
            town[j+1]=t;
            }
        }
    }   
    int k_t=total;
    for (i=0; i<total-1; i++){
        if (town[i]==town[i+1])
            k_t-=1;
    }
    printf ("%d\n", k_t);
    return 0;
}

void func_filling_struct (struct tPearsonCard *a, int n){
    for (i=0; i<n; i++){
        scanf ("%s", (a[i]).surname);
        scanf ("%s", (a[i]).name);
        scanf ("%s", (a[i]).adress.town);
        scanf ("%s", (a[i]).adress.street);
        scanf ("%d", &(a[i]).adress.home_num);
        scanf ("%d", &(a[i]).adress.flat_num);
        scanf ("%s", (a[i]).sport);
        scanf ("%d", &(a[i]).score);
    }
}

int func_sort_sport (struct tPearsonCard *a, int n, char **sport){
    char p[n];
    for (i=0; i<n; i++)
        p[i]=(a[i]).sport[0];
    int j, t;     //Сортировка
    for (i=0; i<n; i++){
        for (j=0; j<n-i-1; j++){
            if (p[j]>p[j+1]){
            t=p[j];
            p[j]=p[j+1];
            p[j+1]=t;
            }
        }
    }   
    
    int k=n;
    for (i=0; i<n-1; i++){
        if (p[i]==p[i+1])
            k-=1;
    }
    
    (*sport)[0]=p[0];
    j=1;
    for (i=1; i<n; i++){
        if (p[i]!=p[i-1]){
            (*sport)[j]=p[i];
            j+=1;
        }
    }
    (*sport)=(char*)realloc(*sport, j*sizeof(char));
    
    return j;
}






