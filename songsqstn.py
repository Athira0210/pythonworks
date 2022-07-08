import json

import functools

import random

#print total number of songs in album1
with open("songs.json",encoding="utf")as f:
     data=json.load(f)
 #    print(data)
#
# num_songs=[song for song in data if song["album"]=="album1"]
# print(len(num_songs))
#
# albm_sng_count=list(filter(lambda song:song["album"]=="album1",data))
# print(len(albm_sng_count))

#print largest rating song

# top_songs=max(data,key=lambda s:s["rating"])
# print(top_songs["rating"])
#
# top_songs=[s for s in data if s["rating"]==top_songs["rating"]]
# print(top_songs)


# t_songs=functools.reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2 ,data)
# print(t_songs)

#random sampleof 2 sad songs

# rand_sample=[song for song in data if song["mode"]=="sad"]
# print(random.sample(rand_sample,2))

#total no of album

# total_album=set([song["album"]for song in data])
# print(len(total_album))

#which album contain most songs

sc={}

for song in data:
    album_name=song.get("album")
    if album_name in sc:
        sc[album_name]+=1
    else:
        sc[album_name]=1
print(sc)

print(max(sc.items(),key=lambda s:s[1]))