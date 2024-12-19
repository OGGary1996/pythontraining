#基本操作
dict1 = {
'name':'sunwukong',
'age':'50000岁',
'gender':'male'
}
#查询对象
#	1、通过dict[key]来直接查询，但是key必须在dict内确实存在，否则会报错。
print(dict1['name'],dict1['age'],dict1['gender'])
print(dict2['name'],dict2['age'],dict2['gender'])
print(dict3['name'],dict3['age'],dict3['gender'])
#	2、通过 get 方法来查询，dict*.get(key[,可选值])，如果该key没有在dict内，不会报错，会返回可选值，可选值默认为为None。
print(dict2.get('name'))
print(dict2.get('hello'))

# len(),查询dict中键值对的项数。
print(len(dict2))

# in not in ,检查dict中是否包含指定的 key。
print('name' in dict2)

#修改dict
#	dict*[key] = value，如果是一个存在的key，则会将key对应的value修改；
#	如果key不存在，则会直接添加一项新的键值对。
dict3['name'] = '孙悟空'
print(f'dict3:{dict3}')

dict3['location'] = '花果山'
print(f'dict3:{dict3}')

#添加dict
#	dict*.setdefault(key[,default])可以创建一项新的键值对,如果是一个存在的key，则会将key对应的原value作为返回值返回，且不会对dict做任何修改；
#	如果key不存在，则会直接添加一项新的键值对。
result = dict3.setdefault('name','猪八戒')
print(f'dict3:{dict3}，返回值是{result}')
#	update(),将其他dict中的键值对添加到当前字典中。如果key有重复，则后dict的键值对会替换掉重复的key。
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}
d1.update(d2)
print(d1)

d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6,'b':10}
d1.update(d2)
print(d1)

#删除dict
#	del
dict_xiyouji = {'name':'sunwukong','age':'5000岁','gender':'male'}
del dict_xiyouji['age']
print(dict_xiyouji)

#	dict*.popitem(),会随机删除一个键值对，但是一般情况下会删掉最后一个。
#	该方法有返回值，会返回刚刚删除的键值对，并且返回值为有两个元素的tuple，第一个元素是key，第二个元素是value。
#	如果删除的是一个空dict，则会报错。
dict_xiyouji = {'name':'sunwukong','age':'5000岁','gender':'male'}
result = dict_xiyouji.popitem()
print(result)
print(dict_xiyouji)

#	dict*.pop(key[,default]),会删除指定key的键值对.
#	当没有输入默认值时，如果该dict里存在这个key，则会删除该键值对并返回value，如果没有这个key，则会报错。
#	当输入了默认值时，如果该dict里没有这个key，不会报错，且会返回输入的默认值。
dict_xiyouji = {'name':'sunwukong','age':'5000岁','gender':'male'}
result = dict_xiyouji.pop('age')
print(result)
print(dict_xiyouji)

dict_xiyouji = {'name':'sunwukong','age':'5000岁','gender':'male'}
result = dict_xiyouji.pop('location','您的选择有误，无法删除！')
print(result)
print(dict_xiyouji)

#	clear，删除当前dict里面的所有键值对。
dict_xiyouji = {'name':'sunwukong','age':'5000岁','gender':'male'}
dict_xiyouji.clear()
print(dict_xiyouji)


# copy()浅复制
#	copy()会对字典进行一个浅复制。
#	复制之后会形成一个新的字典，修改其中一个字典不会对影一个字典产生影响。
#	注意！！但如果原字典中的value是一个可变对象，那就不会复制这个可变对象。
dict_a = {'a':1,'b':2,'c':3,'d':4,'e':5}
dict_b = dict_a.copy()
print(dict_b)

#	注意！！但如果原字典中的value是一个可变对象，那就不会复制这个可变对象。
dict_a = {'a':1,'b':{'name':'shunwukong'},'c':3,'d':4,'e':5}
dict_b = dict_a.copy()
dict_b['b']['name'] = 'zhubajie'
print(f'dict_a = {dict_a},id是{id(dict_a)}')
print(f'dict_b = {dict_b},id是{id(dict_b)}')
#	虽然dict_a与dict_b经过copy()之后是两个单独的dict，但是由于copy()是浅复制，不会复制'b':{'name':'shunwukong'}，
#	所以在修改dict_b的时候也会同时修改dict_a。

