#遍历字典
# dict*.keys()，该方法会返回字典所有的key
# 会返回一个序列，序列内容为所有的key。
new_dict = {'name':'sunwukong','age':'5000岁','gender':'male'}
print(new_dict.keys())
for key in new_dict.keys():
	print(key) #通过返回值打印了所有的key
#也可以通过返回的key来输出value：
for key in new_dict.keys():
	print(key,new_dict.get(key))

# dict*.values()，该方法会返回字典中所有的value。
# 会返回一个序列，序列内容为所有的value。
new_dict = {'name':'sunwukong','age':'5000岁','gender':'male'}
print(new_dict.values())
for value in new_dict.values():
	print(value) # 缺点是无法返回对应的key。

# dict*.items()，该方法会返回字典中所有的键值对。
# 返回值是一个序列，序列会包含双值子序列，key-value。且子序列是一个tuple。
new_dict = {'name':'sunwukong','age':'5000岁','gender':'male'}
print(new_dict.items())
for key_value in new_dict.items():
	key,value = key_value #通过对tuple解构，来分别获取key和value
	print(key,value)

new_dict = {'name':'sunwukong','age':'5000岁','gender':'male'}
print(new_dict.items())
for key,value in new_dict.items():
	print(key,value)