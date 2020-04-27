var distributeCandies = function(candies) {
    var l = Array.from(new Set(candies));
    if (l.length >= candies.length / 2){
        return candies.length / 2;
    }
    return l.length
};