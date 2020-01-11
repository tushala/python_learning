import array

# array 全部为相同类型数据

my_array = array.array("i")  # 存放为int数据类型
my_array.append(1)
my_array.append("abc")  # TypeError: an integer is required (got type str)
