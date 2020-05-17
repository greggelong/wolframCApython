#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:46:41 2020

@author: gregk

 Wolfram rules are just binary numbers
 eg rule 30 = 00011110  is just 30 in binary
   
  but when we are looking at neighbors and truning and converting their binary
  values to a decimal index 0 -7  they are reversed 
  example: 111 gives us the 128 rule which is in our list index 0 
   binary 111 is 7 so we much subtract to get the right index. 

"""
#rules = [0, 0, 0, 1, 0, 0, 1, 0] #18
#rules = [0, 1, 0, 0, 1, 0, 0, 1]  #73

rules = [0, 0, 0, 1, 1, 1, 1, 0]  #30

ca = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def showCA(cellMatrix):
    for i in cellMatrix:
        #print("".join(str(x)for x in i))
        #using list comprehension to change 0 to . and 1 to x
        cellprint = ['.' if x == 0 else 'X' for x in i] 
        print("".join(cellprint))
        
        
def nextGen(cellMatrix,numGen):
    for i in range(1,numGen):
        
        for gen in cellMatrix:
            nextGen =[]
            for cell in range(0,len(gen)):  #use modulo to wrap the gen of cells around
                left = gen[(cell-1)%len(gen)]     # it is as if it is a cylinder
                middle = gen[cell%len(gen)]
                right = gen[(cell+1)%len(gen)]
                #get a binary number, convert it to decimal, sub from 7
                strIndex = str(left)+str(middle)+str(right)
                minIndex = int(strIndex,2)
                rindex = 7 - minIndex
                #this is the right index for the rules
                if rules[rindex] == 1:
                    nextGen.append(1)
                else:
                    nextGen.append(0)
            
        ca.append(nextGen)
    
            



nextGen(ca,30)
showCA(ca)
        