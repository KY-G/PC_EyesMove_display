'''''''''''''''''''''''''''''''''2021.03.10''''''''''''''''''''''''''''''''''''''
键盘和鼠标控制滑块移动，自动移动功能未实现。
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from tkinter import *
import time

i = 0

def moverectangle(event):  # 绑定方向键
    if event.keysym == "Up":
        canvas.move(1, 0, -5)  # 移动的是 ID为1的事物【move（2,0,-5）则移动ID为2的事物】，使得横坐标加0，纵坐标减5
    elif event.keysym == "Down":
        canvas.move(1, 0, 5)
    elif event.keysym == "Left":
        canvas.move(1, -5, 0)
    elif event.keysym == "Right":
        canvas.move(1, 5, 0)
def Mouse_catch(event):
    if event.num == 1:
        print("鼠标点击有效")
        print(event.x)
        print(event.y)
    else:
        print(event)
def Rectangle_AutoMove():
    global i
    # for i in range(0, 800):
    #     canvas.move(1, 2, 0)
    #     EyeMove_window.after(500, Rectangle_AutoMove)


EyeMove_window = Tk()
EyeMove_window.title("眼动轨迹")

window_width = EyeMove_window.winfo_screenwidth()
window_height = EyeMove_window.winfo_screenheight()




canvas = Canvas(EyeMove_window, width = window_width, height = window_height*0.5) #设置画布（即滑块可显示的范围，
                                                        # .geometry范围更大的话，超出此设置范围被吃掉）
canvas.pack() #显示画布
r = canvas.create_rectangle(180,180,220,220,fill="red") # 事件ID为1
print(r) #打印ID验证一下
''' #蓝色色块
m = canvas.create_rectangle(10,10,20,20,fill="blue") #事件ID为2
print(m) #打印ID验证一下
'''
EyeMove_window.attributes("-topmost",True)
      #覆盖掉下方任务栏的全屏显示，需要置顶窗口覆盖掉所有其他窗口。
          #attributes方法中，置顶窗口的属性名为-topmost，其用法是attributes(属性名，属性值)

start_button = Button(EyeMove_window, width=20,height=2,text='开始',bg = 'black',fg = 'white',command=Mouse_catch)#设置按钮属性，text表示按钮文本，bg、fg分别表示文本和背景颜色
#start_button.grid(row=2,column=1) #放置按钮
start_button.pack()

canvas.bind_all("<KeyPress-Up>", moverectangle) #绑定方向键与函数
canvas.bind_all("<KeyPress-Down>", moverectangle)#如果绑定指定的键盘，则"<Key>" 或者"<KeyPress>"都可以，具体到指定键的话后面加入下划线和指定的键就好了
canvas.bind_all("<KeyPress-Left>", moverectangle)#如：绑定小写字母t和Left键，"<KeyPress-t>"
canvas.bind_all("<KeyPress-Right>", moverectangle)
canvas.bind_all("<Button-1>", Mouse_catch)
#canvas.bind_all("<Button-2>", Mouse_catch)
#canvas.bind_all("<Button-3>", Mouse_catch)
'''
鼠标点击事件
<Button-1>  鼠标左键
<Button-2>   鼠标中间键（滚轮）
<Button-3>  鼠标右键
<Double-Button-1>   双击鼠标左键
<Double-Button-3>   双击鼠标右键
<Triple-Button-1>   三击鼠标左键
<Triple-Button-3>   三击鼠标右键
'''
EyeMove_window.mainloop() #窗口继续执行和等待
