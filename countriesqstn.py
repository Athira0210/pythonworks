import json
with open("countries.json",encoding="utf") as f:
    data=json.load(f)

#print total number of country details
# print(len(data))


#print languages of ukraine
# ukrn_lan=[country["languages"] for country in data if country["name"]=="Ukraine"]
# for lan in ukrn_lan[0]:
#     print(lan["name"])
# print(ukrn_lan)



#print currency of PALESTINE
# cur_details=[country["currencies"] for country in data if country["name"].lower().startswith("palestine")]
# cur_details=[country["currencies"] for country in data if country["name"].startswith("Palestine")]
# curr_name=[details.get("name") for details in cur_details[0]]
# print(curr_name)
# # print(cur_details)



#print population of india
# pop_ind=[country["population"] for country in data if country["name"]=="India"]
# print(pop_ind)


#print neighbouring countries of australia

# astr=[country["borders"] for country in data if country["name"]=="Australia" ]
# print(astr)

#neighbouring countries of india
# def get_country(country_name):
#     return[country for country in data if country["name"].lower().startswith(country_name)]
#
# india_data=get_country("india")
# country_borders=india_data[0].get("borders")
# print(country_borders)
# sharing_borders=[country.get("name")for country in data if country["alpha3Code"] in country_borders]
# print(sharing_borders)

#highest population

high_population=max(data,key=lambda d:d.get("population"))
print(high_population["name"])

min_population=min(data,key=lambda d:d.get("population"))
print(min_population["name"])


