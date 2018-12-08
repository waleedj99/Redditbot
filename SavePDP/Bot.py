#for Reddit
#pip install request,requests,json,praw
import praw
import json
import urllib.request
import re
print("start")
def check():
    cha=["UC-lHJZR3Gqxm24_Vd_AJ5Yw","UCq-Fj5jknLsUf-MWSy4_brA","UCEgdi0XIXXZ-qJOFPf4JSKw"]
    #Namecha=['pewdiepie','tseries','ytsports'] #name of youtube channels
    key="AIzaSyD_wHoIHLe6yyYAbAZL4l6YDy_4iZd1vk8" #Youtube Api
    lis=list()
    
    for cha in cha:
        data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+cha+"&key="+key).read()
        subs=lis.append(json.loads(data)["items"][0]["statistics"]["subscriberCount"])
   
    lis=[ int(x) for x in lis] #converting sub count to int type
    

    a1=lis[0]-lis[1]#differnce between pewds and T series
    a2=lis[2]-lis[0]# differnce between Yt sports and pewds 
    if(a1>0):
        if(a2>0):
             comment.reply("Pewdiepie is ahead of T-Series by " + "{:,}".format(a1) + " subs and requires only  "+"{:,}".format(a2)+" more subs to beat Youtube Sports!"+
                      "  \nYoutube sports:"+" \t\t" + "{:,}".format(lis[2])+' \t '+" \nPewdiepie :\t\t" + "{:,}".format(lis[0])+'\t'+"  \nT-Series :\t\t" + "{:,}".format(lis[1])+'\t'+"\n\n I am a bot. \nFor further information please use '! help' (without the space) to mention the owners for any feedback ")
        else:
            a2=lis[0]-lis[2]
            comment.reply("Pewdiepie is now the king by being ahead of Youtube sports by" + "{:,}".format(a2) + " nine year olds. "+" \nPewdiepie :  " + "{:,}".format(lis[0])+"  \nYoutube sports:  " + "{:,}".format(lis[2])+" \nT-Series :  " + "{:,}".format(lis[1])+"\n\n\ Use \'! help' (without the space) to mention the owners for any feedback ")
        
            
        #print("posted")#for my console for me to keep a count
    #if(a1>0 and a2>0):
        #comment.reply("Pewdiepie is ahead of T-Series by " + "{:,}".format(a1) + " subs and requires only  "+"{:,}".format(a2)+" more subs to beat Youtube Sports!"+
                      #" \nPewdiepie :  " + "{:,}".format(lis[0])+"  \nYoutube sports:  " + "{:,}".format(lis[2])+"  \nT-Series :  " + " {:,}".format(lis[1])+"\n\n I am a bot for further information please use '! help' (without the space) to mention the owners for any feedback ")
        
        #print("posted")#for my console for me to keep a count
    #elif(a1>0 and a2<0):
        #a2=lis[0]-lis[2] #used this so that it doesnt print the differnce in negative
        #comment.reply("Pewdiepie is now the king by being ahead of Youtube sports by" + "{:,}".format(a2) + " nine year olds. "+" \nPewdiepie :  " + "{:,}".format(lis[0])+"  \nYoutube sports:  " + "{:,}".format(lis[2])+" \nT-Series :  " + "{:,}".format(lis[1])+"\n\n\ Use \'! help' (without the space) to mention the owners for any feedback ")
        #print("postedS")
    else:
        comment.reply("Pewdiepie has lost the battle as T-Series is"+ "{:,}".format(a1)+" subs ahead")
        print("posted") #for my console for me to keep a count
    
searchkey = re.compile(r'!PewdStatus|!PewdBot|/u/PewdStatus|!pewdstatus|!pewdbot|!Pewdbot|!Pewdstatus')#my stuff
Help=re.compile(r'!help|!Help')
debugkey = re.compile(r'!pewdbotgetcommanddata')
reddit=praw.Reddit(client_id="2T256yp2KjjJOQ", #Reddit Api
                   client_secret="z3FUDDpgi6n4ZLPdm4Ze2kdnC5Q", #Reddit Api
                   user_agent="PewdStatus bot (by /u/ashfaq_haq)",
                   username="PewdStatus",
                   password="pewdiepiebot")
subreddit = reddit.subreddit('PewdiepieSubmissions')
CommentList= []
Keyused = []
with open('file.txt','a+') as file:
    content = file.readlines()
    CommentList = [x.strip() for x in content]
    print(CommentList)
file = open("file.txt",'a+')
#CommentList.append(file.readlines());
#Trigger phrases
#key="!PewdStatus" or "!PewdBot" or"/u/PewdStatus"
for comment in subreddit.stream.comments():
    #print(searchkey.search(comment.body))
    #print(comment.body)
    if(debugkey.search(comment.body)):
        print("reading file")
    if searchkey.search(comment.body) and comment not in CommentList :#my stuff
        Keyused.insert(0,''.join(searchkey.findall(comment.body)))
        KeyFile = open("keyfile.txt",'a+')
        #KeyFile.append(Keyused + "\n")
        file = open("file.txt",'a+')
        file.writelines(str(comment)+"\n")
        check()
        CommentList.insert(0,comment)
        print(Keyused)
        file.close()
    if Help.search(comment.body) and comment not in CommentList:
        
        KeyFile = open("keyfile.txt",'a+')
        comment.reply("/u/waleedj99 and /u/ashfaq_haq")
        file = open("file.txt",'a+')
        file.writelines(str(comment)+"\n")
        CommentList.insert(0,comment)
        #print(Keyused)
        file.close()
        print("help command")
        

