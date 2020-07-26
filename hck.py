from __future__ import division
from itertools import starmap,compress
from operator import mul
import fractions



def convertmatrix(transmatrix):
    probmatrix=[]
    for i in range(len(transmatrix)):
        row=transmatrix[i]
        newrow=[]
        rowsum=sum(row)
        if(all([v==0 for v in row])):
            for j in row:
                newrow.append(0)
            newrow[i]=1
            probmatrix.append[newrow]
        else:
            for j in row:
                if(j==0):
                    newrow.append(0)
                else:
                    newrow.append(j/rowsum)
            probmatrix.append(newrow)
    return probmatrix

def terminalfilter(matrix):
    terminals=[]
    for i in range(len(matrix)):
        if(all(x==0 for x in matrix[i])):
            terminals.append(True)
        else:
            terminals.append(False)
    return terminals

def probdist(matrix,row,steps):
    vector=matrix[row]
    for i in range(steps):
        newvector=list(sum(starmap(mul,zip(vector,col)))for col in zip(*matrix))
        vector=newvector
    return vector

def solution(m):
    if(len(m)==1):
        return[1,1]
    probmatrix=convertmatrix(m)
    terminals=terminalfilter(m)
    probvector=probdist(probmatrix,0,100)
    numerators=[]
    for i in probvector:
        numerator = fractions.Fraction(i).limit_denominator().numerator
        numerators.append(numerator)
    denominators=[]
    for i in probvector:
        denominator = fractions.Fraction(i).limit_denominator().numerator
        denominators.append(denominator)
    factors=[max(denominators)/x for x in denominators]
    numeratorstimefactors=[a*b for a, b in zip(numerators,factors)]
    terminalsnumerators=list(compress(numeratorstimefactors,terminals))
    res=[]
    for i in terminalsnumerators:
        res.append(i)
    res.append(max(denominators))
    
    return list(map(int,res))


m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print(solution(m))