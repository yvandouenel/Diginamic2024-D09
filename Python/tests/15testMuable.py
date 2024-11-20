hello = "Hello World"
hello.replace("l", "m")
hello = hello + " Ca va le monde ?"
print(hello)

# tuple immuable
mon_tuple = (1, 2, 3)
mon_tuple_mix = ("coucou", True, 45, [1, 2, 3])

# Comment faire pour ajouter 4 à la liste qui se trouve en dernier élément de mon_tuple_mix ?
mon_tuple_mix[3].append(4)
print(mon_tuple_mix)
