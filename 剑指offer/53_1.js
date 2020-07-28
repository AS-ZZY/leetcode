var search = function(nums, target) {
    let start = 0, end = nums.length - 1;
    let tstart, tend;
    while( start <= end ){
        let mid = Math.floor((start + end) / 2);
        if(nums[mid] < target){
            start = mid + 1;
        }
        else if(nums[mid] === target && (mid === 0 || nums[mid - 1] < target)){
            tstart = mid;
            break
        }
        else{
            end = mid - 1;
        }
    }
    if(typeof(tstart) === "undefined"){
        return 0;
    }
    start = 0;
    end = nums.length - 1;
    while( start <= end ){
        let mid = Math.floor((start + end) / 2);
        if(nums[mid] > target){
            end = mid - 1;
        }
        else if(nums[mid] === target && (mid === nums.length - 1 || nums[mid + 1] > target)){
            tend = mid;
            break
        }
        else{
            start = mid + 1;
        }
    }
    return tend - tstart + 1;
};

l = [1,8,8,9]
n = 1

console.log(search(l, n))