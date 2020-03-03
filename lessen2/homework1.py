
"""
利用random库，随机出100道两个数的加、减口算题。要求：
（1）a+b或者a-b，a、b和得数范围均为【0，100】，
（2）如果是加法运算，要求有进位，如果是减法运算要求有退位
（3）在屏幕中打印出结果，每行显示4道题，注意对齐
"""
import random

op=['-','+']

for i in range(25):
    for j in range(4):
        a=random.randint(0,100)
        b=random.randint(0,100)
        jia_or_jian=random.choice(op)
        if a<b:
            a,b=b,a
        if jia_or_jian=='-':
            while (a%10)>(b%10):
                if a-b<10:
                    if a<10:
                        a=a+10
                    else:
                        b=b-10
                a=a-1
            print('%3d-%2d=%3d' % (a,b,a-b),sep='',end='    ')
        if jia_or_jian=='+':
            while (a%10)+(b%10)<10:
                while a%10<9:
                    a=a+1
                while b%10<9:
                    b=b+1
            while a+b>100:
                while a>10:
                    a=a-10
                while b>10:
                    b=b-10
            print('%3d+%2d=%3d' % (a,b,a+b),sep='',end='    ')
    print()
