# num1=int(input("enter num1:"))
# num2=int(input("enter num2:"))
#
# try:
#     res=num1/num2
# except Exception as e:
#     num2=int(input("enter num2:"))
#     print(num1/num2)
#
# finally:
#     print("line1")
#     print("line2")

# age=int(input("enter num1:"))
#
# if(age<18):
#     raise Exception("not eligible for taking booster dose")
# else:
#     print("eligible")

phonenum=len(input("enter number:"))

if(phonenum!=10):
    raise Exception("invalid phone number")
else:
    print("valid")

#try : block doubtfull code
#except: b handling code
#finally:b cleanup process
#raise: throwing custom exception