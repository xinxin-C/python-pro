import tkinter
from tkinter import *

window = tkinter.Tk()  # 创建一个窗口
window.title("My First GUI Program")
window.minsize(width=500, height=300)  # 设置窗口大小

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))  # 创建一个label
my_label.pack()  # 把创建的label放进window里, pack是一个排版的工具
# pack里可以调的参数写在了**kw里面，有无限的参数可以写？

# 以下两种方式和上面直接定义的时候设置text都可以改变text的值，都可以用
my_label["text"] = 'New Text'
my_label.config(text="New Text")


def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked")


# Button
button = Button(text='Click me', command=button_clicked)  # command写点了这个按钮之后要干嘛
button.pack()

# Entry

input = Entry(width=10)
input.pack()

window.mainloop()  # 让创建的窗口一直显示
