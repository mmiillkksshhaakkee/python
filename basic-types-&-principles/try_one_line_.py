f = ["apple", "pear", "cherry"]

#f[2:2], f[4:] = [['peach']]*2
f += ['peach', f.pop(), 'peach']
print(f)