accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]
#q1 print details of 1002

# for ac in accounts:
#     if ac["acno"]==1002:
# to remone transaction from acno 1002
#         transactions=ac.pop("transactions")
#         print(ac)

#ac_details=[ ac["acno"] for ac in accounts if ac["acno"]==1002]

#q2 print savings type acnt deatails

#savings_type=[ ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
#print(savings_type)

#q3 sort accounts based on balamce order by
#accounts.sort(reverse=True,key=lambda ac:ac["balance"])
#print(accounts)

#q4 print all phn pay transactions

# all_transaction=[ac["transactions"]for ac in accounts]
# phone_pay=[trans for tlist in all_transaction for trans in tlist if trans["method"]=="phone-pay"]
# print(phone_pay)


# #q5 print all transactions where transction amnt >500
# amount_gt_fi=[trans for tlist in all_transaction for trans in tlist if trans["amount"]>500]
# print(amount_gt_fi)



#q6 credit transaction of 1002

# all_transaction=[ac["transactions"]for ac in accounts]
# credit_trans=[trans for tlist in all_transaction for trans in tlist if trans["to"]>1002]
# print(credit_trans)



#q7 aggregate transaction based on mode

# pms={}
# all_transaction=[ac["transactions"]for ac in accounts]
# transactions=[t for tlist in all_transaction for t in tlist]
# for transaction in transactions:
#     p_method=transaction["method"]
#     amount=transaction["amount"]
#     if p_method in pms:
#         pms[p_method]+=amount
#     else:
#         pms[p_method]=amount
# print(pms)

#print max trans

#print(max(pms.items(),key=lambda ite:ite[1]))