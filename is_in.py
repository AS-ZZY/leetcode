import os

def num(path):
    count = 0
    for i in range(11):
        l = 0
        path2 = str(i * 100 + 1) + "-" + str(i + 1) + "00"
        for root, dirs, files in os.walk(path + path2):
            l = len(files)
        count += l
        print(path2 + " " * (12 - len(path2)) + str(l))
    print("sum\t" + str(count))


def find():
	l = [] 
	ll = []
	try:
		num = input("题号：")
		if num == "exit":
			return False
		a = int(num) // 100
		path =  str(a * 100 + 1) + "-" + str((a + 1) * 100)
		for root, dirs, files in os.walk(path):
			l = files.copy()
		for i in l:
			i = i.split(".")	
			if i[0] == "leetcode_" + num:
				print(True, i[1])
				return True
		print(False)
	except:
		print(False)
	return True
	

if __name__ == '__main__':
	num("./")
	print("exit退出")
	while find():
		pass


