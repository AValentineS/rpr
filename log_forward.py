import requests
import base64
import sys
from tailf import tailf    
import time

time.sleep(20)
for line in tailf("/tmp/local_log.txt"):
  r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + base64.b64encode(line.encode("utf-8")))
               
