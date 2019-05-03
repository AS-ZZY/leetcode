import os


def num_(path):
    if os.path.exists(path):
        count = 0
        for root, dirs, files in os.walk(path):
            for _ in files:
                count += 1
        a = 13 - len(path.split("\\")[-1])
        print(path.split("\\")[-1] + " " * a + str(count))
        return count
    else:
        return 0


def clear():
    os.system('cls')


def num__(path):
    sum_ = 0
    for i in range(11):
        path_ = str(i) + "01-" + str(i + 1) + "00"
        path_all = path + path_
        sum_ +=  num_(path_all)
    print("sum" + " " * 10 + str(sum_))


def _input():
    while True:
        a = input("输入题号：")
        try:
            a = int(a)
            break
        except Exception:
            clear()
            a = 'c'
            break
    return a


def find_dir(x, path):
    i = 0
    while 100 * i + 1 > x or x > 100 * (i + 1):
        i += 1
        if i == 15:
            return False, ""
    if i == 0:
        st = "001"
    else:
        st = str(100 * i + 1)
    path_ = path + st + "-" + str(100 * (i + 1))
    return True, path_


def find_fil(x, path):
    if not os.path.exists(path):
        return False, ""
    list_ = os.listdir(path)
    for i in list_:
        s = i.split("_")[-1].split(".")
        if int(s[0]) == x:
            return True, s[1]
    return False, ""


def main():
    num = _input()
    while num == 'c':
        num__(".\\")
        num = _input()
    tt, path = find_dir(num, ".\\")
    if tt:
        t, l = find_fil(num, path)
        if t:
            print(str(t) + '\t' + l)
        else:
            print(False)
    else:
        print(False)


if __name__ == '__main__':
    num__(".\\")
    while True:
        main()



