var dailyTemperatures = function(T) {
    let list = [0];
    let stack = [ T.length - 1 ];
    for(let i = T.length - 2; i >= 0; i--){
        while(stack.length > 0){
            if(T[stack[0]] < T[i]){
                stack.shift();
            }
            else if(T[stack[0]] == T[i]){
                if(stack.length > 1){
                    list.unshift(stack[1] - i);
                }
                else{
                    list.unshift(0);
                }
                stack[0] = i;
                break
            }
            else{
                list.unshift(stack[0] - i);
                stack.unshift(i);
                break
            }
        }
        if(stack.length === 0){
            stack.push(i);
            list.unshift(0);
        }
    }
    return list;
};