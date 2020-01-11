import numbers


# 自定义可切片序列

class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):  # 调用reversed()
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)  # 获取当前类 <class '__main__.Group'>
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name="imooc", staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name="imooc", staffs=[self.staffs[item]])

        return self.staffs[item]

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        iter(self.staffs)

    def __contains__(self, item):
        return item in self.staffs


if __name__ == '__main__':
    staffs = ["jinshala", "shuishala", "huoshala", "tushala"]
    group = Group(company_name="imooc", group_name="user", staffs=staffs)
    print(group[:2].__dict__)

     