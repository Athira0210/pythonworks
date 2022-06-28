class Course:
    course_name:str
    active_status:bool
    def __init__(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")

    def __str__(self):
        return self.course_name


class Batch:
    course:Course
    batch_code:str
    start_date:str

    def __init__(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code




class Student:
    student_name:str
    gender:str
    rol:str
    batch:Batch

    def __init__(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.rol=kwargs.get("rol")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.student_name


django=Course(course_name="django",active_status=True)

bigdata=Course(course_name="bigdata",active_status=True)

db1=Batch(course="django",batch_code="abc",start_date="2-2-2022")
bb1=Batch(course="bigdata",batch_code="abc",start_date="3-3-2022")

print(db1)

rahul=Student(student_name="rahul",gender="male",rol="12",batch=db1)
akhil=Student(student_name="akhil",gender="male",rol="14",batch=db1)
rithu=Student(student_name="rithu",gender="female",rol="16",batch=bb1)
meenu=Student(student_name="meenu",gender="female",rol="18",batch=bb1)

print(akhil.batch.course)



