#python可以通过引入模块来实现更多的功能来实现扩展
#例如想要获取一段代码的执行时间，可以引入一个time模块

# #优化前⬇️

from time import *
begin = time()
a = 2
total = 0
while a <= 10000:
	b = 2
	flag = True
	while b < a:
		if a % b == 0:
			flag = False
		b += 1
	if flag == True:
		print(a)
		total += a
	a += 1
end = time()
print(f'time_cost_is{end - begin}s!total_is_{total}')

#优化后⬇️

from time import *
begin = time()
a = 2
total = 0
while a < 10000:
	b = 2
	flag = True
	while b <= (a / 2): #缩小b的范围
		if a % b == 0:
			flag = False
			break
		b += 1
	if flag == True:
		print(a)
		total += a
	a += 1
end = time()
print(f'time_cost_is{end - begin}s!total_is_{total}')


from time import *
begin = time()
a = 2
total = 0
while a < 10000:
	b = 2
	flag = True
	while b <= (a ** 0.5): #缩小b的范围
		if a % b == 0:
			flag = False
			break
		b += 1
	if flag == True:
		print(a)
		total += a
	a += 1
end = time()
print(f'time_cost_is{end - begin}s!total_is_{total}')