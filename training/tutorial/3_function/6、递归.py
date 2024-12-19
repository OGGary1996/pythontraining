#  递归的含义简单来将就是自己引用自己：
#   从前有座山，山里有座庙，庙里有个老和尚在讲故事，讲的什么故事呢：
#       从前有座山，山里有座庙，庙里有个老和尚在讲故事，讲的什么故事呢：
#           从前有座山，山里有座庙，庙里有个老和尚在讲故事，讲的什么故事呢：…………

# 尝试求10的阶乘
n = 10
for i in range(1,10):
    n *= i
print(n)

# 创建一个函数 来求任意数字的阶乘
def fun1(nums):
    result = nums
    for i in range(1,nums):
        result *= i
    return result
print(fun1(10))

# 递归式的函数 就是在函数中自己调用自己：
#  无穷递归：
def fn():
    fn()
# fun() 效果类似于死循环

# 递归是解决问题的一种方式，与循环类似
#   整体思想是，把一个大问题分解为一个个小问题，直到无法被分解，再去解决问题。
# 递归式函数的两个要件：
#   1、基线条件：问题能够分解到的最小的问题，当满足了基线条件时，需要让递归停止执行
#   2、递归条件：将问题继续分解的条件
# 例如任意数字阶乘的问题，可以通过 n! = n * (n-1)! 的条件，一直分解到 1！
# 上述情况下基线条件就是 1！，递归条件就是 n! = n * (n-1)!
def fun2(nums):
    if nums == 1:
        return 1    #定义基线条件
    result = nums * fun2(nums-1)
    return result   #定义递归条件
print(fun2(10))

# 练习
#   1、创建一个函数来为任意一个数字做幂运算 n ** i
def power(n,i):
    if i == 1:
        return n    #定义基线条件
    result = n * power(n,i-1)
    return result   #定义递归条件
print(power(5,3))

#    2、创建一个函数来检查任意一个字符串是否为回文字符串（字符串往前和往后念是一样的 abcdcba）,是回文字符串则返回True，否则返回False
def fun3(str1):
    if len(str1) < 2:
        return True
    elif str1[0] != str1[-1]:
        return False    #本次案例中基线条件存在两个，即字符串只有一个字符，和第一步检查中首位两个字符不一样则可马上判定
    return fun3(str1[1:-1])
print(fun3('hello'))
