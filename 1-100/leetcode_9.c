#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int main()
{
    return 0;
}

bool isPalindrome(int x) {
    int s[15];
    int i = 0;
    if(x < 0)
        return false;
    for(;x > 0;i++)
    {
        s[i] = x % 10;
        x = x / 10;
    }
    int j;
    for(j = 0,i--;j < i;i--,j++)
    {
        if(s[i] != s[j])
            return false;
    }
    return true;
}

