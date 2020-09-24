import requests
import base64
import sys
import tailf 
import time

time.sleep(20)

with tailf.Tail("local_log.txt") as tail:
    print("started")
    while True:
        for event in tail:
            if isinstance(event, bytes):
                print("updating")
                r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + str(base64.b64encode(event)))
                print("updated")
            elif event is tailf.Truncated:
                print("File was truncated")
        time.sleep(0.01) # save CPU cycles
  
            
