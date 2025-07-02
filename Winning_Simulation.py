# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 09:54:34 2025

@author: user
"""
import random

class Lottery_Machine():
    count=0;
    def _init_(self):
        self.count=0;
    def draw(self,number):
        if(self.count>73):
            if(number<=6+(self.count-73)*60):
                return self.winning();
            return self.fail();
        elif(self.count==90):
            return self.winning();
        if(number<=6):
            return self.winning();
        return self.fail()
    def winning(self):
        self.count=0;
        return True;
    def fail(self):
        self.count+=1;
        return False;

Lottery_Machine=Lottery_Machine();
draw=500;
log=[];

for i in range(1,draw):

    number=random.randint(1, 1000);
    if(Lottery_Machine.draw(number)==True):
        log.append(i);

print(log);
if(len(log)>0):
    ex=draw/len(log)
    print("%.3f"%ex)
       