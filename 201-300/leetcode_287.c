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
int findDuplicate(int* nums, int numsSize) {
    int i = 0,j = 0;
    do{
        j = nums[nums[j]];
        i = nums[i];
    }while(i != j);
    i = 0;
    do{
        i = nums[i];
        j = nums[j];
    }while(i != j);
    return i;
}





