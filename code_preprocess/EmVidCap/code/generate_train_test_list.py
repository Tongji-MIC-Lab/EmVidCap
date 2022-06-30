import os
import sys
import re

f_txt=file('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits/test2.txt','a+')

vid_path='/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits/test/'

vid_list=os.listdir(vid_path)
vid_list=sorted(vid_list)
for vid in vid_list:
   #print(vid)
   img_path=vid_path+vid
   img_list=os.listdir(img_path)
   #img_list=sorted(img_list)
   #img_list=sorted(img_list,key=lambda i:int(re.match('\D+(\w)',i).group(1)))
   img_list.sort()
   for img in img_list:
      #print(img)
      absoute_path=img_path+'/'+img+' '+str(0)+'\n'
      f_txt.write(absoute_path)
  
