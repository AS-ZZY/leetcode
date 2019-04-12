#include <stdio.h>
#include <stdlib.h>
int main()
{
    return 0;
}
void moveZeroes(int* nums, int numsSize) {
    int i = 0,j = 0;
    for(;i < numsSize;i++)
    {
        if(nums[i] != 0)
            nums[j++] = nums[i];
    }
    for(;j < numsSize;j++)
        nums[j] = 0;
}
