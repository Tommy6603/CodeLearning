#include <stdio.h>
int main(void){
    char str[1000];
    printf("input any characters:");
    fgets(str, sizeof(str), stdin);
    printf("%s", str);
    return 0;
}