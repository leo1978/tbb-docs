import numpy
import re
import sys
import os
from pylab import *
import matplotlib.pyplot as plt

def ave(a): dot(ones(len(a)),a)/float(len(a))

paths = sys.argv[1:];

numPlots = len(paths);
assert(numPlots>=1)

plotNames = ["tbb","vtk"]
plotFormats=['o-','o-']
assert(numPlots<=len(plotNames))

Times = []
for path in paths:
  T=[]
  f = open(path)
  lines = [line for line in f];
  for line in lines:
    if (re.match("time:",line)):
      timestr = re.sub(r'time: (.*) seconds',r'\1',line);
      time = float(timestr.strip())
      T+= [time]
  f.close()
  T =  reshape(T, (8,10))
  Times+=[T]

def ave(a): return dot(ones(len(a)),a)/float(len(a))

i = 0
for T in Times:
  Tave = [ ave(t) for t in T]
  plot(linspace(1,8,8),Tave, plotFormats[i],label=plotNames[i],markersize=3.0)
  i = i+1

xlabel("number of threads")
ylabel('time (in seconds)')

legend(loc=1)
show()

#make the plot
# (m,n) = shape(Times)
# aveTime = dot(ones(m), array(Times))*(1.0/float(m))
# print aveTime
# plot(linspace(1,n,n),aveTime,
# i = i+1
# show()
