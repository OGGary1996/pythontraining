s = {'a','b',1,2,3,4}

#集合是无序的，不支持使用index。
# print(s[2])

#使用len（）函数。
print(len(s))

# is not is in not in 

#添加元素 
# 通过set*.add()方法
s.add(10)
print(s,type(s))
# 通过set*.update方法
s.update('hello') #添加字符串
s.update([1,2,3]) #添加序列
s.update({'f':100,'g':200}) #添加字典
print(s,type(s))

#删除元素
# 通过set*.pop()方法来删除，会随机删除一个元素。
s.pop()
print(s,type(s))
# 通过set*.remove()方法来删除指定的元素。
s.remove(10)
print(s,type(s))
# 通过set*.clear()方法来清空所有的元素。

#复制元素
#set*.copy()

#集合的运算
# 集合的运算不影响集合本身，只会返回结果。
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
# & 交集运算
result = set1 & set2
print(f'运算结果是{result}')

# ^ 异或集运算
result = set1 ^ set2
print(f'运算结果是{result}')

# | 并集运算
result = set1 | set2
print(f'运算结果是{result}')
#	效果类似于set*.update方法
set1.update(set2)
print(f'运算结果是{set1}')

# - 差集运算 
result = set1 - set2
print(f'运算结果是{result}')





