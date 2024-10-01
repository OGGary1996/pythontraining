#作用域（scope）
# 作用域指的是变量生效的区域
# 在python中一共有两种作用域：
#	全局作用域
#	 -全局作用域在程序执行创建时创建，在程序执行后销毁
#	 -所有函数以外的作用域都是全局作用域
#	 -在全局作用域中定义的变量都属于全局变量，可以在程序的任意位置访问

#	函数作用域
#	 -函数作用域在函数调用时创建，在函数调用后销毁
#	 -函数每调用一次就会产生一个新的函数作用域
#	 -在函数作用域中定义的变量叫局部变量，只能在函数内部访问

a = 100 #全局变量
def fun1():
	b = 200 #局部变量
	print(f'函数内部的a = {a}')
	print(f'函数内部的b = {b}')
fun1()
print(f'函数外部的a = {a}')
# print(f'函数外部的b = {b}')  NameError: name 'b' is not defined

# 局部变量a存在于fun2的函数作用域中，但是在fun2函数的下一级fun3函数中可以访问局部变量a
def fun2():
	a = 10
	def fun3():
		print(f'a = {a}')
	fun3()
fun2()

# 变量的查找
# 当我们调用一个变量时，会优先在当前的作用域中寻找，如果没有，则会继续去上级作用域寻找，以此类推。
a = 5
def fun4():
	a = 10
	def fun5():
		a = 20
		print(f'a = {a}')
	fun5()
fun4()

# 变量的修改
# 如果希望在函数内部直接修改全局变量,则需要用global关键字来声明修改的变量。
a = 10
def fun():
	global a # 声明修改的变量为全局变量。
	a = 100 
	print(f'函数内部a = {a}')
fun()
print(f'函数外部a = {a}')


#命名空间（namespace）
# 命名空间指的是变量的储存位置，每一个变量都需要保存到指定的命名空间内。
# 每一个作用域都有一个对应的命名空间，用于储存变量，命名空间与作用域一一对应。
# 全局命名空间用于保存全局变量，函数命名空间保存局部变量，命名空间写到哪里，就是获取哪里的命名空间。
namespace = locals() # 获取全局作用域的命名空间。
print(f'当前全局作用域的命名空间是{namespace},\n类型是{type(namespace)}') # 命名空间本质上是一个字典，所有的变量都保存在这个地点内。
# 既然是字典，当然也符合字典的使用规范：
print(f'命名空间中变量a的值为{namespace['a']}')
# 函数的命名空间
def fun100():
	a = 100
	namespace = locals()
	print(namespace)
fun100()

