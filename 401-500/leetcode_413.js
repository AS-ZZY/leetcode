var numberOfArithmeticSlices = function (nums) {
    const getV = (v) => {
        let a = 0;
        for (let i = 1; i <= v - 2; i++) {
            a += i;
        }
        return a
    }
    if (nums.length === 0) {
        return 0;
    }
    let num = 0, start = 0, re = nums[1] - nums[0];
    for (let i = 1; i < nums.length; i++) {
        const res = nums[i] - nums[i - 1];
        if (res !== re) {
            if (i - start >= 3) {
                num += getV(i - start)
            }
            re = res;
            start = i - 1;
        }
    }
    if (nums.length - start >= 3) {
        num += getV(nums.length - start)
    }
    return num
};