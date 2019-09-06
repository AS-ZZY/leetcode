int singleNumber(int* nums, int numsSize) {
    int i,j,l,time;
    for(i=0;i<numsSize;i++)
    {
        time=0;
    	for(j=i+1;j<numsSize;j++)
    	{
		if(nums[i]==nums[j])
    		{
    			l=nums[i+1];
				nums[i+1]=nums[j];
				nums[j]=l;
				time++;
				i++;
                if(time==2)
                    break;
            } 	
		}
        if(time==0)
			break;
	}
	return nums[i];
}
