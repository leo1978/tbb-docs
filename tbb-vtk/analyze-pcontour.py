import numpy
import re
import sys
import os
from pylab import *
import matplotlib.pyplot as plt

path = sys.argv[1];

T=[]
T1=[]
f = open(path)
lines = [line for line in f];
for line in lines:
  if (re.match("time:",line)):
    timestr = re.sub(r'time: (.*) seconds',r'\1',line);
    time = float(timestr.strip())
    T+= [time]

  if (re.match("Merge took ",line)):
    timestr = re.sub(r'Merge took (.*) seconds',r'\1',line);
    time = float(timestr.strip())
    T1+= [time]

f.close()

T =  reshape(T, (len(T)/10,10))
T1 =  reshape(T1, (len(T1)/10,10))

def ave(a): return dot(ones(len(a)),a)/float(len(a))

i = 0
Tave = [ ave(t) for t in T]
T1ave = [ ave(t) for t in T1]
print T1ave
plot(range(1,9),Tave,"o-",label='total running time')
plot(range(2,9),T1ave,"o-", label='merge time')

xlabel("number of threads")
ylabel('time (in seconds)')
ylim(ymin = 0)
legend()
show()
