import tkinter as tk
from tkinter import ttk


def getSave():
    f = open("a.txt", "+a")
    f.write("\n")
    f.write(str(v1.get()))
    f.write(",")
    f.write(v2.get())
    f.write(",")
    f.write(str(v3.get()))
    f.write(",")
    if radVar.get() == 1:
        f.write("man")
    else:
        f.write("woman")


win = tk.Tk()
win.geometry("+400+200")
win.minsize(800,400)
# 文本
v1 = tk.StringVar()
number = ttk.Entry(win, width=12, textvariable=v1)
number.grid(column=1, row=0)
v2 = tk.StringVar()
name = ttk.Entry(win, width=12, textvariable=v2)
name.grid(column=1, row=1)
# 下拉框
v3 = tk.StringVar()
age = ttk.Combobox(win, width=10, textvariable=v3)
age['values'] = (18, 19, 20, 21, 22, 23)
age.grid(column=1, row=2)
age.current(0)
age.focus()
# 单选框
radVar = tk.IntVar()
a = tk.Radiobutton(win, text="男", variable=radVar, value=1)
a.grid(column=1, row=3, sticky=tk.W, columnspan=3)
b = tk.Radiobutton(win, text="女", variable=radVar, value=2)
b.grid(column=2, row=3, sticky=tk.W, columnspan=3)
# 按钮
save = ttk.Button(win, text="保存", command=getSave)
save.grid(column=0, row=10)
# 标签
number_ = ttk.Label(win, text="学号")
number_.grid(column=0, row=0)
name_ = ttk.Label(win, text="名字")
name_.grid(column=0, row=1)
age_ = ttk.Label(win, text="年龄")
age_.grid(column=0, row=2)
gender_ = ttk.Label(win, text="性别")
gender_.grid(column=0, row=3)
win.mainloop()
