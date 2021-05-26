import win32api
import pyttsx3 as r
engine = r.init()
engine.setProperty('rate',130)
import random
import psutil
from time import sleep
import reg_ever
import reg_main
import os
from difflib import SequenceMatcher

#to know the default drives
'''p_drives = win32api.GetLogicalDriveStrings()
p_drives = p_drives.split('\000')[:-1]
print(p_drives)'''

p_drives =['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\','H:\\']
res=["hai sir","hello sir","sir"]
max_len_drive=len(p_drives)
c_=0

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def speak(text):
    engine.say(text)
    engine.runAndWait()
            
while True:
    try:
        l,dic,z=[],{},""
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        if len(drives)<max_len_drive:
            c_-=1
            speak("device removed")
            max_len_drive=len(drives)
        if len(drives)>6 and len(drives)>max_len_drive:
            c_+=1
            max_len_drive=len(drives)
            sleep(1)
            speak(random.choice(res)+" . there is a new device connected in your system . collecting information about the new device")
            sleep(3)
            for i in drives:
                if i not in p_drives:
                    c=win32api.GetVolumeInformation(i) #getting information about the new device
                    #print(c) #uncomment to see what info is gathered about the new device
                    dic['name']=c[0]
                    d=psutil.disk_usage(i)
                    dic['total']=str(round(d.total/(2**30),1))
                    dic['total_used']=str(round(d.used/(2**30),1))
                    dic['total_free']=str(round(d.free/(2**30),1))
                    dic['per']=int(d.percent)
                    l.append(dic)
                    dic={}
            '''print(l)
            print(c_)
            print()'''
            i=l[c_-1]
            sleep(1.5)
            z+="information collected . device name . "+i['name']+" . total storage space of the device . "+i['total']+" GB . total space used . "+i['total_used']+" GB . free space available . "+i['total_free']+" GB . "
            if 100-i['per']<=20:
                z+="this device has only "+str(100-i['per'])+" percent of free space"
            else:
                z+="this device has "+str(100-i['per'])+" percent of free space"
            speak(z)
            speak("would you like to open the new device")
            if reg_main.reg(max_len_drive):
                speak("opening")
                os.startfile(drives[len(drives)-1])
                m=drives[len(drives)-1]
                print(m)
                m=m[:len(m)-1]
                print(m)
                while True:
                    drives = win32api.GetLogicalDriveStrings()
                    drives = drives.split('\000')[:-1]
                    if len(drives)<max_len_drive:
                        c_-=1
                        speak("device removed")
                        max_len_drive=len(drives)
                        break
                    else:
                        c="\m"
                        max_=-0.1
                        try:
                            lis=os.listdir(m)
                        except:
                            pass
                        text=reg_ever.reg_1(max_len_drive)
                        if "open" in text.lower():
                            try:
                                print(text)
                                text=text.lower().replace("open","")
                                print(text)
                                for i in lis:
                                    if similar(text,i.lower())>=max_:
                                        max_=similar(text,i.lower())
                                        fol=i
                                m+=c[0]+fol
                                print(m)
                                os.startfile(m)
                            except:
                                pass
                        elif "go back" in text.lower():
                            try:
                                m=m.rsplit(c[0],1)[0]
                                print(m)
                                os.startfile(m)
                            except:
                                continue
                        elif text=="device removed":
                            break
    except:
        speak("the new device is not connected properly , please recconnect the device")
