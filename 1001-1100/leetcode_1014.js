var maxScoreSightseeingPair = function(A) {
    let maxLeft = Number.NEGATIVE_INFINITY;
    let max = Number.NEGATIVE_INFINITY;
    for(let i = 0; i < A.length;i++) {
        if(max < A[i] - i + maxLeft){
            max = A[i] - i + maxLeft
        }
        if(A[i] + i > maxLeft){
            maxLeft = A[i] + i;
        }
    }
    return max;
};