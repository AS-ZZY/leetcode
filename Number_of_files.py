import os


def main(path):
    if os.path.exists(path):
        count = 0
        for root, dirs, files in os.walk(path):
            for _ in files:
                count += 1
        print(path.split("\\")[-1] + " " + str(count))
        return count
    else:
        return 0


if __name__ == '__main__':
    path = '.\\'
    sum_ = 0
    for i in range(10):
        path_ = str(i) + "01-" + str(i + 1) + "00"
        path_all = path + path_
        sum_ +=  main(path_all)
    print("sum = " + str(sum_))
