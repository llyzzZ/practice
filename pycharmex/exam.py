count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate' and password == '666666':
        print("登陆成功！")
        break
    elif count == 2:
        print("3次用户名或者密码均有误！退出程序。")
    count += 1