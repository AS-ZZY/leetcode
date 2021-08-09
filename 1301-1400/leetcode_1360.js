var daysBetweenDates = function (date1, date2) {
    const d = new Date(date1) - new Date(date2);
    const re = parseInt(d / 1000 / 60 / 60 / 24, 10)
    return re > 0 ? re : -re;
};