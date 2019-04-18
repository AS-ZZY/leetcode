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
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int i,*j,k;
    i = digitsSize - 1;
    digits[i]++;
    if(digits[i] >= 10)
        for(;i > 0;i--)
        {
            if(digits[i] >= 0)
            {
                digits[i] -= 10;
                digits[i - 1]++;
            }
            else
                break;
        }
    if(digits[0] == 10)
    {
        j = (int*)malloc(sizeof(int) * (digitsSize + 1));
        *returnSize = digitsSize + 1;
        j[0] = 1;
        digits[0] = 0;
        k = 1;
    }
    else
    {
        j = (int*)malloc(sizeof(int) * (digitsSize));
        *returnSize = digitsSize;
        k = 0;
    }
    for(i = 0;i < digitsSize;k++,i++)
        j[k] = digits[i];
    return j;
}

