var verifyPostorder = function(postorder) {
    if(postorder.length === 0){
        return true;
    }
    let root = postorder[postorder.length - 1];
    let i = 0;
    for(;i < postorder.length - 1; i++){
        if(postorder[i] > root){
            break
        }
    }
    for(let j = i; j < postorder.length - 1; j++){
        if(postorder[j] < root){
            return false
        }
    }
    return verifyPostorder(postorder.slice(0, i)) && verifyPostorder(postorder.slice(i, j))
};