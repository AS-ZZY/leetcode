var maxCount = function(m, n, ops) {
    var minx = m;
    var miny = n;
    for(var i = 0; i < ops.length; i++){
        if( ops[i][0] < minx ){
            minx = ops[i][0]
        }
        if( ops[i][1] < miny ){
            miny = ops[i][1]
        }
    }
    return minx * miny;
};