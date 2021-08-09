var removeOuterParentheses = function (s) {
    let start = 0;
    let re = "";
    let times = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] == "(") {
            times++;
        } else {
            times--;
            if (times == 0) {
                re += s.substring(start + 1, i);
                start = i + 1;
            }
        }
    }
    return re
};