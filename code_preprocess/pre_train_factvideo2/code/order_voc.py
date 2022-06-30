
voc_old=open('/data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/vocabulary.txt')

voc_new=file('/data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/vocabulary_new.txt','a+')

lines=voc_old.readlines()

lines=sorted(lines)

for line in lines:
   voc_new.write(line)



