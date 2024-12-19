#遍厉指的是将一个序列中所有的元素全部取出。

#通过while循环实现：
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
i = 0 
while i < len(Gary_List):
	print(Gary_List[i])
	i += 1

#通过for循环实现：
#语法：
#for 变量 in 序列：
#	代码块
#for循环会执行多次，序列有多少元素就会执行多少次。
#for循环每执行一次就会将序列里的元素依次赋值给这个变量。
Gary_List = ['孙悟空','猪八戒','沙僧','唐僧','白骨精','蜘蛛精']
for i in Gary_List:
	print(i)

