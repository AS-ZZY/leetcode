
var MinStack = function() {
    this.list = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.list.push(val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.list.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.list[this.list.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    let min = this.list[0]
    for(let i = 1;i < this.list.length;i++) {
        if(min > this.list[i]) {
            min = this.list[i]
        }
    }
    return min
};
