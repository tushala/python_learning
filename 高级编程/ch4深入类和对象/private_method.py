from datetime import datetime


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2019 - self.__birthday.year


if __name__ == '__main__':
    user = User(datetime(1991, 2, 3))
    # print(user.__birthday)  # "私有属性不允许访问"
    # print(user._User__birthday)
    print(user.get_age())
