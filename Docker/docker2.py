#!/usr/bin/python3
print("Content-type: text/html")
print()

import time
import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
pull=cmd.getvalue("j")
st,out=sub.getstatusoutput(" sudo docker pull " +pull)
if st==0:
    print("Your Image Successfully Pull :" +out)
else:
    print("Error Occurred \n " +out)
