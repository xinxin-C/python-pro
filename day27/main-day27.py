import tkinter

window = tkinter.Tk() # 创建一个窗口
window.title("My First GUI Program")
window.minsize(width=500, height=300) #设置窗口大小

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold")) #创建一个label
my_label.pack(side='left', expand=True) #把创建的label放进window里, pack是一个排版的工具
#pack里可以调的参数写在了**kw里面，有无限的参数可以写？

import turtle

tim = turtle.Turtle()
tim.write() #write的参数里写了所有可以调的东西


window.mainloop() #让创建的窗口一直显示