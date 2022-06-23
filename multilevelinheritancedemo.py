class p1:
    def n1(self):
        print("inside n1")

class p2(p1):
    def n2(self):
        print("inside n2")

#multipleinheritance

class p3(p2,p1):
    def n3(self):
        print("inside n3")

p3=p3()
p3.n3()
p3.n2()
p3.n1()