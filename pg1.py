#lst=[10,20,10,30,40,20,30]

#st=set(lst)
#print(st)

#st1={1,2,3}
#st2={3,4,5,6}

#union_set=st1.union(st2)
#print(union_set)

#intersection_set=st1.intersection(st2)
#print(intersection_set)

#difference_set=st1.difference(st2)
#print(difference_set)

students=["ram","ravi","hari","tom","nikhil","jain","john"]
passed_students=["ravi","hari","tom"]

failed_students=set(students).difference(set(passed_students))
print(failed_students)