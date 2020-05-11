var letterCasePermutation = function(S) {
    var l = [""];
    for(var i in S){
        l = getString(S[i], l);
    }
    return l;
};

var getString = function(val, l){
    var list = [];
    var re = /^[0-9]/;
    if(re.test(val)){
        for(var i in l){
            list.push(l[i] + val);
        }
    }
    else{
        for(var i in l){
            list.push(l[i] + val.toUpperCase());
            list.push(l[i] + val.toLowerCase());
        }
    }
    return list;
}