from math import sqrt
from math import floor
import time
__author__ = 'Adam'


def generateTriangle(n):
    sum=0
    for i in range(n):
        sum+=i+1
    return sum

def addtotriangle(number,index):
    return number+index+1

def getDivisors(n):
    numofDiv=0
    for i in range(floor(sqrt(n))):
        if i!=0:
            if n%i==0:
                numofDiv+=2

    if sqrt(n).is_integer():
        numofDiv+=1
    return numofDiv

def main():
    cond=True
    i=1
    value=1
    while(cond):
        value=addtotriangle(value,i)
        a=getDivisors(value)
        if a >=500:
            cond=False
            print(value)
        i+=1
if __name__ == '__main__':
    t=time.time()
    main()
    print(time.time()-t)