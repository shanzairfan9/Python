Str = "My name is Shanza Irfan"
Str1 = "     "
rows =20
pre = ""
for i in range(0, rows, 5):
    pre = ""
    for j in range(i):
        pre = "\t" + pre
        print(pre + Str)
