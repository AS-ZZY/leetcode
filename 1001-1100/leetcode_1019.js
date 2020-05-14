var nextLargerNodes = function(head) {  
    var l = new ListNode(0);
    l.next = null;
    var p = head;
    while(p){
        var q = p.next;
        p.next = l.next;
        l.next = p;
        p = q;
    }
    const stack = [];
    const re = [];
    p = l.next;
    while(p){
        while(stack.length !== 0){
            if(stack[stack.length - 1] > p.val){
                break;
            }
            stack.pop();
        }
        if(stack.length === 0){
            re.unshift(0);
        }
        else{
            re.unshift(stack[stack.length - 1]);
        }
        stack.push(p.val);
        p = p.next;
    }
    return re;
};