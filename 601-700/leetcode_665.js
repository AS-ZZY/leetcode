var checkPossibility = function(nums) {
    if(nums.length <= 2){
        return true;
    }
    let small = false;
    for(let i = 1; i < nums.length - 1; i++ ){
        if(nums[i] > nums[i + 1]){
            if(small){
                return false;
            }
            if(nums[i + 1] >= nums[i - 1]){
                nums[i] = nums[i + 1];small = true;
            }
            else{
                nums[i + 1] = nums[i];
                small = true;
            }
        }
    }
    if(nums[0] > nums[1] && small){
        return false;
    }
    if(nums[nums.length - 1] < nums[nums.length - 2] && small){
        return false;
    }
    return true;
};