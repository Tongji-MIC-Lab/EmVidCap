
import json
import string
import re
#import urllib32
#import base64
import os

f_sent=open('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/sent_train_new.txt')
#rc=json.load(f_json)
lines=f_sent.readlines()

f_txt=file('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/voc.txt','w+')

#anno=rc['annotations']
#remove="."
voc={}
k=0
voc[0]="UNK"
for line in lines:
    #caption=anno[i]['caption']
    caption=line.replace(".","")
    caption=caption.replace(",","")
    caption=caption.replace("!","")
    caption=caption.replace(";","")
    caption=caption.replace("\"","")
    caption=caption.replace("$","")
    caption=caption.replace("#","")
    caption=caption.replace("'","")
    caption=caption.replace("&","")
    caption=caption.replace("(","")
    caption=caption.replace(")","")
    caption=caption.replace("?","")
    caption=caption.replace("@","")
    caption=caption.replace(">","")
    caption=caption.replace("/","")
    caption=caption.replace("\\","")
    caption=caption.replace("`","")
    caption=caption.replace("=","")
    caption=caption.replace("[","")
    caption=caption.replace("]","")
    caption=caption.replace("-","")
    caption=caption.replace(":","")
    caption=caption.replace("\r","")
    for r in range(10):
        caption=caption.replace(str(r),"")

    words=caption.split(" ")
    for j in range(len(words)-1):
        word=words[j+1]
        word=word.lower()
        if word==" " or word=="\n":
           continue
        print len(voc)
        #print voc[k]
        while k<=len(voc):
              if word==voc[k]:
                 break
              k+=1
	      if k>=len(voc):
		 break
        if k>=len(voc): 
              #new_line=[word,'\n']
              f_txt.writelines(word+"\n")
              #f_txt.write('\n')
              voc[len(voc)]=word
        k=0

