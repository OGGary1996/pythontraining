#字典（dict）
#字典属于一种新的数据结构，不同于序列，称为映射（mapping）
#序列存储数据的性能很好，但是查询信息的性能较差，如果不明确具体信息的索引，则需要遍历整个序列。
#但是在字典中每一个元素都有一个唯一的名字，通过为一个名字可以快速找到指定元素；在查询时效率非常高
#同样在字典中可以保存多个对象，每个对象有一个唯一的名字，这个名字称为 键（key），这个对象称为 值（value）；所以字典可以称为键值对（key-value）结构。
#字典里可以有多个键值对，每一个键值对称为一项（item）

#创建字典
a = {} 
print(f"a的类别是{type(a)}") #创建了一个空dict。
#添加键值对：
# 1、通过{}来创建：dict1 = {key1:value1,key2:value2,key3:value3}
# 2、通过dict函数来创建：dict1 = dict()
#	dict中的value可以是任意的对象。
#	dict中的key只能是不可变对象，int\str\bool\tuple\list……，但是一般采用str。
#	dict中的key不能重复，具有唯一性，如果出现重复的key，则会会替换掉前面的key。

dict1 = {
'name':'sunwukong',
'age':'50000岁',
'gender':'male'
} # 大括号中括号可以自行换行
print(f'dict1:{dict1}')

dict2 = dict(name = 'sunwukong',age = '5000岁',gender = 'male') #每一个对象都是一项键值对，通过dict函数创建的，所有的 key 都是str格式。
print(f'dict2:{dict2}')

#如果一个序列中所有的元素都是双值子序列，则可以用dict函数将该序列转换成dict。
#	双值子序列：
list1 = [('name','sunwukong'),('age','5000岁'),('gender','male')]
dict3 = dict(list1)
print(f'dict3:{dict3}')