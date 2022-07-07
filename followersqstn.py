import json
import random

try:
    with open("followers.json",encoding="utf") as f:
      data=json.load(f)
      print(data)

    all_users=[user["id"]for user in data]
    my_following=[user["followers"]for user in data if user["username"]=="akhil"][0]
    my_id=[user["id"]for user in data if user["username"]=="akhil"].pop()
    to_follow=set(all_users)-set(my_following)
    to_follow.remove(my_id)
    print(to_follow)
    suggestions=random.sample([*to_follow],2)
    print(suggestions)


except Exception as e:

    print(e.__class__)

#destructring

lst=[10,20,30,40,50]
st={*lst}
print(st)