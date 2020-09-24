import requests
import base64
import sys
import tailf 
import time
import os
fn = "local_log.txt"
time.sleep(20)

r = requests.get('http://127.0.0.1:8080/ping.php')
oldsize=-1
while True:
    size = os.path.getsize(fn)
    r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + str(base64.b64encode(line)))
    if size!=oldsize:
        with open(fn, "r") as f:
            if size>oldsize:
                f.seek(oldsize)
            for line in f:
                r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + str(base64.b64encode(line)))
    oldsize = size
    time.sleep(2.5)
            
