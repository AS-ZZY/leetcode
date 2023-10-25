var createCounter = function(n) {
    var flag = n
    return function() {
        return flag++
    };
};