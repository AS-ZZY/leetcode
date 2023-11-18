function longestAlternatingSubarray(nums: number[], threshold: number): number {
  if (nums.length === 0) {
    return 0
  }
  let last = 0
  let max = last
  for (let i = 0;i < nums.length;i++) {
    let re = 0
    if (nums[i] > threshold) {
      re = 0
    } else if (last === 0) {
      if (nums[i] % 2 === 0) {
        re = 1
      }
    } else {
      re = nums[i - 1] % 2 === nums[i] % 2 ? (nums[i] % 2 === 0 ? 1 : 0) : last + 1
    }
    max = Math.max(re, max)
    last = re
  }
  return max
};