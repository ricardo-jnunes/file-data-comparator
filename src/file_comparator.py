import numpy as np
import difflib
import fileinput
from difflib import Differ


f1 = open('C:/Users/ricardo.nunes/Downloads/Problema_OUD/file-data-comparator/input/example_from.txt','r').readlines()
f2 = open('C:/Users/ricardo.nunes/Downloads/Problema_OUD/file-data-comparator/input/example_to.txt','r').readlines()
rf = open('C:/Users/ricardo.nunes/Downloads/Problema_OUD/file-data-comparator/output/result.txt','w+')
countf1 = len(f1)
countf2 = len(f2)

differ = Differ()

try:
#for line1 in fileinput.input(f1):
       arr = [] 

       for line1 in f1:
              count = 0
              for line2 in f2:
                     count+=1
                     if (line1 == line2):
                            if (line1 not in arr):
                                   arr.append(line1)
                                   print("line 2: " + line1 + " and " + line2 +" = break")
                                   break
                     else:
                            if count >= countf2 and (line1 not in arr):
                                   print("line 2: " + line1 + " and " + line2 +" = continue")
                                   rf.write(line1)

finally:
       rf.close()