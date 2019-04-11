#include <stdio.h>
#include <stdlib.h>
int main()
{
    return 0;
}
void reverseString(char* s, int sSize) {
    int i = 0,j = sSize - 1;
    char a;
    while(i < j)
    {
        a = s[i];
        s[i] = s[j];
        s[j] = a;
        i++;
        j--;
    }
}
