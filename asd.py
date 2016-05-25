import time
myfile = open ('diego.txt','w')
myfile.write('rarara')
myfile.write('rarara')
myfile.write('rarara')
print >>myfile,"hello"
myfile.write('rarara\n')
myfile.write('rarara\n')
myfile.write('rarara\n')
for i in range(0,10000,1):
    if i%100==0:
        myfile.write('\n')
        myfile.write(str(i))
    time.sleep(20)
myfile.close()
