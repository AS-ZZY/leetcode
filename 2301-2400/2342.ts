function maximumSum(nums: number[]): number {
  const obj = {}
  let max = -1
  nums.forEach((i) => {
    const sum = String(i).split("").reduce((v, i) => v + Number(i), 0)
    if (obj[sum]) {
      max = Math.max(max,  obj[sum] + i)
      obj[sum] = Math.max(i, obj[sum])
    } else {
      obj[sum] = i
    }
  })
  return max
};