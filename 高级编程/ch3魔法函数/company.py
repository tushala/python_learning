"""
__getitem__
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __repr__(self):
        # 面向开发者
        return "\t".join(self.employee)

    __str__ = __repr__  # 面向客户


company = Company(["tushala", "tutushala", "tututushala"])
for em in company:
    print(em)

print(company[:2])
print(len(company[:2]))
print(len(company))  # TypeError: object of type 'Company' has no len()
print(repr(company))
