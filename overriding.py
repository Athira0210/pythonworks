# class parent:
#     def phone(self):
#         print("redminote10 ")
#     def bike(self):
#         print("passion pro")
#
# class child(parent):
#     def phone(self):
#         print("iphone 12")
#     def bike(self):
#         print("duke")
#
# ch=child()
# ch.phone()
# ch.bike()




#in dictnory

# class parent:
#     def properties(self):
#         self.props={"mobile":"nokia","bike":"passionpro"}
#         return self.props
# class child(parent):
#     def properties(self):
#         props=super().properties()
#         props["car"]="swift"
#         return props
#
# ch=child()
# print(ch.properties())


#in list

class editor:
    def functionalities(self):
        self.funcs=["ceatenewfile","execute","save"]
        return self.funcs

class pycharm(editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["debug","versioncontrolling"])
        return funcs

pyc=pycharm()
print(pyc.functionalities())