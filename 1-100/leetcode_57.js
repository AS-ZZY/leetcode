var insert = function (intervals, newInterval) {
    const max = (a, b) => (a > b ? a : b);
    const min = (a, b) => (a < b ? a : b);
    let l = newInterval;
    let t = false
    const re = intervals.reduce((list, item) => {
        if (item[0] > l[1]) {
            if (!t) { list.push(l) }
            t = true
            list.push(item)
        } else if (item[1] < l[0]) {
            list.push(item);
        } else {
            l = [min(item[0], l[0]), max(item[1], l[1])]
        }
        return list;
    }, [])
    if (!t) { re.push(l) };
    return re
};