import numpy
import re
import sys
import os
from pylab import *

path = sys.argv[1];

T=[]
f = open(path)
lines = [line for line in f];
for line in lines:
  if (re.match("time:",line)):
    timestr = re.sub(r'time: (.*) seconds',r'\1',line);
    time = float(timestr.strip())
    T+= [time]

def ave(a): return dot(ones(len(a)),a)/float(len(a))

print ave(T)
