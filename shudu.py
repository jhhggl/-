# -*- coding: utf-8 -*-

# 数独解法

# 变量定义, 变量名是指行号，其中的列表[x,x]，第一位是可修改位，1是可修改，0是不可修改 第二位是实际的值
value=[]            #整个数独列表
# 每个元素包括二个值 [行，列]
try_queue=[]        #尝试的解法，采用后进先出的方法进行管理，错误时进行回退

for k in range(9):
    value.append([[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]])

# 将结果按照格式输出
def value_output():
    for a in range(9):
        for b in range(9):
            if b == 8:
                print(value[a][b][1])
                continue
            print(value[a][b][1],end=',')

#判断现有数值是否符合规则“横竖及宫格中均无此数”
#如果没有合适的值则返回0，如果合适则返回对应的数值（大于0的值）
def value_judge(mycol,myrow,my_value):
    while my_value<10:
        if my_value not in (value[mycol][1][1],value[mycol][2][1],value[mycol][3][1],value[mycol][4][1],value[mycol][5][1],value[mycol][6][1],value[mycol][7][1],value[mycol][8][1],value[mycol][0][1]):
            if my_value not in (value[0][myrow][1],value[1][myrow][1],value[2][myrow][1],value[3][myrow][1],value[4][myrow][1],value[5][myrow][1],value[6][myrow][1],value[7][myrow][1],value[8][myrow][1]):
                my_i=(mycol)//3*3
                my_j=(myrow)//3*3
                if my_value not in (value[my_i][my_j][1],value[my_i][my_j+1][1],value[my_i][my_j+2][1],value[my_i+1][my_j][1],value[my_i+1][my_j+1][1],value[my_i+1][my_j+2][1],value[my_i+2][my_j][1],value[my_i+2][my_j+1][1],value[my_i+2][my_j+2][1]):
                     return my_value
        my_value=my_value+1
    if my_value==10:
        return 0

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
                print("no answers, please check the input")
                return 0                                       #如果第一个数就找不到则出错
            else:                                               #继续循环查找这个元素的可能值
                i=try_queue[-1][0]
                j=try_queue[-1][1]
                del try_queue[-1]
        i+=1
    return 1

# 将问题中的初始数值读入到元组列表中
def input_value(my_input_file):
    i=0
    with open(my_input_file, 'r', encoding='utf-8') as st:
        for my_line in st.readlines():
            try:
                my_line=my_line.strip()
                my_list=my_line.split(',')
                for j in range(9):
                    if my_list[j]!='0':
                        value[i][j][0]=0        #有固定数值，则标志位为0，表示不可修改
                        value[i][j][1] = int(my_list[j])
                        continue
                i=i+1
            except:
                print("read error")
                continue



def main():
    input_file1 = 'D:/game1.csv'
    input_value(input_file1)
    value_try()
    value_output()
main()
