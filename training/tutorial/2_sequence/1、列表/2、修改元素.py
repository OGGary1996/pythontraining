#通过索引！！替换！！元素
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
Gary_List[0] = 'swk'
print(Gary_List)
#通过del！！删除！！元素
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
del Gary_List[2]
print(Gary_List)


#通过slice修改编辑元素,给slice赋值时只能赋值序列，相当于赋值的序列替换了slice的序列。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
Gary_List[0:2] = 'swk' #'swk'在此相当于一个['s','w','k']序列。
print(Gary_List)
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
Gary_List[0:2] = ['牛魔王','铁扇公主']
print(Gary_List)

#通过slice！！插入！！新元素（相当于吧slice的范围定义为0）
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
Gary_List[0:0] = ['牛魔王']
print(Gary_List)

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
Gary_List[6:6] = ['牛魔王']
print(Gary_List)

#!!!!当设置了step之后，赋值的序列元素个数必须等于slice的元素个数
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
Gary_List[::2] = ['牛魔王','铁扇公主','红孩儿']
print(Gary_List)

#通过slice来！！删除！！元素
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
Gary_List[1:2] = []
print(Gary_List)

Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
del Gary_List[1:2]
print(Gary_List)

#=============以上操作只针对于可变序列==============
#e.g
# a = 'hello' 
# a[1] = 'a'
# print(a) #TypeError: 'str' object does not support item assignment
# #str不是可变序列

#如果非要修改，可以采用list()函数来将序列转换为可变序列
a = list('hello')
a[1] = 'a'
print(a)
