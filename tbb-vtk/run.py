import sys
import numpy
import os

assert(len(sys.argv)==2)

inputcmd=sys.argv[1]

numRuns = 10;
maxThreads = 8
for numThreads in range(1,maxThreads+1,1):
  actualNumThreads = numThreads if numThreads>1 else 0
  for j in range(numRuns):
    cmd = inputcmd+" --numThreads "+ str(actualNumThreads)
    os.system("echo "+cmd)
    os.system(cmd)

