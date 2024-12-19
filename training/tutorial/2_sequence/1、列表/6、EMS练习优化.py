# print('-' * 20,'欢迎使用员工管理系统','-' * 20)
# employee_list = []
# while True :
# 	print('请选择你要进行的操作：\n \t1、查看员工信息。\n \t2、添加新员工。\n \t3、删除员工信息.\n \t4、关闭系统。')
# 	user_choose = input('请选择你要进行的操作（1-4）：')
# 	print('-' * 60)
# 	if user_choose == '1':
# 		if len(employee_list) == 0 :
# 			print('员工信息暂时为空，请添加员工信息后再查询！')
# 		else :
# 			for employee in employee_list :
# 				print('员工编号\t员工姓名\t员工年龄\t员工性别\t员工住址')
# 				print(employee_list.index(employee)+1,employee)
# 	elif user_choose == '2':
# 		employee_name = input('请输入员工的姓名：') 
# 		employee_age = input('请输入员工的年龄：') 
# 		employee_sexual = input('请输入员工的性别：')	 
# 		employee_location = input('请输入员工的住址：') 
# 		employee = f'{employee_name}\t{employee_age}\t{employee_sexual}\t{employee_location}'
# 		print('你将要添加的员工信息如下\n员工姓名\t员工年龄\t员工性别\t员工住址')
# 		print(employee)
# 		user_confirm = input( '请问是否确认添加？（Y/N）')
# 		if user_confirm == 'Y' :
# 			employee_list.append(employee)
# 			print(f'已成功添加员工{employee_name}的信息！')
# 		elif user_confirm == 'N':
# 			print('取消添加！')
# 		else :
# 			print('您的输入有误，请重新输入！')
# 	elif user_choose == '3':
# 		employee_number = int(input('请输入需要删除的员工编号：'))
# 		if employee_number < 1 and employee_number > len(employee_list):
# 			print('您的输入有误，请重新输入！')
# 		else:
# 			employee_list.pop(employee_number - 1)
# 			print(f'您已成功删除了{employee_number}号员工！')
# 	elif user_choose == '4':
# 		print('感谢使用员工管理系统，按回车键退出系统！')
# 		break
# 	else :
# 		print('您的输入有误，请重新输入！')
# 	print('-' * 60)

#=======================================================

print('-' * 20,'欢迎使用员工信息管理系统','-' * 20)
emp_list = []
while True:
	print('请选择你要进行的操作：\n\t1、查询员工信息。\n\t2、添加员工信息。\n\t3、删除员工信息。\n\t4、退出系统。')
	user_choose = int(input('请输入你的选择（1-4）：'))
	print('-' * 60)
	if user_choose == 1:
		if len(emp_list) == 0:
			print('员工信息暂时为空，请添加员工信息后再进行查询！')
		else :
			for emp in emp_list:
				print('员工编号\t员工姓名\t员工性别\t员工年龄\t员工住址')
				print(emp_list.index(emp)+1,emp)
	elif user_choose == 2:
		emp_name = input('请输入员工的姓名：')
		emp_sexual = input('请输入的性别：')
		emp_age = input('请输入员工的年龄：')
		emp_location = input('请输入员工的住址：')
		emp = f'\t{emp_name}\t{emp_sexual}\t{emp_age}\t{emp_location}'
		print('你将要添加的员工信息如下：\n\t员工姓名\t员工性别\t员工年龄\t员工住址')
		print(emp)
		user_choose = input('请问是否确认添加该员工的信息（Y/N）：')
		if user_choose == 'Y' or 'y':
			emp_list.append(emp)
			print('您已成功添加该员工信息！')
		elif user_choose == 'N' or 'n':
			print('您已经取消添加！')
		else :
			print('您的输入有误，请重新输入！')
	elif user_choose == 3:
		emp_number = int(input('请输入你要删除的员工信息编号：'))
		if emp_number < 1 or emp_number > len(emp_list):
			print('您的输入有误，请重新输入！')
		else:
			print('你将要删除的员工信息如下：\n\t员工姓名\t员工性别\t员工年龄\t员工住址')
			print(emp_list[emp_number - 1])
			user_del = input('请问是否确认删除该员工的信息（Y/N）：')
			if user_del == 'Y' or 'y':
				del emp_list[emp_number - 1]
				print('您已经成功删除了该员工信息！')
			elif user_del == 'N' or 'n':
				print('您已取消删除！')
			else:
				print('您的输入有误，请重新输入！')
	elif user_choose == 4:
		print('感谢使用员工信息管理系统，按回车键退出系统！')
		break
	else :
		print('您的输入有误，请重新输入！')
	print('-' * 60)










