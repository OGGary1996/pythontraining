#元组（tuple）
#元组是一个不可变的序列，但是操作方式与可变列表是一样的，在操作元组时，当作是一个不可变的列表即可。

#创建元组
#列表创建时使用[]，创建元组使用(),当元组不是空元组时，可以不写括号。

Gary_tuple = (1,2,3,4,5,6)
print(Gary_tuple)
#同样可以对元组进行非改变类的操作，例如index，slice.
print(Gary_tuple[3])
#但是不能对其进行替换，删除，添加等修改操作。TypeError: 'tuple' object does not support item assignmen
# Gary_tuple[3] = 20
# print(Gary_tuple)

#元组和其他序列一样可以进行 解构赋值
Gary_tuple = 10,20,30,40
a,b,c,d = Gary_tuple
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')
#通常进行对象赋值的交换：
a = 5 
b = 10 
c = 15 
a,b,c = c,a,b # 注意！此时右边的c,a,b被视作一个元组
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
#对元组进行解构赋值时，变量的个数需要与元组中的元素个数一致；但是当元组中元素非常多时可以在用如下方式：
a,b,*c = 5,10,15,20,40,60,90,100
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c},c的类型是{type(c)}') # 这里的c将会将除了a,b剩下的元素组成一个新的列表。

a,*b,c = 5,10,15,20,40,60,90,100
print(f'a = {a}')
print(f'b = {b},b的类型是{type(b)}')
print(f'c = {c}') # 这里的b将会将除了第一个a,最后一个c剩下的元素组成一个新的列表。

*a,b,c = 5,10,15,20,40,60,90,100
print(f'a = {a},a的类型是{type(a)}')
print(f'b = {b}')
print(f'c = {c}') # 这里的a将会将除了倒数第二个b,最后一个c剩下的元素组成一个新的列表。
#但是不能出现两个及以上的*变量。
