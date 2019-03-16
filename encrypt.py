import time
import os
import os,sys
from stat import *
import sys
from sys import argv
import datetime
from os.path import exists

def encry(dire) :
 lastdat= time.ctime(os.stat(dire).st_atime)   
 insec=lastdat[17]+lastdat[18]
 last=(int)(insec)

 outadd=os.getcwd()+"/encrypted.txt"
 
 out=open(outadd,"w")
 out.write(insec)
 while True :
  print "Enter the file that you want to encrypt : "
  inpe = raw_input()

  try :
    with open(inpe) as fil :
     while True :
      c=fil.read(1)
      if not c :
        break
      else :
       now=(str)(datetime.datetime.now().microsecond)
       nowt=now[len(now)-1]+now[len(now)-2]
       key=(int)(nowt) 
       if ord(c)-last+key>255 :
        out.write(chr(ord(c)-last+key-256))
       elif ord(c)-last+key<0 :
        out.write(chr(ord(c)-last+key+256))
       else :
        out.write(chr(ord(c)-last+key)) 
        out.write(chr(key)) 
    break    
  except Exception :
      print "File not found!"
      continue
 print "Your file is encrypted and is saved at "
 print outadd



    



