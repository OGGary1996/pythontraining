# 高阶函数（至少满足如一个要求）
#  1、接收一个或者多个函数作为参数
#  2、将函数作为返回值的函数

# 普通函数例子：
#  定义一个函数来将列表中所有的偶数保存到一个新的列表中并返回
list1 = [1,2,3,4,5,6,7,8,9,10]
def fun1(lst):
    new_list = []
    for i in lst:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
print(fun1(list1))
print(list1)
# 缺点：如果需要变更需求例如将奇数提取出，或者将大于5的数提出则需要更新代码块

# 高阶函数
#  将各种需求先作为函数定制好，需要那种需求就调用哪种函数
def fun2(i): 
    if i % 2 == 0:
        return True
    return False

def fun3(i):
    if i > 5 :
        return True
    return False

def fun4(i):
    if i % 2 != 0:
        return True
    return False

def fun(new_fun,lst):
    new_list = []
    for n in lst:
        if new_fun(n) :
            new_list.append(n) # 通过调用new_fun函数 可以在此随意更新上面的任意一个需求
    return new_list
print(fun(fun4,list1)) # 通过给new_fun函数赋值 可以更新任意一个需求

# 实际上上述简单的功能也可以通过一个内建函数filter()来实现
# filter() 可以从序列中过滤出符合条件的元素 保存到一个新的可迭代的结构中
#  参数：1、函数，根据该函数来过滤可迭代的结构，2、需要过滤的可迭代结构
#  返回值：过滤后的新的可迭代结构

result = filter(fun4,list1) 
print(result) # <filter object at 0x10103a4a0> 表示返回值为一个新的可迭代的结构，需要将其转换为list
print(list(result))


# 通过在全局作用域中创建的fun2-4来实现一些小功能会占用函数名称，可以采用匿名函数（lambda）
# lambda函数表达式专门用于创建一些简单的表达式，也是函数创建的另外一种方式
# lambda 参数列表：返回值
def fn1(a,b):
    return a + b

lambda a,b : a + b #两个函数功能一样

# 调用lambda()
result = (lambda a,b : a + b)(10,10)
print(result)  #通过加括号直接调用

sum = lambda a,b : a + b 
print(sum(10,10)) # 通过先给lambda函数赋值再调用函数
# 以上两种调用方式并不常用，lambda函数作为匿名函数主要作用为可以高度定制化，用一次之后就不再使用

# 可以通过lambda函数优化之前的filter函数
result = filter(lambda i : i % 2 == 0,list1)
print(list(result))

# 除了filter函数以外，还有一个内置函数map()
# map()可以对任意一个可迭代的对象中的所有元素进行指定的操作 
# 参数1: 指定将要对对象中元素进行的操作，参数2: 需要进行操作的可迭代对象
# 将list1中的元素统一乘以2
result = map(lambda i : i * 2,list1)
print(list(result))

# sort()和sorted()
# list中有sort方法可以对元素进行排序
list2 = ['aaaa','bb','cccccc','ddd','fffffffffff']
list2.sort() 
print(list2) # 但是sort方法只会对字符串的unicode编码进行排序
# 如果希望对字符串的长度进行排序，可以加入一个关键字参数key
#   key需要一个函数作为参数，当设置了函数作为参数后每次都会以列表中的一个元素作为参数来调用该函数，并使用函数的返回值来比较大小
list2.sort(key=len)
print(list2) 

list2 = ['1',2,3,'4','5',6]
# list2.sort() # 直接排序将会报错，因为int和str类型不能放在一起排序
list2.sort(key=int) #加入关键字int函数，会将每个元素都先转换为int再排序
print(list2)

# sorted()函数
# 和sort方法的用法基本一致，但是sorted()函数可以对任意的序列进行排序，并且sorted()函数不会影响原来的对象，而是返回一个新的对象
list3 = [2,5,8,'12','6','9']
print(f'排序前:{list3}')
print(sorted(list3,key=int))
print(f'排序后:{list3}')