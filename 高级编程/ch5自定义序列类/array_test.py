import array

# array 全部为相同类型数据

my_array = array.array("i")  # 存放为int数据类型
my_array.append(1)
my_array.append("abc")  # TypeError: an integer is required (got type str)


# 在list中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据
