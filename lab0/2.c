#include <stdio.h>
#include <string.h>

int main() {
int l=1;
int N=3;
int tab[]={1,2,3}; //tablica -> int tab[N]
int *a=&l;
printf("L=%i\n",l);
printf("A=%p\n",a);
printf("sL=%li\n",sizeof(l));
printf("sA=%li\n",sizeof(a));
printf("Rozmiar tablicy = %i\n",sizeof(tab));
printf("Rozmiar int = %i\n",sizeof(int));
printf("Rozmiar tab+int = %i\n",sizeof(int)+sizeof(tab));
memcpy(tab,tab,sizeof(tab)); //?

tab[3]=4; //*(tab+3)=4;
printf("%i\n",tab[3]);
N=sizeof(tab)/sizeof(int)+1;
for(int i=0;i<N;i++) {
 printf("%i\n",tab[i]); //*(tab+i)
}
return 0;
}