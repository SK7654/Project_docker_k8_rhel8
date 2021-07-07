#!/usr/bin/python3
print("Content-type: text/html")
print()

import time
import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
status=cmd.getvalue("k")
st,out=sub.getstatusoutput("sudo "+status)
if st==0:
    print("Your Container Status Successfully launch :" +out)
else:
    print("Error Occurred \n " +out)
