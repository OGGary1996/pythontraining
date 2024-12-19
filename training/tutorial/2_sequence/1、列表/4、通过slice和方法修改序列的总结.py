#删除元素
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List[1:2] = []
print(f'修改后的列表是{Gary_List}')

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
del Gary_List[1:2]
print(f'修改后的列表是{Gary_List}')

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.pop(1)
print(f'修改后的列表是{Gary_List}')

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.remove('猪八戒')
print(f'修改后的列表是{Gary_List}')

#插入元素或者序列
#不可指定位置，默认在最后插入
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List += ['牛魔王','铁扇公主']
print(f'修改后的列表是{Gary_List}')

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.append('牛魔王')
print(f'修改后的列表是{Gary_List}')

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.extend(['牛魔王','铁扇公主'])
print(f'修改后的列表是{Gary_List}')
#指定索引位置插入
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List[3:4] = ['牛魔王','铁扇公主']
print(f'修改后的列表是{Gary_List}')

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
print(f'原列表是{Gary_List}')
Gary_List.insert(3,'牛魔王')
print(f'修改后的列表是{Gary_List}')

