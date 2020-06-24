import os
import time

t1=time.time()
os.system('python /home/zyzhang/software/libsvm-3.22/tools/gridthunder.py -b 1 -v 5 ./m91temp/out_2438.svm.scale > test1.C-G')
print("gridthunder time:%f"%(time.time()-t1))

t2=time.time()
os.system('python /home/zyzhang/software/libsvm-3.22/tools/grid.py -b 1 -v 5 ./m91temp/out_2438.svm.scale > test2.C-G')
print("grid time:%f"%(time.time()-t2))

