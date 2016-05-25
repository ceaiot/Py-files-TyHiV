import datetime   
import time
import random
from matplotlib import pyplot
from numpy import arange
import matplotlib.dates as md
d1=0
st0=0
ts = time.time()
st1 = datetime.datetime.fromtimestamp(ts).strftime('%H%M%S')
to=float(st1)*0.01
ts = time.time()
st1 = datetime.datetime.now()
pyplot.close()
d1=random.random()
for n in  range(0,50,1):
    pyplot.figure(n%2+1)
    d0=d1
    d1=random.random()
    st0=st1
    ts = time.time()
    st1 = datetime.datetime.now()
    print ('('+str(st0)+','+str(d0)+')\n')
    pyplot.plot([st0,st1],[d0,d1],'b')
    #pyplot.ylim(2120,2130)
    pyplot.xticks( rotation=25 )
    ax=pyplot.gca()
    xfmt = md.DateFormatter('%H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    pyplot.ion()
    pyplot.show()
    pyplot.pause(1) 
       
    
    
pyplot.close("all")
    
