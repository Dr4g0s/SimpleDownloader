import os
from pySmartDL import SmartDL
import argparse
import time

parser = argparse.ArgumentParser(prog="python3 Download_Manager.py")
parser.add_argument('-u',dest='url',nargs='?',metavar='Your Link')
parser.add_argument("-d",dest='dir',nargs='?',metavar='your Directory',help='Default = current directory')
args = parser.parse_args()
if args.url==None :
   print("Usage: < python3 Download_Manager.py -h/--help >")
   exit(0)
else:
    url=str(args.url)
    if args.dir==None:
           dest=os.getcwd()
    else:
        dest=str(args.dir)

    obj = SmartDL(url,dest)
    print("\n"+"="*70+"\n")
    file_name= url.split("/")[-1]
    obj.start()
    path = obj.get_dest()
    if obj.isSuccessful():
          print("\n"+"="*70+"\n")
          print("File Name: '%s'" % file_name)
          print("downloaded file to '%s'" % obj.get_dest())
          print("Speed: %s" % obj.get_speed(human=True))
          print("Already downloaded: %s" % obj.get_dl_size(human=True))
          print("Eta: %s" % obj.get_eta(human=True))
          print("Progress: %d%%" % (obj.get_progress()*100))
          print("Progress bar: %s" % obj.get_progress_bar())
          print("Status: %s" % obj.get_status())
          print("\n"*2+"="*70+"\n")
          time.sleep(0.025)
    else:
          print("There were some errors:")
          for e in obj.get_errors():
              print(str(e))

