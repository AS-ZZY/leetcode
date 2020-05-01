var mergeKLists = function(lists) {
    var l = new ListNode(0);
    var s = l;
    while(true){
        frist = true;
        var min;
        for(var i = 0; i < lists.length;i++){
            if(lists[i]){
                if(frist){
                    frist = false;
                    min = i;
                }
                else if(lists[min].val > lists[i].val){
                    min = i;
                }
            }
        }
        if(frist){
            return l.next;
        }
        s.next = lists[min];
        s = s.next;
        lists[min] = lists[min].next;
    }
};