var findInMountainArray = function(target, mountainArr) {
    var start = 0;
    var end = mountainArr.length() - 1;
    var mid;
    while(start <= end){
        mid = Math.ceil((start + end) / 2);
        var b = mountainArr.get(mid);
        if( b > mountainArr.get(mid - 1) ){
            if( b > mountainArr.get(mid + 1) )
                break;
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }
    }
    var a = getIndex(mountainArr, 0, mid, 1, target);
    if( a === -1 ){
        return getIndex(mountainArr, mid, mountainArr.length() - 1, -1, target);
    }
    return a;
};

function getIndex(mountainArr, start, end, c, target){
    while(start <= end){
        var mid = Math.ceil((start + end) / 2);
        var a = mountainArr.get(mid);
        if( c * (a - target) === 0 ){
            return mid;
        }
        else if( c * (a - target) < 0 ){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }
    }
    return -1;
}
