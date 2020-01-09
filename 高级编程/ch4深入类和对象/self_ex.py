"""python 自省"""


class Person:
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("慕课网")
    # print(user.__dict__)
    # user.__dict__["location"] = "海淀区"
    print(Person.__dict__)
    # print(user.name)  # name 不是student属性, 是
    # print(user.location)
    # print(dir(user))  # 列出所有属性

    # print(dir([1, 2]))