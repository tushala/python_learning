if __name__ == '__main__':
    user = type("user", (), {"name": "tushala"})
    print(user)
    print(user.name)
    print(user.__dict__)
