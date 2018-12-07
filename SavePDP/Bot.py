#for Reddit
#pip install request,requests,json,praw
import praw
import json
import urllib.request
import re
print("start")
def check():
    cha=['pewdiepie','tseries'] #name of youtube channels
    key="AIzaSyD_wHoIHLe6yyYAbAZL4l6YDy_4iZd1vk8" #Youtube Api
    lis=list()
    
    for cha in cha:
        data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+cha+"&key="+key).read()
        subs=lis.append(json.loads(data)["items"][0]["statistics"]["subscriberCount"])
   
    lis=[ int(x) for x in lis] #converting sub count to int type
    

    a=lis[0]-lis[1]
    
    if(a>0):
        comment.reply("Pewdiepie is leading with " + "{:,}".format(a) + " nine year olds " +
                      " \nPewdiepie :  " + "{:,}".format(lis[0])+"  \nT-Series :  " + "{:,}".format(lis[1]))
        
        print("posted")#for my console for me to keep a count
    else:
        comment.reply("Pewdiepie has lost the battle as T-Series is " +
                      "{:,}".format(a)+" subs ahead")
        print("posted") #for my console for me to keep a count
    
searchkey = re.compile(r'!PewdStatus|!PewdBot|/u/PewdStatus|!pewdstatus|!pewdbot|!Pewdbot|!Pewdstatus')#my stuff
debugkey = re.compile(r'!pewdbotgetcommanddata')
reddit=praw.Reddit(client_id="2T256yp2KjjJOQ", #Reddit Api
                   client_secret="z3FUDDpgi6n4ZLPdm4Ze2kdnC5Q", #Reddit Api
                   user_agent="PewdStatus bot (by /u/ashfaq_haq)",
                   username="PewdStatus",
                   password="pewdiepiebot")
subreddit = reddit.subreddit('pythonforengineers')
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

