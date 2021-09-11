var calculate = function (s) {
    let ss = s.replace(" ", "");
    const l = [];
    const f = ["+", "-", "*", "/"];
    let start = 0;
    for (let i = 1; i < s.length; i++) {
        if (f.includes(s[i])) {
            l.push(Number(s.substring(start, i)))
            l.push(s[i])
            start = i + 1;
        }
    }
    l.push(Number(s.substring(start)))
    const re = [], stack1 = [], stack2 = [];
    for (let i = 0; i < l.length; i++) {
        if (typeof (l[i]) === "number") {
            stack1.push(l[i]);
        } else if (["-", "+"].includes(l[i])) {
            stack2.push(l[i]);
        } else if (l[i] === "*") {
            stack1.push(parseInt(stack1.pop() * l[i + 1], 10));
            i++;
        } else {
            stack1.push(parseInt(stack1.pop() / l[i + 1], 10));
            i++;
        }
    }
    let num = stack1[0];
    for (let i = 1; i < stack1.length; i++) {
        if (stack2[i - 1] === "+") {
            num += stack1[i];
        } else {
            num -= stack1[i]
        }
    }
    return num;
};