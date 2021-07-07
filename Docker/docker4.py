#!/usr/bin/python3
print("Content-type: text/html")
print()

import time
import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
imgstat=cmd.getvalue("l")
st,out=sub.getstatusoutput("sudo "+imgstat)
if st==0:
    print("Your Image Status Successfully launch :" +out)
else:
    print("Error Occurred \n " +out)
