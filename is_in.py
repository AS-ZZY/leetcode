import os


def num_(path):
    if os.path.exists(path):
        count = 0
        for root, dirs, files in os.walk(path):
            count += len(files)
        a = 13 - len(path.split("\\")[-1])
        print(path.split("/")[-1] + "\t" + str(count))
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
    print("sum" + "\t" + str(sum_))

def find():
	l = [] 
	ll = []
	try:
		num = input("题号：")
		a = int(num) // 100
		path =  str(a * 100 + 1) + "-" + str((a + 1) * 100)
		for root, dirs, files in os.walk(path):
			l = files.copy()
		for i in l:
			i = i.split(".")	
			if i[0] == "leetcode_" + num:
				print(True, i[1])
				return
		print(False)
	except:
		print(False)
		


if __name__ == '__main__':
	num_("./")
	num__("./")
	while True:
		find()


