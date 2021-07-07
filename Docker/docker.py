#!/usr/bin/python3
print("Content-type: text/html")
print()

import time
import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
img=cmd.getvalue("x")
cont=cmd.getvalue("y")
st,out=sub.getstatusoutput(" sudo docker run -dit --name=" +cont +" " +img)
if st==0:
    print("Your Container Successfully launch :" +out)
else:
    print("Error Occurred \n " +out)

