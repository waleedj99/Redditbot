#the Script
import urllib.request
import json
p="UC-lHJZR3Gqxm24_Vd_AJ5Yw"
t="UCq-Fj5jknLsUf-MWSy4_brA"
sp="UCEgdi0XIXXZ-qJOFPf4JSKw"
cha=["UC-lHJZR3Gqxm24_Vd_AJ5Yw","UCq-Fj5jknLsUf-MWSy4_brA","UCEgdi0XIXXZ-qJOFPf4JSKw"]
#cha2=[p,t,sp]
key="AIzaSyD_wHoIHLe6yyYAbAZL4l6YDy_4iZd1vk8"
lis=list()
i=-1
for cha in cha:
    data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+cha+"&key="+key).read()
    subs=lis.append(json.loads(data)["items"][0]["statistics"]["subscriberCount"])
    


lis=[ int(x) for x in lis]


a1=lis[0]-lis[1]
a2=lis[2]-lis[1]
if(a1>0):
    print("Pewdiepie is leading with " +"{:,}".format(a1) + " nine year olds \n Pewds is "+ str(a2)+" behind YT sports" )
    #print("Pewds is "+ str(a2) +"behind YT sports" )
else:
    print("Pewdiepie has lost the battle as T-Series is"+"{:,}".format(a)+"ahead of us")

print("Pewdiepie has "+ "{:,}".format(lis[0]))
print("T-Series has " +"{:,}".format(lis[1]))
print("Yt sports " +"{:,}".format(lis[2]))
    
   

