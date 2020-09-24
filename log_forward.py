import requests
import base64
import sys
from tailf 
import time

time.sleep(20)

with tailf.Tail("/tmp/local_log.txt") as tail:
    print("started")
    while True:
        for event in tail:
            if isinstance(event, bytes):
                r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + base64.b64encode(event))
                print("updated")
            elif event is tailf.Truncated:
                print("File was truncated")
            else:
                assert False, "unreachable" # currently. more events may be introduced later
        time.sleep(0.01) # save CPU cycles
  
               
