
f_old=open('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/voc.txt')

f_new=file('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/voc_fine.txt','a+')

line_old=f_old.readlines()
#line=sorted(line_old)
line={}.fromkeys(line_old).keys()
line=sorted(line)
unknown="UNK"+'\n'
f_new.write(unknown)

#print len(line)
#while line:
#      if line!="" and line!=" ":
#         print line
#         f_new.write(line)
for l in line:
    if not l.isspace():
       print(l,'\n')
       f_new.write(l)





