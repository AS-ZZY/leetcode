function prevPermOpt1(arr: number[]): number[] {
  let end = arr.length - 2
  for (; end >= 0; end -= 1) {
    if (arr[end] > arr[end + 1]) {
      break
    }
  }
  if (end < 0) {
    return arr
  }
  let nearest = end + 1
  for (let i = end + 1; i < arr.length; i += 1) {
    if (arr[i] >= arr[end]) {
      break
    }
    if (arr[i] !== arr[i - 1]) {
      nearest = i
    }
  }
  let a = arr[nearest]
  arr[nearest] = arr[end]
  arr[end] = a
  return arr
};