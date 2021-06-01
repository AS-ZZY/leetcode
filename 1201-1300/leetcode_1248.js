var numberOfSubarrays = function(nums, k) {
    var num = 0; 
    var odd = [-1];
    for(var i = 0;i < nums.length; i++){
        if(nums[i] % 2 === 1){
            odd.push(i)
        }
    }
    odd.push(nums.length);
    if(odd.length- 2 < k){
        return 0;
    }
    for(var i = 1;i + k < odd.length;i++){
        num = num + (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
    }
    return num;
};