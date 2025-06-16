ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_est = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

tmp_list = list(ft_tuple)
tmp_list[1] = "Portugal!"
ft_tuple = tuple(tmp_list)

ft_est.remove("tutu!")
ft_est.update({"Lisboa!"})

ft_dict["Hello"] = "42Lisboa!"

print(ft_list)
print(ft_tuple)
print(ft_est)
print(ft_dict)