import time
import os
import os,sys
from stat import *
import sys
from sys import argv
import datetime
from os.path import exists
import encrypt
import decrypt


ch='Y'
try :
 key=open("key.txt")
except Exception  :
   print "Error opening Key file!"
   time.sleep(3)
   print "Terminating!"
   exit()
    
dire=key.readline()

while True :
 os.system('clear') 
 os.system("cls") 
 print "==========Welcome to ModEncrypto 1.0========== \n"
 print "What do you want to do : ?\n"
 print "\n\nYour current key directory is : "
 print dire
 print "\n\n"
 print "  1-Encrypt a file \n"
 print "  2-Decrypt a file \n"
 print "  3-Change the key directory \n"
 print "  4-Exit\n"
 print "\n\n Enter your choice : "
 choice = (int)(raw_input())
 
 if choice == 1 :
   encrypt.encry(dire)
   print "Do you want to continue : (Y/N) "
   ch= raw_input()
   if ch == 'y' or ch == 'Y' :
     continue
   else :
      exit()
 elif choice == 2 :
   decrypt.decry()
   print "Do you want to continue : (Y/N) "
   ch= raw_input()
   if ch == 'y' or ch == 'Y' :
     continue
   else :
      exit()
 elif choice == 3 :
   print "Enter your new key directory : "
   dire = raw_input()
   try :
    key= open("key.txt","w")
   except Exception :
      print "Error opening key file " 
   key.writelines(dire)

   


   print "Do you want to continue : (Y/N) "
   ch= raw_input()
   if ch == 'y' or ch == 'Y' :
     continue
   else :
      exit()
 elif choice == 4 :
    exit()
 else :
    continue
 
