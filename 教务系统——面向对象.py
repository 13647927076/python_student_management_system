import math
from pymysql import Connection


class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f'姓名是:{self.name}语文成绩是:{self.chinese}数学成绩是：{self.math}英语成绩是:{self.english}总分是:{self.chinese + self.math + self.english}'

    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
        print(f'修改过后的成绩是{self}')


class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.students_list = []
        sql = 'select * from student_grade;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        # 清空原有内存列表，把数据库所有记录转成Student对象放入列表
        self.students_list = []
        for row in rows:
            stu = Student(row[0], row[1], row[2], row[3])
            self.students_list.append(stu)

    def add_student(self):
        name = input('请输入学生姓名： ')
        for s in self.students_list:
            if s.name == name:
                print("该学生已经存在，无法重复添加")
                return
        chinese = int(input("请输入语文成绩"))
        math = int(input("请输入数学成绩"))
        english = int(input("请输入英语成绩"))
        if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
            stu = Student(name, chinese, math, english)
            self.students_list.append(stu)
            print('学生信息添加成功')
            sql = f'insert into student_grade(name,chinese,math,english) values (\'{name}\',{chinese},{math},{english})'
            cursor.execute(sql)
        else:
            print('学生成绩必须在1到150之间')

    def update_student(self):
        name = input('请输入要修改的学生姓名： ')
        for s in self.students_list:
            if s.name == name:
                print(f'当前成绩： {s}')
                chinese = int(input('请输入修改之后的语文成绩： '))
                math = int(input('请输入修改之后的数学成绩： '))
                english = int(input('请输入修改之后的英语成绩： '))
                if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 < english <= 150:
                    s.update_score(chinese, math, english)
                    print('成绩修改成功')
                    print(f"修改后的成绩是:{s}")
                    sql = f'update student_grade set chinese={chinese}, math={math}, english={english} where name="{name}"'
                    cursor.execute(sql)
                    return
                else:
                    print('学生成绩必须在1到150之间')
                    return
        print('未找到学生信息')

    def delete_student(self):
        name = input('请输入要删除的学生姓名： ')
        for s in self.students_list:
            if s.name == name:
                self.students_list.remove(s)
                print('删除成功')
                sql = f'delete from student_grade where name="{name}"'
                cursor.execute(sql)
                return
        print("未找到该学生，删除失败")

    def query_student(self):

        name = input("请输入要查询的学生姓名： ")
        for s in self.students_list:
            if s.name == name:
                print(f'学生信息为：{s}')

    def list_student(self):

        for s in self.students_list:
            print(s)

    def run(self):

        print(f"欢迎使用教务系统{EduManagement.system_version}")
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            choice = input('请选择要执行的操作，输入1-6: ')
            print()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.query_student()
            elif choice == '5':
                self.list_student()
            elif choice == '6':
                print('Bye~~')
                break
            else:
                print("输入错误，请输入数字1-6!")


conn = Connection(
    host='localhost'
    , user='root',
    port=3306,
    password='136479'
    , autocommit=True
)

cursor = conn.cursor()
cursor.execute('use school')

edu = EduManagement()

edu.run()
