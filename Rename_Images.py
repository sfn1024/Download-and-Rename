import os
os.chdir('D:\python\AI\Gesture Detection SSD\VOC2007\JPEGImages\images\hand_gesture_one')
i=1
for file in os.listdir():
    src=file
    dst=str(i)+".png"
    os.rename(src,dst)
    i+=1
