# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 07:50:39 2025

@author: user
"""

Probabilitylist=[];

sumprob=0;
fail_rate=1;

ex=0;

for i in range(1,91):
    win_rate=0.006
    if(i>73):
        win_rate+=(i-73)*0.06
    elif(i==90):
        win_rate=1
    p=fail_rate*win_rate
    Probabilitylist.append(p);
    sumprob+=p;
    fail_rate=1-sumprob

    ex+=i*Probabilitylist[i-1];

print(ex)
    
"""
米池期望值計算

米池規則：中獎率為0.6%，第90抽保底中獎，如果第73抽前都未中獎，第74抽中獎機率提升6%，提升後為6.6%，之後
每多一抽都提升中獎機率6%；所以第75抽為12.6%，第76抽為18.6%...直至第90為100%


"""
    