import numpy
import re
import sys
import os
from pylab import *
import matplotlib.pyplot as plt

path = sys.argv[1];

T=[]
f = open(path)
lines = [line for line in f];
for line in lines:
  if (re.match("time:",line)):
    timestr = re.sub(r'time: (.*) seconds',r'\1',line);
    time = float(timestr.strip())
    T+= [time]
f.close()

T =  reshape(T, (len(T)/10,10))

def ave(a): return dot(ones(len(a)),a)/float(len(a))

i = 0
Tave = [ ave(t) for t in T]
plot(range(1,9),Tave,"o-",label='total running time')

xlabel("number of threads")
ylabel('time (in seconds)')
ylim(ymin = 0)
legend()
show()
