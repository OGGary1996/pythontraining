numb = int(input('请输入一个整数:') )
result = numb % 2
if result != 0 :
	print('该数字为奇数')
else :
	print('该数字为偶数')

year = int(input('请输入任意一个年份：'))
result = (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0
if bool(result) :
	print('该年份是闰年')
else :
	print('该年份是平年')

dog_age = float(input('请输入狗狗的年龄：'))
age = 10.5 * 2 + (dog_age-2) * 4 if dog_age >=2 else dog_age * 10.5
if dog_age <= 0 :
	print('输入有误，请重新输入。')
else :
	print(f'狗狗的年龄相当于人的{age}岁u')

dog_age = float(input('请输入狗狗的年龄：'))
while dog_age < 0:
	print('输入年龄有误，请重新输入！')
	dog_age = float(input('请输入狗狗的年龄：'))
	age = 10.5 * 2 + (dog_age-2) * 4 if dog_age >=2 else dog_age * 10.5
	print(f'狗狗的年龄相当于人的{age}岁')

dog_age = float(input('请输入狗狗的年龄：'))
if dog_age <= 0 :
	print('输入有误，请重新输入。')
elif dog_age <= 2 :
	age = dog_age * 10.5
	print(f'狗狗的年龄相当于人类的{age}岁')
else :
	age = 2 * 10.5 + (dog_age-2) * 4
	print(f'狗狗的年龄相当于人类的{age}岁')

dog_age = float(input('请输入狗狗的年龄：'))
while dog_age <= 0 :
	print('输入有误，请重新输入。')
	dog_age = float(input('请输入狗狗的年龄：'))
else :
	if dog_age <= 2 :
		age = dog_age * 10.5
		print(f'狗狗的年龄相当于人类的{age}岁')
	else :
		age = 2 * 10.5 + (dog_age-2) * 4
		print(f'狗狗的年龄相当于人类的{age}岁')

num = float(input('请输入你的期末考试成绩:'))
if num > 100 or num < 0 :
	print('输入成绩无效')
elif num == 100 :
	print('奖励一台BMW!')
elif 80 <= num <= 99 :
	print('奖励一台iPhone!')
elif 60 <= num <= 79 :
	print('奖励一本书！')
else :
	print('SB')

num = float(input('请输入你的期末考试成绩:'))
while num > 100 or num < 0 :
	print('输入成绩无效')
	num = float(input('请输入你的期末考试成绩:'))
else :
	if num == 100 :
		print('奖励一台BMW!')
	elif 80 <= num <= 99 :
		print('奖励一台iPhone!')
	elif 60 <= num <= 79 :
		print('奖励一本书！')
	else :
		print('SB')

num = float(input('请输入你的期末考试成绩:'))
if 0 <= num <= 100 :
	if num == 100 :
		print('奖励一台BMW!')
	elif 80 <= num <= 99 :
		print('奖励一台iPhone!')
	elif 60 <= num <= 79 :
		print('奖励一本书！')
	elif 0 <= num <= 59 :
		print('SB')
else :
	print('输入的成绩无效！')


high = float(input('请输入身高（cm）：'))
handsome = bool(input('请输入0/1，（0表示丑，1表示帅）：'))
properties = float(input('请输入存款金额：'))
if type(handsome) != bool or high <= 0 :
	print('检测到条件有误，请重新输入自身条件！')
elif high >= 180 and handsome == True and properties >= 5000000 :
	print('我一定要嫁给他！')
elif high >= 180 or handsome == True or properties >= 5000000 :
	print('嫁吧 比上不足比下有余！')
else :
	print('不嫁！')

high = float(input('请输入身高（cm）：'))
handsome = bool(input('请输入0/1，（0表示丑，1表示帅）：'))
properties = float(input('请输入存款金额：'))
while type(handsome) != bool or high <= 0 :
	print('检测到条件有误，请重新输入自身条件！')
	high = float(input('请输入身高（cm）：'))
	handsome = bool(input('请输入0/1，（0表示丑，1表示帅）：'))
	properties = float(input('请输入存款金额：'))
else :
	if high >= 180 and handsome == True and properties >= 5000000 :
		print('我一定要嫁给他！')
	elif high >= 180 or handsome == True or properties >= 5000000 :
		print('嫁吧 比上不足比下有余！')
	else :
		print('不嫁！')


# ===========================================================================

numb = 1
total = 0
N = 0
while numb < 100:
	print(numb)
	total += numb
	N += 1
	numb += 2
print(f'100以内的奇数个数是{N}，它们的总和是{total}')

total = 0
for i in range(1,101):
	if i % 2 != 0:
		total += i
		print(i)
print(total)

total = 0
for i in range(1,101,2):
	total += i
	print(i)
print(total)


numb = 0
total = 0
N = 0
while numb < 100:
	numb += 1
	if numb % 2 != 0 :
		print(numb)
		total += numb
		N += 1
print(f'100以内的奇数个数是{N}，它们的总和是{total}')

numb = 7
total = 0
N = 0
while numb < 100:
	print(numb)
	total += numb
	N += 1
	numb += 7
print(f'100以内所有能被7整除的数一共有{N}个，他们的总和为{total}。')

numb = 0
total = 0
N = 0
while numb < 100:
	numb += 1
	if numb % 7 == 0:
		print(numb)
		total += numb
		N += 1
print(f'100以内所有能被7整除的数一共有{N}个，他们的总和为{total}。')

numb = 100
total = 0
N = 0
while numb < 1000:
	a = int((numb)/1000*10) #取百位值
	b = int((numb-a*100)/10) #取十位值
	c = int(numb-a*100-b*10) #取各位值
	if a**3 + b**3 + c**3 == numb:
		print(numb , a , b , c)
		total += numb
		N += 1
	numb += 1
print(f'100至1000以内的水仙花数共有{N}个，它们的总和为{total}。')

numb = 100
total = 0
N = 0
while numb < 1000:
	a = numb // 100
	b = (numb - a*100) // 10
	c = numb % 10
	if a**3 + b**3 + c**3 == numb:
		print(numb , a , b , c)
		total += numb
		N += 1
	numb += 1
print(f'100至1000以内的水仙花数共有{N}个，它们的总和为{total}。')

total = 0
for i in range(100,1000):
	a = i // 100
	b = (i - a*100) // 10
	c = i % 10
	if i == a ** 3 + b ** 3 + c ** 3:
		print(i)
		total += i
print(total)

numb = int(input('请输入任意一个数字：'))
while numb <= 1 :
	print('输入值不合理，请重新输入！')
	numb = int(input('请输入任意一个数字：'))
N = 1
a = 0
while N <= numb :
	if numb % N == 0 :
		a += 1 #如果是质数，则a值会+1
		N += 1
print('输入的值是一个质数') if a == 2 else print('输入的值不是一个质数')

numb = int(input('请输入任意一个数字：'))
while numb <= 1 :
	print('输入值不合理，请重新输入一个数字！')
	numb = int(input('请输入任意一个数字：'))
N = 2
flag = True
while N < numb :
	if numb % N == 0:
		flag = False
		N += 1
if flag == True :
	print('该数字是一个质数！')
else :
	print('该数字不是一个质数！')

total = 0
for i in range(2,1001):
	for n in range(2,i):
		if i % n != 0:
			print(i)
			total += i
			break
print(total)

# ========================================================================================

i = 0
while i < 5:
	N = 0
	while N <5:
		print('* ',end = '')
		N += 1
	print()
	i += 1


a = 0
while a < 5:
	b = 0
	while b < a + 1:
		print('* ',end = '')
		b += 1
	print()
	a += 1


a = 0
while a < 5:
	b = 0
	while b < (5 - a):
		print('* ',end = '')
		b += 1
	print()
	a += 1


a = 1
while a <= 9:
	b = 1
	while b <= 9:
		print(f'{a}x{b}={a * b} ',end = '')
		b += 1
	print()
	a += 1

a = 1
while a <= 9:
	b = 1
	while b <= a:
		print(f'{b}x{a}={a*b}  ',end = '')
		b += 1
	print()
	a += 1

a = 2
while a <= 100:
	b = 2
	flag = True
	while b < a:
		if a % b == 0:
			flag = False
		b += 1
	if flag == True:
		print(a)
	a += 1

