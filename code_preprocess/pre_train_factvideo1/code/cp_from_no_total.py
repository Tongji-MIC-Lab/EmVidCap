import os
import sys

begin = int(sys.argv[1])
end = int(sys.argv[2])
des_path = sys.argv[3]

for i in range(begin, end + 1):
    cmd = 'cp -r /data/tpj/tpj/S2VT/videocap-datasets/Youtube/splits_per10/test/vid%d %s' % (i, des_path)
    os.system(cmd)
