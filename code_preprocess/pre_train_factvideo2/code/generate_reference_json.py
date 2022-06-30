
import json
import os

f_txt=open('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/sent_val_new.txt')
f_json=open('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/sent_val_new.json','w')

out={}
anno={}
img={}
annotations=[]
images=[]
image_id=[]

k=0

lines=f_txt.readlines()

for i in range(135):
    vid='vid'+str(1300+i)
    for line in lines:
        if vid in line:
           print(vid)
           k=k+1
           line=line.replace('\r','')
           line=line.replace('\n','')
           words=line.split('	')
           #words=words.rstrip('\r'+'\n')
           caption=' '
           caption=caption.join(words[1:len(words)])
           anno['caption']=caption
           if len(str(i))==1:
              image_id='20180909000000000'+str(i)
           elif len(str(i))==2:
              image_id='2018090900000000'+str(i)
           else:
              image_id='201809090000000'+str(i)
           anno['image_id']=image_id
           anno['id']=str(k)
           
           annotations.append(anno)

           img['date_captured']=''
           img['file_name']=vid
           img['height']=0
           img['width']=0
           img['id']=image_id
           img['license']=''
           img['url']=vid
     
           images.append(img)

           anno={}
           img={}
info={}
licenses={}

info['contributor']='Tongji_MIC'
info['date_created']=''
info['description']='CaptionEval'
info['url']='http://www.tongji.edu.cn'
info['version']='1'
info['year']='2018'

licenses['id']=1
licenses['name']='test'
licenses['url']='test'

out['annotations']=annotations
out['images']=images
out['info']=info
out['licenses']=licenses
out['type']='captions'

json.dump(out,f_json)

f_txt.close()
f_json.close()















