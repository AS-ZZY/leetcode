var maxSatisfied = function (customers, grumpy, minutes) {
    let sum = 0;
    for (let i = 0; i < customers.length; i++) {
        sum += customers[i] * (grumpy[i] === 1 ? 0 : 1);
    }
    let max = 0;
    for (let i = 0; i < customers.length; i++) {
        if (grumpy[i] === 1) {
            let t = customers[i];
            for (let j = 1; j < minutes; j++) {
                if (grumpy[i + j] === 1) {
                    t += customers[i + j];
                }
            }
            if (t > max) {
                max = t;
            }
        }
    }
    return sum + max
};