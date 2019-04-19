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
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    int i, len = 0, j = 0;
    for(i=0; i<numsSize; i++){
        nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1]);
    }
    for(i=0; i<numsSize; i++){
        if(nums[i] > 0)
            len++;
    }
    int *res = malloc(sizeof(int) * len);
    if(!res)
        return NULL;
    *returnSize = len;
    for(i=0; i<numsSize; i++){
        if(nums[i] > 0)
            res[j++] = i + 1;
    }
    return res;
}

















