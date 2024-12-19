#列表的方法

#通过append方法添加元素，将会添加到列表的最后。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.append('牛魔王')
print(f'修改后的列表是{Gary_List}')

#通过insert方法在列表指定索引位置！！插入！！元素，类似于通过slice给定范围为0的位置来插入元素。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.insert(6,'牛魔王')
print(f'修改后的列表是{Gary_List}')

#通过extend方法来！！扩展！！元素，参数只能是一个序列！！！类似于 += ，也类似于用slice给定范围0的位置来插入一组序列。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.extend(['牛魔王','铁扇公主'])
print(f'修改后的列表是{Gary_List}')

#通过clear方法来删除列表所有的元素。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.clear()
print(f'修改后的列表是{Gary_List}')

#通过pop方法来删除指定索引位置的元素，并且pop方法是具有返回值的。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
result = Gary_List.pop(3) #括号内参数默认为-1，如不写括号内参数，则默认删除最后一个。
print(f'修改后的列表是{Gary_List}')
print(f'pop的返回值是{result}')

#通过remove方法来删除指定值的元素，如果有多个元素符合该值，那只会删除第一个元素。
Gary_List = [0,1,2,2,2,3,4,5]
print(f'原列表是{Gary_List}')
Gary_List.remove(2)
print(f'修改后的列表是{Gary_List}')

#通过reverse方法对序列的元素进行反转。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.reverse()
print(f'修改后的列表是{Gary_List}')

#通过sort方法对序列进行排序，默认为升序。
Gary_List = [100,101,90,265,389,129,88]
print(f'原列表是{Gary_List}')
Gary_List.sort()
print(f'修改后的列表是{Gary_List}')
 #如果想修改为降序排列，则可以添加一个reverse=True参数。
Gary_List = [100,101,90,265,389,129,88]
print(f'原列表是{Gary_List}')
Gary_List.sort(reverse = True)
print(f'修改后的列表是{Gary_List}')
