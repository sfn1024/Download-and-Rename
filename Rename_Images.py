import os
os.chdir('<folder path>')
i=1
for file in os.listdir():
    src=file
    dst="A" + str(i) + ".png"   #dst= "name" +"Extension"
    os.rename(src,dst)
    i+=1 #delete if you didn't use any number increment
