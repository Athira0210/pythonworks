import json

with open("blogs.json",encoding="utf-8")as f:
    data=json.load(f)
print(len(data))

#number of post by userid=1

post_user1=[post for post in data if post["userId"]==1]
print(len(post_user1))

#total number of likes for postid=6
post6_likes=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(post6_likes)

# number of post like by user2
user2_like=len([post for post in data if 2 in post["liked_by"]])
print(user2_like)