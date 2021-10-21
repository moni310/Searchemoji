import json
with open("emoji.json","r") as f:
    m=json.load(f)
# print(m)
title=input("enter your title---------")
i=0
while i<len(m):
    if m[i]["title"]==title:
        print(m[i]["symbol"])
        print(m[i]["keywords"])
    i=i+1
