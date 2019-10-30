int search(int* nums, int numsSize, int target) {
    int frist = 0,last = numsSize - 1;
    int mid;
    while(frist <= last)
    {
        mid = (frist + last) / 2;
        if(nums[mid] == target)
            return mid;
        if(nums[frist] <= nums[last])
        {
            if(nums[mid] < target)
                frist = mid + 1;
            else
                last = mid - 1;
        }
        else
        {
            if(nums[frist] <= nums[mid])
            {
                if(target < nums[frist]||target > nums[mid])
                    frist = mid + 1;
                else
                    last = mid - 1;
            }
            else
            {
                if(nums[mid] < target&&nums[last] >= target)
                    frist = mid + 1;
                else
                    last = mid - 1;
            }
        }
    }
    return -1;
}
