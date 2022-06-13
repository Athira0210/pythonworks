mobiles=[
    [1000,"samsungA52","4g","AMOLED",27000,"samsung",12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung",20],
    [1002, "redminote10", "4g", "led", 17000, "redmi",50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi",70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung",1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung",34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67]

]
# q1 no of mobiles
#print(f"total number of moblie ={len(mobiles)}")

#q2 total out_of_stock
#out_of_stock=[mob for mob in mobiles if mob[-1]==0]
#print(out_of_stock)

#q3 print mobiles available in range 20k to 30k
#mobiles_gt=[mob for mob in mobiles if mob[4] in range(20000,30000)]
#print(mobiles_gt)

#q4 print all 5g mobiles
#fiveg_mobiles=[mob for mob in mobiles if mob[2]=="5g"]
#print(fiveg_mobiles)

#q5 print costly mobiles
#mobiles.sort(reverse=True,key=lambda mob:mob[4])
#print(mobiles)
#0r
#costly_mob=max(mobiles,key=lambda mob:mob[4])
#print(costly_mob)

#q6 is there is any mobiles is available in 10000
#mob_ten=[mob[4]==1000 for mob in mobiles]
#print("available" if True in mob_ten else"na")

#q7 list all mobiles having same price
