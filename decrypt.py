import time
import os
import os,sys
from stat import *
import sys
from sys import argv
import datetime
from os.path import exists

def decry() :
 while True :

    print "Enter the file you want to decrypt : "
    inpe = raw_input()
    try :
     fil= open(inpe)
     break
    except Exception :
     print "File Not found!"
     continue 
     
 last1=fil.read(1)
 last2=fil.read(1)
 las=last1+last2
 last=(int)(las)

 outadd=os.getcwd()+"/decrypted.txt"
 out=open(outadd,"w")

 while True :
         c=fil.read(1)
         if not c :
          break
         now1=fil.read(1)
        
         now=ord(now1)
         if ord(c)+last-now>255 :
            out.write(chr(ord(c)+last-now-256))
         elif ord(c)+last-now<0 :
            out.write(chr(ord(c)+last-now+256))
         else :
            out.write(chr(ord(c)+last-now))  
         continue
       
 print "Your decrypted file is stored at "
 print outadd

       
       
   


