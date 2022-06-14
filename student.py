student={"name":"john","age":18,"class":12,"course":"cs"}
print(student["name"])
print(student["course"])
print(student["age"])

print("dob" in student)
# inserting new item
student["dob"]=2000
print(student)

# update value
student["class"]=11
print(student)