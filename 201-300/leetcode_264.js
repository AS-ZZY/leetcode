var nthUglyNumber = function(n) {
    var l = [1];
    var id2 = 0, id5 = 0, id3 = 0;
    for(var i = 1;i < n;i++){
        var j = Math.min(l[id2] * 2, Math.min(l[id3] * 3, l[id5] * 5));
        l.push(j)
        if(j === l[id2] * 2){
            id2++;
        }
        if(j === l[id3] * 3){
            id3++;
        }
        if(j === l[id5] * 5) {
            id5++;
        }
    }
    return l[l.length - 1];
};