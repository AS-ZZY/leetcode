var getDecimalValue = function(head) {
    let a = 0;
    while(head){
        a = a * 2 + head.val;
        head = head.next;
    }
    return a;
};