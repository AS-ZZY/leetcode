var numMovesStones = function(a, b, c) {
    if(b < a) {
        a = [b, b = a][0]
    }
    if(c < b) {
        c = [b, c = b][0];
    }
    if(b < a) {
        a = [b, b = a][0]
    }
    
    if(c-b==1 && b-a==1) return [0,  c-a-2];
    if(c-b<=2 || b-a<=2) return [1,  c-a-2];
    return [2,  c-a-2]; 
};