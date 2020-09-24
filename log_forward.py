import requests
import base64
import sys

for line in sys.stdin:
  r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + base64.b64encode(line.encode("utf-8")))
               
