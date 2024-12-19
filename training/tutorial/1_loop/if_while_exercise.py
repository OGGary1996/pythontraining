#身份选择阶段
print('==============欢迎来到游戏《唐僧大战白骨精》================\
	\n 请输入1或2来选择你的身份：\n 		1、唐僧 \n 		2、白骨精')
a = str(input('请选择输入你的选择:'))
while a not in'12':
	print('你的输入有误，请重新输入！')
	a = str(input('请选择输入你的选择:'))
else:
	if a == '1' :
		print('你的身份是->唐僧<-，初始等级为1，你的攻击力是 2，你的生命值是 2。')
	elif a == '2':
		print('你真不要脸！怎么会选择白骨精！系统已经自动为你选择身份！\n 你的身份是->唐僧<-，初始等级为1，你的攻击力是 2，你的生命值是 2。')
#操作阶段
flag = True 
level = 1
hart = 2
attack = 2
boss_hart = 20
boss_attack = 20
#设置一个循环使得每次选择操作1之后进行回滚，可进行反复选择操作。
while flag:
	print(f'请选择你要进行的操作：\n 		1、打怪升级，满级为5级！\n 		2、与白骨精进行战斗！（白骨精的攻击力为{boss_attack}，生命值为{boss_hart}）\
		\n  		3、逃跑')
	b = int(input('请选择你要进行的操作：'))
	if str(b) not in '123':
		print('输入的操作有误，请重新输入！') 

	elif b == 3:
		flag = False
		print('怂逼！游戏结束！')

	elif b == 1:
		if level < 5:
			level += 1
			hart += 4
			attack += 5
			print(f'恭喜你升级成功！你的等级现在是{level},生命值是{hart},攻击力为{attack}。\n==============================================')
		else :
			print(f'你已经达到满级！你的等级现在是{level},生命值是{hart},攻击力为{attack}。\n==============================================')

	elif b == 2:
		boss_hart -= attack
		hart -= boss_attack
		if boss_hart <= 0:
			print('你杀死了白骨精！游戏结束！')
			flag = False 
		elif hart <= 0:
			print('你被白骨精杀死了！游戏结束！')
			flag = False
