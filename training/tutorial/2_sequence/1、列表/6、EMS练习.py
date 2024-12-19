print('-' * 20,'欢迎使用员工管理系统','-' * 20,)
employee_list = []
while True :
	print('请选择你要进行的操作：\n 	1、查看员工信息。\n 	2、添加新员工。\n 	3、删除员工信息。\n 	4、关闭系统。')
	user_choose = input('请选择你要进行的操作（1-4）:')
	print('-' * 60)
	if user_choose == '1' :
		if len(employee_list) == 0 :
			print('员工列表暂时为空，请添加员工后进行查询！')
		else :
			for i in employee_list:
				print('编号\t姓名\t年龄\t住址')
				print(employee_list.index(i)+1	,i)
	elif user_choose == '2' :
		employee_name = input('请输入员工的姓名：')
		employee_age = input('请输入员工的年龄：')
		employee_location = input('请输入员工的住址：')
		employee_list.append([employee_name,employee_age,employee_location])
		print(f'您已成功添加{employee_name}员工的个人信息!')
	elif user_choose == '3' :
		employee_number = int(input('请输入需要删除的员工编号：'))
		if employee_number < 0 and employee_number > (len(employee_list)-1) :
			print('您的输入有误，请重新输入！')
		else:
			employee_list.pop(employee_number - 1)
	elif user_choose == '4' :
		break
	else :
		print('您的输入有误，请重新输入！')
	print('-' * 60)

