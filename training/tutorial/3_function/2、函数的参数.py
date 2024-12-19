#函数的参数
# 形参：在函数内部定义了形式上的参数，但并不赋值，只是声明了变量。
# 实参：如果函数定义了形参，那必须在调用函数的时候指定实参，实参将会赋值给形参，有几个形参对应几个实参。
# 例子1：计算任意两个数的和
def sum(a,b) :
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'a + b = {a + b}')

sum(2,5)
sum(10,20)

# 例子2：根据不同的名称来显示欢迎信息
def welcome(name):
	print(f'欢迎{name}光临！')
welcome('Gary') # welcome(input('请输入您的姓名：')) 



#参数的传递
# 形参可以指定默认值，如果后续没有传递实参，则该默认值生效；如果传递了实参，则还是以实参为准。
def fun1(a , b , c = 3):
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'c = {c}')
fun1(1,2)

# 实参的传递方式
#  1、通过位置参数传递，将对应位置的实参传递给形参，一一对应。
fun1(5,6,7)
#  2、通过关键字参数传递，直接不需要记忆形参的位置，直接指定形参的名字即可。
fun1(b = 20,a = 100,c = 60)
# 两种传递方式可以同时存在，但是一定要注意，关键字参数只能放在位置参数后面。
fun1(99,c = 58,b = 20)
# 可以只采用关键字参数，要求形参最前面加上 *， 
def fun(*, a , b , c):
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'c = {c}')
fun(b = 2,a = 10,c = 26)
# 在调用实参时，系统不会检查实参的对象类型，可以实参可以传递任意类型的对象。
fun1('hello',[1,2,3],{'a':1,'b':2})
# 甚至可以传递另一个函数：
def fun2(name):
	print(name)
fun2(fun1) # !注意 这里的fun1没有加（），没有调用fun1的函数代码块，仅仅是将fun1本身当作实参进行传递。
fun2(fun1('hello',[1,2,3],{'a':1,'b':2}))

# 在函数中的代码块中对形参重新赋值不会影响其他的变量：
def fun3(a):
	a = 20
	print(f'a = {a}',id(a))
b = 10
fun3(b)
print(f'b = {b}',id(b)) # 在代码块中对形参a重新赋值，修改了a变量，不会影响b变量的值。
# 但是如果在函数的代码块中修改了对象，则指向该对象的所有变量都会被修改。
def fun4(a):
	a[2] = 100
	print(f'a = {a}',id(a))
b = [1,2,3,4]
fun4(b)
print(f'b = {b}',id(b)) # 在代码块中对形参a进行了修改对象的操作，而形参a与b都指向同一个对象，该操作修改了对象会对所有指向该对象的变量进行修改。
# 如果希望避免此情况（不希望代码块对对象做修改），可以在将另外一个变量的副本作为实参来传递，这样代码块仅会修改那个副本而不会影响到变量本身。
def fun5(a):
	a[2] = 100
	print(f'a = {a}',id(a))
b = [1,2,3,4]
fun5(b.copy())
print(f'b = {b}',id(b))



#不定长的参数
# 函数的形参与实参个数必须一一对应，但如果例如需要求任意个数的数字的和，则需要不断修改实参于形参的个数，所以有了不定长参数。
# *形参，此时无论实参个数有多少，都会传递给这个形参，并且以tuple的形式保存（类似于tuple的结构）。
def fun6(*a):
	print(f'a = {a},a的类型是{type(a)}')
fun6(1,2,3,4,5)

# 例如用如下函数求任意个数的数字之和：
def fun7(*nums):
	result = 0
	for num in nums:
		result += num
	print(f'数字分别为{nums}他们的和是{result}')
fun7(1,5,4)

# 同样类似于元组的解构，带*的不定长参数只能有1个。
# 当*形参位于最后时，会自动按照位置实参传递给形参，最后所有的实参都传递给*形参（装包）：
def fun8(a,b,*c):
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'c = {c}')
fun8(1,2,3,4,5,6,7,8,9)
# 同样类似于元素的解构，带*形参可以位于中间和前面，但是注意！带*形参之后的形参所对应的实参必须要以关键字形式的实参来传递，不能以位置实参来传递。
def fun9(a,*b,c):
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'c = {c}')
fun9(1,2,3,4,5,6,7,8,c = 9)

def fun10(*a,b,c):
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'c = {c}')
fun10(1,2,3,4,5,6,7,b = 8,c = 9)
# *形参对应的实参只能是位置实参，不能是关键字实参。
# def fun11(*a):
# 	print(f'a = {a}，类型是{type(a)}')
# fun11(b = 1,c = 2,d = 3) #报错类型是 TypeError: fun11() got an unexpected keyword argument 'b'

# **形参 可以对其传递关键字实参。
def fun11(**a):
	print(f'a = {a}，类型是{type(a)}')
fun11(b = 1,c = 2,d = 3) #此时实参传递的对象格式为dict，key对应实参的名字，value对应实参的值。
# **形参只能有一个，且只能放在所有形参的最后一个。
def fun12(a,b,c,**d):
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'c = {c}')
	print(f'd = {d},d的类型是{type(d)}')
fun12(c = 10,a = 5,b = 0,e = 130,f = 146,g = 126) # 所有能对应其他形参的关键字实参传递完后，会将剩下的所有实参统一传递给**形参。
fun12(c = 10,a = 5,b = 0,d = 120)


# 参数解包
def fun13(a,b,c):
	print(f'a = {a}')
	print(f'b = {b}')
	print(f'c = {c}')
# 元组与list的解包
tuple1 = (1,2,3)
# fun13(tuple1) #报错信息为 TypeError: fun13() missing 2 required positional arguments: 'b' and 'c'
# tuple1会作为第一个位置实参，整个传递给形参a。
# 需要将tuple1进行解包，然后再分别传递给形参a,b,c。
fun13(*tuple1)

# 字典的解包
dict1 = {'a':100,'b':200,'c':300}

fun13(**dict1)






