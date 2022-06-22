class course:
    c_id=int
    c_name=str
    c_fees=int
    def __init__(self,c_id,c_name,c_fees):
        self.c_id=c_id
        self.c_name=c_name
        self.c_fees=c_fees
    def get_course(self):
        print(self.c_id,self.c_name,self.c_fees)

c1=course("102","bca","20000")
c1.get_course()