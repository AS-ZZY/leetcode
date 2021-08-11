var maximalSquare = function (matrix) {
    if (matrix.length === 0) {
        return 0;
    }
    const list = new Array(matrix.length);
    const min = (a, b, c) => {
        let d = a < b ? a : b;
        return d < c ? d : c;
    }
    let maxV = 0;
    for (let i = 0; i < matrix.length; i++) {
        list[i] = new Array(matrix[0].length).fill(0)
        if (matrix[i][0] === "1") {
            list[i][0] = 1;
            maxV = 1
        }
    }
    for (let i = 1; i < matrix[0].length; i++) {
        if (matrix[0][i] === "1") {
            list[0][i] = 1;
            maxV = 1
        }
    }
    for (let i = 1; i < matrix.length; i++) {
        for (let j = 1; j < matrix[0].length; j++) {
            if (matrix[i][j] === "1") {
                list[i][j] = min(list[i - 1][j], list[i][j - 1], list[i - 1][j - 1]) + 1;
                if (maxV < list[i][j]) {
                    maxV = list[i][j];
                }
            } else {
                list[i][j] = 0;
            }
        }
    }
    return maxV * maxV
};