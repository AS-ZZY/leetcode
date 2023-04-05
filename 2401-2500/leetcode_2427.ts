function commonFactors(a: number, b: number): number {
    let num = 0
    const min = Math.min(a, b)
    const max = Math.max(a, b)
    for (let i = 1;i <= Math.pow(min, 0.5); i += 1) {
        if (min % i === 0) {
            if (max % i === 0) {
                num += 1
            }
            if (max % (min / i) === 0 && i * i !== min) {
                num += 1
            }
        }
    }
    return num
};