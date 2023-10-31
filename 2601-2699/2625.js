var flat = function (arr, n) {
    if (n === 0) {
        return arr
    } else {
        let res = [], k = 0
        arr.forEach(item => {
            if (Array.isArray(item)) {
                for (let num of flat(item, n - 1)) {
                    res[k++] = num
                }
            } else {
                res[k++] = item
            }
        })
        return res
    }
};
