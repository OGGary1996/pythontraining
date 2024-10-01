role = '->唐僧<-'
boss = '->白骨精<-'
print(f'======================欢迎来到《{role}大战{boss}》游戏！========================\
	\n 请输入1或者2来选择你的身份：\n 		1.{role} \n 		2.{boss}')
choose = input('请选择：')
role_level = 1
role_live = 2
role_attack = 2
boss_live = 20
boss_attack = 20
while choose not in '12':
	print('你的输入有误，请重新输入！')
	choose = input('请选择：')
else:
	if choose == '1':
		print(f'你选择了{role}! 你的初始等级为{role_level},生命值为{role_live},攻击力为{role_attack}！\
			\n =========================================================')

	elif choose == '2':
		print(f'你真不要脸！怎么能选择{boss}呢！系统已为您自动切换角色为{role}!\
			\n 现在你的角色是{role},你的初始等级为{role_level},生命值为{role_live},攻击力为{role_attack}！\
			\n =========================================================')

while True:
	print(f'现在请选择你希望的操作：\n 		1.打怪升级，满级为5级！\n 		2.与{boss}进行战斗！（{boss}的生命值为{boss_live},攻击力为{boss_attack}）\
		\n 		3.直接逃跑！')
	action = input('请输入你的选择：')
	if str(action) not in '123':
		print('你的输入有误，请重新输入！')
	elif action == '1':
		if role_level < 5:
			role_level += 1
			role_live += 5
			role_attack += 4
			print(f'恭喜你升级了！你现在的等级为{role_level},生命值为{role_live},攻击力为{role_attack}！\
				\n ======================================================')
		else :
			print(f'你的等级已经满级！无法再继续修炼，请尝试与{boss}进行战斗吧！\
				\n ======================================================')
	elif action == '2':
		role_live -= boss_attack
		boss_attack -= role_attack
		if role_live <= 0:
			print(f'你被{boss}杀死了！游戏结束！')
			break
		elif boss_live <= 0:
			print(f'{boss}被你杀死了！你赢得了战斗！') 
			break
	elif choose == '3':
		print('你选择了直接逃跑！游戏结束！')
		break