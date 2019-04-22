#include <stdio.h>
#include <stdlib.h>
#define bool int
#define false 0
#define true 1
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct ListNode {
    int val;
    struct ListNode *next;
 };
int main()
{
    return 0;
}
char findTheDifference(char* s, char* t) {
    int i = 0,j = 0;
    int l = strlen(s);
    for(;i < l;i++)
    {
        j = j ^ (int)s[i] ^ (int)t[i];
    }
    j = j ^ (int)t[i];
    return (char)j;
}






