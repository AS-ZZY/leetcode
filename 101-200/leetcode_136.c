int singleNumber(int* nums, int numsSize) {
    int i,j = 0;
    for(i = 0;i < numsSize;i++)
        j ^= nums[i];
    return j;
}
