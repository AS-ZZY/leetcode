var findRestaurant = function (list1, list2) {
    const obj = {};
    let min = Infinity;
    let re = [];
    const getRe = (item, index) => {
        if (obj[item] !== undefined) {
            obj[item] += index
            if (min > obj[item]) {
                min = obj[item]
                re = [item]
            } else if (min === obj[item]) {
                re.push(item)
            }
        } else {
            obj[item] = index
        }
    }
    list1.forEach(getRe);
    list2.forEach(getRe);
    return re
};