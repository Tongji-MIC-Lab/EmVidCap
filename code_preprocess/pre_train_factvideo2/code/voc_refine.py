
voc_old=open('/data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/vocabulary_new.txt')

voc_new=file('/data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/vocabulary_refine.txt','a+')

lines=voc_old.readlines()

lines=sorted(set(lines),key=lines.index)

for line in lines:
   
   voc_new.write(line)



