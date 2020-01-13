# dict 操作
new_list = ["bobby1", "bobby2"]
new_dict = dict.fromkeys(new_list, {"company": "imooc"})  # fromkeys
print(new_dict)

x = new_dict.setdefault("name", "tushala")  # setdefault
print(new_dict, x)
new_dict.update([("x", "y"), ("x1", "y1")])  # update
print(new_dict)
