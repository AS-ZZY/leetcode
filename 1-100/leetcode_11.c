#include <stdio.h>
#include <stdlib.h>
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

int maxArea(int* height, int heightSize) {
    int i = 0,j = heightSize - 1;
    int max = 0;
    while(i < j)
    {
        int a = height[i] > height[j] ? height[i] : height[j];
        if(max < a *(j - i))
            max = a *(j - i);
        if(height[i] < height[j])
            i++;
        else
            j--;
    }
    return max;
}



















