var maximum69Number = function (num) {
    const a = num.toString().split("");
    for (let i = 0; i < a.length; i++) {
        if (a[i] === "6") {
            a[i] = "9";
            break
        }
    }
    return a.join("")
};