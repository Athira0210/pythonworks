#2 sum pairs 8

lst=[3,4,5,6,2]
sum=8
res=[]

def findpairs(lst,sum):

    while lst:
        num=lst.pop()
        diff=sum-num
        if diff in lst:
            res.append((diff,num))
    return res
print(findpairs(lst,sum))

#3 sum pair 9[4.3,2]
lst=[3,4,5,6,2]
sum=9
res=[]

def findpairs(lst,sum):

    while lst:
        num=lst.pop()
        diff=sum-num
        if diff in lst:
            res.append((diff,num))
    return res
print(findpairs(lst,sum))

#            12[3,4,5][6,4,2]