#返回值就是函数执行之后返回的结果
# 可以使用 return 来指定返回值
# 可以直接使用函数的返回值，也可以指定一个变量来接受函数的返回值。

def fun1(*nums):
	result = 0
	for num in nums:
		result += num
print(fun1(1,5,4)) # None
# print(f'数字分别为{nums}他们的和是{result}')  #报错信息 NameError: name 'nums' is not defined
# 函数中的代码块执行之后，并不会在代码块外面被作为对象直接引用，需要一个返回值来接受结果。

# return 后跟什么值，函数的返回值就是什么值，且return后可以跟任意类型的对象，同样也可以跟一个函数。
def fun2():
	return 100
print(fun2())#直接使用函数的返回值。fun2()表达式就代表了他的返回值
a = fun2() #指定一个变量来接收函数的返回值。
print(a)

def fun2():
	return 'hello'
print(fun2())

def fun2():
	def fun3():
		print('hello_world')
	return fun3 #返回值是fun3本身，不是fun3()
print(fun2())

def fun2():
	def fun3():
		print('hello_world')
	fun3()
fun2()

# 如果return后面不接任何的对象，或者直接不写return，则函数的结果是none
def fun4():
	a = 100
print(fun4())

def fun5():
	print('你好！')
	print('hello')
print(fun5()) # 先执行fun5()中的内容，但是由于fun5()内部没有写return，所以会再次返回一个none。

# return写在函数内部时，会直接中断整个函数并获取返回值，return后面的代码都不会执行。
def fun6():
	print('123')
	return
	print('abc') # 不会执行
fun6()

def fun7():
	for i in range(6):
		if i == 3:
			break # 中断循环代码块中的循环，不影响整个函数。
		print(i)
	print('循环结束了！')
fun7()

def fun7():
	for i in range(6):
		if i == 3:
			return #直接中断整个函数，此时不会执行 print('循环结束了！')
		print(i)
	print('循环结束了！')
fun7()

#通过return来优化

def fun1(*nums):
	result = 0
	for num in nums:
		result += num
	return result
print(fun1(123,456,789))



