var treeToDoublyList = function(root) {
    if(!root) return null;
    let l = [];
    let p = root;
    let re = []
    while(re.length > 0 || p){
        if(p){
            re.push(p)
            p = p.left;
        }
        else{
            p = re[re.length - 1];
            re.pop();
            l.push(p)
            p = p.right;
        }
    }
    let max = 0;
    for(let i = 0;i < l.length; i++){
        if(l[max].val > l[i].val){
            max = i;
        }
        if(i == 0){
            l[i].left = l[l.length - 1];
            if(l.length === 1){
                l[i].right = l[i]
            }
            else{
                l[i].right = l[i + 1];
            }            
        }
        else if(i == l.length - 1){
            l[i].left = l[i - 1];
            l[i].right = l[0];
        }
        else{
            l[i].left = l[i - 1];
            l[i].right = l[i + 1];
        }
    }
    return l[max];
};