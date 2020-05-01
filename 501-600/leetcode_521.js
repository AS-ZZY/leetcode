var findLUSlength = function(a, b) {
    if(a.length !== b.length){
        return a.length > b.length ? a.length : b.length;
    }
    for(var i = 0;i < a.length;i++){
        if(a[i] !== b[i]){
            return a.length;
        }
    }
    return -1;
};