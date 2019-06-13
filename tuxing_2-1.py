# -*- coding: utf-8 -*-
# version 1.1 is finally edition.

import tkinter as tk

myw=[]       #输入数组
value=[]      #转换后的值
myresult=[]  #输出数组

window = tk.Tk()
window.title('数独解法')
window.geometry('500x300')  # 这里的乘是小x
frame = tk.Frame(window)
frame.pack()
try_queue=[]        #尝试的解法，采用后进先出的方法进行管理，错误时进行回退
for k in range(9):
    value.append([[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]])

for myi in range(81):
    myw.append(tk.StringVar())

def value_judge(mycol1,myrow1,my_value1):
    while my_value1<10:
        if value_valid(mycol1,myrow1,my_value1)==0:
            my_value1=my_value1+1
        else:
            return my_value1
    if my_value1==10:
        return 0

def value_valid(mycol,myrow,my_value):
    if my_value not in (
    value[mycol][1][1], value[mycol][2][1], value[mycol][3][1], value[mycol][4][1], value[mycol][5][1],
    value[mycol][6][1], value[mycol][7][1], value[mycol][8][1], value[mycol][0][1]):
        if my_value not in (
        value[0][myrow][1], value[1][myrow][1], value[2][myrow][1], value[3][myrow][1], value[4][myrow][1],
        value[5][myrow][1], value[6][myrow][1], value[7][myrow][1], value[8][myrow][1]):
            my_i = (mycol) // 3 * 3
            my_j = (myrow) // 3 * 3
            if my_value not in (
            value[my_i][my_j][1], value[my_i][my_j + 1][1], value[my_i][my_j + 2][1], value[my_i + 1][my_j][1],
            value[my_i + 1][my_j + 1][1], value[my_i + 1][my_j + 2][1], value[my_i + 2][my_j][1],
            value[my_i + 2][my_j + 1][1], value[my_i + 2][my_j + 2][1]):
                return my_value
    return 0

def init_judge():
    for myt in range(9):
        for myp in range(9):
            kk_value = value[myt][myp][1]
            if kk_value>0:
                if value_valid(myt,myp,kk_value)==0:
                    return 0
    return 1


#如果第一个都没有则返回0，否则返回1
def value_try():
    i=0
    while i<9:
        j=0
        while j<9:
            if value[i][j][0]==0:                               #如果是固定值则继续
                j+=1
                continue
            my_result=value_judge(i,j,value[i][j][1])          #如果判断符合标准则加入符合队列
            value[i][j][1] = my_result                          #更新列表值，符合则为实际值，否则重置为0
            if my_result>0:
                try_queue.append([i, j])
                j+=1
            elif len(try_queue)==0:
                #print("no answers, please check the input")
                return 0                                       #如果第一个数就找不到则出错
            else:                                               #继续循环查找这个元素的可能值
                i=try_queue[-1][0]
                j=try_queue[-1][1]
                del try_queue[-1]
        i+=1
    return 1

#my_var=tk.StringVar()
#l = tk.Label(window, textvariable=my_var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
#l.pack()
#my_var.set("this is test")

def test(content):
    return content.isdigit()

testCMD = frame.register(test)



def value_output():
    for a in range(81):
        r1=a//9
        c1=a%9
        c2=c1+13
        l1 = tk.Label(frame, text=str(value[r1][c1][1]), font=('Arial', 12), width=1)
        l1.grid(row=r1,column=c2)

# 将问题中的初始数值读入到元组列表中
for j in range(81):
    e1=tk.Entry(frame, width=1, font=('Arial', 14),textvariable=myw[j], validate='key',validatecommand=(testCMD, '%P'))
    i=(j)%9
    myk=(j)//9
    e1.grid(row=myk, column=i)


def tick_me():
    for i1 in range(81):
        i2=i1//9
        j2=i1%9
        if myw[i1].get().isdigit():
            value[i2][j2][0]=0
            value[i2][j2][1]=int(myw[i1].get()[-1])
#    if init_judge()==0:
#        return
    value_try()
    value_output()

b = tk.Button(window, text='start', font=('Arial', 12), width=10, height=1, command=tick_me)
b.pack()
#c = tk.Button(window, text='output',font=('Arial', 12), width=10, height=1, command=value_output)
#c.pack()

window.mainloop()