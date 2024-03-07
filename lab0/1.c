#include <stdio.h>
#include <string.h> //!

int main() {
int a=1;
float b=1.1;
char c[]="Lab."; //5->'\0'
printf("Wynik=%f\n",a+b); //?
printf("Wynik=%f\n",a+b);
strcat(c,"1");
printf("Tekst=%s\n",c);
printf("L=%i\n",strlen(c));
for (int i=0; c[i]!='\0'; i++) {
printf("%c",c[i]);
}
return 0;
}
