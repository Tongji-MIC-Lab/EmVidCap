import os
import sys
import re

f_old=open('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/sent_train.txt','r')

f_new=file('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/sent_train_new.txt','a+')

lines=f_old.readlines()

for i in range(241):
    vid='vid'+str(i)+'	'
    for line in lines:
        if vid in line:
           f_new.write(line)
  

  
