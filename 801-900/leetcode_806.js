var numberOfLines = function (widths, s) {
    let line = 1;
    let num = 0;
    let a = "a".charCodeAt();
    for (let i = 0; i < s.length; i++) {
        if (num + widths[s[i].charCodeAt() - a] > 100) {
            line += 1;
            num = widths[s[i].charCodeAt() - a];
        } else {
            num += widths[s[i].charCodeAt() - a];
        }
    }
    return [line, num]
};