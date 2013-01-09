import numpy
import re
import sys
import os
from pylab import *
import matplotlib.pyplot as plt

logDirs = sys.argv[1:];

numPlots = len(logDirs);
assert(numPlots>=1)

plotNames = ["tbb","vtk"]
plotFormats=['o-','o--']
assert(numPlots<=len(plotNames))

i = 0
for logDir in logDirs:

  fnames = os.listdir(logDir)

  Times = []

  for (path,dir,files) in os.walk(logDir):
    for fname in files:
      fullname = os.path.join(path,fname)
      times = []
      f = open(fullname,"r")
      for line in f:
        if (re.match("time:",line)):
          timestr = re.sub(r'time: (.*) seconds',r'\1',line);
          time = float(timestr.strip())
          times+= [time]

      if(len(times)!=0):
        Times+=[times]
      f.close()

    Times = array(Times);
    (m,n) = shape(Times)

    aveTime = dot(ones(m), array(Times))*(1.0/float(m))
    print aveTime
    plot(linspace(1,n,n),aveTime,plotFormats[i],label=plotNames[i],markersize=4.0)
  i = i+1

#make the plot
legend()
xlabel("number of threads")
ylabel('time (in seconds)')
ylim((0,15))
show()
