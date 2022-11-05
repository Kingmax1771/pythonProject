file_object = open("object/info.txe", mode="wt", encoding="utf-8")
while True:
    user=input("请输入用户名：")
    if user.upper()=="Q":
        break
    psw=input("请输入密码：")
    data="{}-{}\n".format(user, psw)
    file_object.write(data)
file_object.close()
