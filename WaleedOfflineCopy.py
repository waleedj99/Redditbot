#the Script
import urllib.request
import json

cha=['pewdiepie','tseries']
key="AIzaSyD_wHoIHLe6yyYAbAZL4l6YDy_4iZd1vk8"
lis=list()
i=-1
for cha in cha:
    data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+cha+"&key="+key).read()
    subs=lis.append(json.loads(data)["items"][0]["statistics"]["subscriberCount"])
    


lis=[ int(x) for x in lis]


a=lis[0]-lis[1]

if(a>0):
    print("Pewdiepie is leading with [" +"{:,}".format(a) + "]9 year olds" )
else:
    print("Pewdiepie has lost the battle as T-Series is"+"{:,}".format(a)+"ahead of us")
while i<0:
    print("Pewdiepie has "+ "{:,}".format(lis[0]))
    print("T-Series has " +"{:,}".format(lis[1]))
    i=1

