import win32api
import speech_recognition as sr
def reg(max_len_drive):
    i=0
    while True:
            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split('\000')[:-1]
            if len(drives)<max_len_drive:
                c_-=1
                return False
            else:
                try:
                    a=sr.Recognizer()
                    with sr.Microphone() as speech:
                        a.adjust_for_ambient_noise(speech)
                        spoke=a.listen(speech)
                        try:
                            text=a.recognize_google(spoke)
                            if text.lower()=="ok" or text.lower()=="yes":
                                return True
                            else:
                                if i<2:
                                    i+=1
                                    continue
                                else:
                                    return False
                        except:
                            if i<2:
                                i+=1
                                continue
                            else:
                                return False
                except:
                    if i<2:
                        i+=1
                        continue
                    else:
                        return False

