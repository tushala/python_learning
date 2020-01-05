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


company = Company(["tushala", "tutushala", "tututushala"])
print(hasattr(company, "__len__"))

# abc模块

import abc


class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set(self, key):
        pass

    @abc.abstractmethod
    def get(self, key, value):
        pass


class RedisCache(CacheBase):
    pass

rediscache = RedisCache()