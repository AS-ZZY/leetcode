function countDigits(num: number): number {
    return String(num).split("").reduce((v, i) => {
        if (num % Number(i) === 0) {
            return v + 1
        }
        return v
    }, 0)
};