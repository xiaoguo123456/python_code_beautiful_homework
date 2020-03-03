"""
求解所有由两个四位数组成的亲和数。
两个正整数a，b，a所有的真因数之和等于b，同时b所有的真因数之和等于a。
"""
import numpy as np

zhenyinshu={}

def sum_yinshu(n):
    a=[]
    for i in range(1,n):
        if n%i==0:
            a.append(i)
    return sum(a)
    
for i in range(1000,10000):
    if i in zhenyinshu.values():
        continue
    y=sum_yinshu(i)
    if i==sum_yinshu(y):
        if y>=1000 and y<=9999:
            zhenyinshu.update({i:y})

for a in zhenyinshu.items():
    print(a)
    
