import datetime

Name = str(input("请输入您的姓名："))
birth = int(input("请输入您的出生年份："))
age = datetime.date.today().year - birth
print("您好！{0}。您{1}岁。".format(Name, age))
