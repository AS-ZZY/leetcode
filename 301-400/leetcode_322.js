var coinChange = function(coins, amount) {
    let list = Array(amount).fill(-1);
    for(let i = 0; i < amount; i++){
        let itemList = [];
        for(let j in coins){
            if(i + 1 === coins[j]){
                itemList = [1];
                break;
            }
            if(i + 1 > coins[j]){
                itemList.push(1 + list[i + 1 - coins[j]])
            }
        }
        if(itemList.length === 0){
            list[i] = -1
        }
        else{
            list[i] = Math.max(itemList);
        }
    }
    return list[amount - 1];
};