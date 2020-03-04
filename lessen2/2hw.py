


import random



total_num=0
op=['-','+']
while True:
    a=random.randint(0,100)
    b=random.randint(0,100)
    c_op=random.choice(op)
    if c_op=='+':
        while (a%10)+(b%10)<10 or a+b>100:
            a=random.randint(0,100)
            b=random.randint(0,100)
        print('%3d+%2d=%3d' % (a,b,a+b),sep='',end='\t')
        total_num=total_num+1
        if total_num%4==0:
            print()
        if total_num==100:
            break
    if c_op=='-':
        while (a%10>=b%10) or (a-b<0):
            a=random.randint(0,100)
            b=random.randint(0,100)
        print('%3d-%2d=%3d' % (a,b,a-b),sep='',end='\t')
        total_num=total_num+1
        if total_num%4==0:
            print()
        if total_num==100:
            break




