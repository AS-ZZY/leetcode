class NumArray {
  private arr: number[]

  constructor(nums: number[]) {
    this.arr = nums
  }

  update(index: number, val: number): void {
    this.arr[index] = val
  }

  sumRange(left: number, right: number): number {
    let sums = 0
    for(let i = left; i <= right; i++) {
      sums += this.arr[i]
    }
    return sums
  }
}