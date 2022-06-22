class student:
    name: str
    rollno: int
    course: str
    #instance variable

    def __init__(self, name, rollno, course):
        #initializing instance variable
        self.name = name
        self.rollno = rollno
        self.course = course

    def print_student(self):
        print(self.name, self.rollno, self.course)


s1 = student("athira","2","bca")

s1.print_student()


#course c_id,c_name,c_fees