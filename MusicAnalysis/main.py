import PyAudio_Record as rec
import BPM_Extraction as rbpm
import threading
import time
if __name__ =="__main__":
    while True:
        t1 = threading.Thread(target=rec.record,args=()) #Thread 1 to record sound every 10 seconds
        t2 = threading.Thread(target=rbpm.extractBPM,args=())#Thread 2 to detect features from the recorded file
# to save space we are rewriting the same file
        t1.start()
        t1.join()
        t2.start()
        t2.join() # once both of them are done wait for a sec
        """if (rbpm.bpm == None):
            print("Default Colour Scheme")
            break"""
        print("Hi!")
        time.sleep(1)
        #control signals

