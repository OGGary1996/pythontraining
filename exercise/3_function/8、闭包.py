# 将函数作为返回值返回 也是高阶函数
def fn1():
    def inner():
        print('这是inner')
    return inner 
r = fn1()
r()
# r是一个函数，是调用fn1()之后返回的函数
#  这个函数是在fn1内部定义的，并不是全局函数，所以这个函数总能访问到fn1函数内部的变量
def fn1():
    a = 10
    def inner():
        print('这是inner',a)
    return inner 
r = fn1()
r()
# 这种高阶函数也称为闭包，通过闭包可以创建一些只能有当前函数能访问到的变量
#  可以将一些私有数据藏到闭包中
# 求一个序列中元素的平均值
nums = [] # 先建立一个空序列用于储存元素，以便后续添加
def average(i):
    nums.append(i)
    return sum(nums)/len(nums) # sum()是一个内置函数，用于求序列的中元素的和
print(average(10))
print(average(20))
print(average(30))
# 但是这样做有一个很大的风险，nums作为全局对象，所有人都可以访问nums，我们需要将闭包操作将nums放在函数内部
def out_average():
    nums = []
    def inner_average(i):
        nums.append(i)
        return sum(nums)/len(nums)
    
    return inner_average
r = out_average()
print(r(10))
print(r(20))
print(r(30))

# 形成闭包的必要条件：
#   1、函数嵌套，2、将内部函数作为返回值返回，3、内部函数必须使用到外部函数的变量