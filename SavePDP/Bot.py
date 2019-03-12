#for Reddit
#pip install request,requests,json,praw
import praw
import json
import urllib.request
import re
print("start")
message="we have added a new command ! like (use it without the spaces) which displays the difference between the likes of PewDiePie's Youtube Rewind video and Despacito .\n\n"
def Pew():
	
	id=["kJQP7kiw5Fk","By_Cn5ixYLg&t"]
	key="AIzaSyD_wHoIHLe6yyYAbAZL4l6YDy_4iZd1vk8"
	up=list()
	down=list()
	for id in id:
		da=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+id+"&key="+key).read()
		su=down.append(json.loads(da)["items"][0]["statistics"]["dislikeCount"])
		ad=up.append(json.loads(da)["items"][0]["statistics"]["likeCount"])

	down=[ int(x) for x in down]
	up=[int(x) for x in up]
	l1=up[0]-up[1]
	l2=down[0]-down[1]
	if(l1>0):
		comment.reply("Pewdiepies Youtube rewind needs more  " +"{:,}".format(l1) + " likes to defeat Despacito."+
                      "\n\n Despacito has  "+ "{:,} ".format(up[0])+" Likes."+
    "\n\n\nPewdiepie's Rewind has  " +"{:,} ".format(up[1])+" likes."+
                      " \n\nI am a bot.\nFor further information please use '! help' (without the space) to see the commands.PM me for any feedback. ")
	else:
		comment.reply("Pewdiepie's Rewind video has the most likes")

       

def Rate():
    id=["YbJOTdZBX1g","kffacxfA7G4"]
    #cha2=[p,t,sp]
    key="AIzaSyD_wHoIHLe6yyYAbAZL4l6YDy_4iZd1vk8"
    ls=list()
    Like=list()
    i=-1
    for id in id:
        #data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+cha+"&key="+key).read()
        #subs=lis.append(json.loads(data)["items"][0]["statistics"]["subscriberCount"])
        dat=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+id+"&key="+key).read()
        sub=ls.append(json.loads(dat)["items"][0]["statistics"]["dislikeCount"])
        adds=Like.append(json.loads(dat)["items"][0]["statistics"]["likeCount"])

    ls=[ int(x) for x in ls]
    Like=[int(x) for x in Like]                     

    #print("Youtube Rewind:" Likes: "+"{:,}".format(Like[0])+ "|Dislikes: "+"{:,}".format(ls[0]))
    #print("Baby Likes: "+"{:,}".format(Like[1])+"|Dislikes:  "+"{:,} ".format(ls[1]))
    a1=ls[1]-ls[0]
    a2=ls[0]-ls[1]
    if(a1>0):
        comment.reply(message + "The Youtube Rewind 2018 video still needs " +"{:,}".format(a1) + " to be the most disliked video."+
                      "\n\nThe rewind video has "+ "{:,} ".format(ls[0])+"dislikes."+
    "\n\n\nBaby has " +"{:,} ".format(ls[1])+"dislikes."+
                      " \n\nI am a bot.\nFor further information please use '! help' (without the space) to see the commands.PM me for any feedback. ")
        #print("Pewds is "+ str(a2) +"behind YT sports" )
    else:
        comment.reply("The youtube rewind is the most disliked video of all time.    " + " Youtube Rewind has " + " {:,}".format(ls[0]) + " dislikes")
    
    #("The rewind video has "+ "{:,} ".format(ls[0])+"dislikes."+)
    #"Baby has " +"{:,} ".format(ls[1])+"dislikes.")
#print("Yt sports " +"{:,}".format(lis[2]))
def check():
    cha=["UC-lHJZR3Gqxm24_Vd_AJ5Yw","UCq-Fj5jknLsUf-MWSy4_brA","UC-9-kyTW8ZkZNDHQJ6FgpwQ"]
    #cha=["UC-lHJZR3Gqxm24_Vd_AJ5Yw","UCq-Fj5jknLsUf-MWSy4_brA","UCEgdi0XIXXZ-qJOFPf4JSKw","UCOpNcN46UbXVtpKMrmU4Abg"]	
    #Namecha=['pewdiepie','tseries','ytsports','ytgaming'] #name of youtube channels
    key="AIzaSyD_wHoIHLe6yyYAbAZL4l6YDy_4iZd1vk8" #Youtube Api
    lis=list()
    
    for cha in cha:
        data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+cha+"&key="+key).read()
        subs=lis.append(json.loads(data)["items"][0]["statistics"]["subscriberCount"])
   
    lis=[ int(x) for x in lis] #converting sub count to int type
    

    a1=lis[0]-lis[1]#differnce between pewds and T series
    a2=lis[2]-lis[0]# differnce between Yt sports and pewds
    a3=lis[2]-lis[0]
    if(a1>0):
        if(a3>0):
             comment.reply("Pewdiepie is ahead of T-Series by " + "{:,}".format(a1) + " subs and requires only  "+"{:,}".format(a3)+" more subs to beat Youtube Music!"+
                      "    \n\nYoutube Music:"+" \t\t" + "{:,}".format(lis[2])+' \t '+"    \n\nPewdiepie :\t\t" + "{:,}".format(lis[0])+'\t'
                           +"    \n\nT-Series :\t\t" + "{:,}".format(lis[1])+'\t'+
                           "\n\n Use ! rewind to know the dislikes of rewind   \n\nI am a bot.\nFor further information please use '! help' (without the space).    PM me for any feedback. ")
        else:
            comment.reply("Pewdiepie has defeated Youtube Sports and needs more " + "{:,}".format(a3) + " to defeat Youtube Gaming "+" \n\nPewdiepie :  " + "{:,}".format(lis[0])
                          +"  \n\nYoutube Gaming:  " + "{:,}".format(lis[2])+" \n\nT-Series :  " + "{:,}".format(lis[1])+
                          "\n\n\n Use \'! help' (without the space) to see more commands .PM me for feedback. ")
        
            
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
        comment.reply("We can defeat them.Be strong .It doesn't matter how many times we fail ,what matters is how many times we rise\n\n  T-series"+ "{:,}".format(a1)+" subs ahead")
        print("posted") #for my console for me to keep a count
    
searchkey = re.compile(r'!pvt|!pewd|!PewdStatus|!PewdBot|/u/PewdStatus|!pewdstatus|!pewdbot|!Pewdbot|!Pewdstatus')#my stuff
Rewind=re.compile(r'!Rewind |!rewind')
Help=re.compile(r'!help|!Help')
Pewd=re.compile(r'!like|!Like|!likes|!Likes')
debugkey = re.compile(r'!pewdbotgetcommanddata')
reddit=praw.Reddit(client_id="2T256yp2KjjJOQ", #Reddit Api
                   client_secret="z3FUDDpgi6n4ZLPdm4Ze2kdnC5Q", #Reddit Api
                   user_agent="PewdStatus bot (by /u/ashfaq_haq)",
                   username="PewdStatus",
                   password="pewdiepiebot")
subreddit = reddit.subreddit('PewdiepieSubmissions')  #("pythonforengineers") 
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
        
        comment.reply("! pewdbot->to get the subs of Pewdiepie and T-series   \n\n ! rewind->To get the dislikes of Youtube Rewind  \n\n ! like-> To Get the Pewdiepie's  rewind vs Despacito Likes" )
        file = open("file.txt",'a+')
        file.writelines(str(comment)+"\n")
        CommentList.insert(0,comment)
        #print(Keyused)
        file.close()
        print("help command")
    if Rewind.search(comment.body) and comment not in CommentList:
        file = open("file.txt",'a+')
        file.writelines(str(comment)+"\n")
        Rate()
        file.close()
        print("Dislike used")
    if Pewd.search(comment.body) and comment not in CommentList:
    	file=open("file.txt",'a+')
    	file.writelines(str(comment)+"\n")
    	Pew()
    	file.close()
    	print('Pewd REwind used')
