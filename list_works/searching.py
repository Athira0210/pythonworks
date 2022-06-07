lst=[10,11,12,4,15,16]
element=15

flag=0
#for num in lst:
#    if element==num:
 #       flag=1
 #       break
#print("element found" if flag!=0 else "not found")

for i in range(0,len(lst)):
    if element==lst[i]:
        flag=1
        break
print("element found" if flag!=0 else "element not found")
