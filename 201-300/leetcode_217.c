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

bool containsDuplicate(int* nums, int numsSize) {
    int n = numsSize;
    if(n<2)
        return false;
    for(int i=0;i<n;i++){
         for(int j=i-1;j>-1;j--){
            if(nums[i]>nums[j])
                break;
            if(nums[i]==nums[j])
                return true;
        }

    }
   return false;
}

