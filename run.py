import os
import subprocess
import requests
import sys
import base64
def run_command(command):
  with open("local_log.txt", "w") as f:
    process = subprocess.Popen(command,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        se = process.stderr.readline()
        if se:
          output+=se
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip(), file=sys.stderr)
            f.write(output + "\n")
            #sys.stderr.write(
            r = requests.get('http://127.0.0.1:8080/tfpw.php?data=' + str(base64.b64encode(output.encode("utf-8"))))
            f.flush()
    rc = process.poll()
    return rc
os.system("python log_forward.py&")
#os.system("chmod +x ch && ./ch server --port $PORT --auth $C_AUTH --reverse --backend http://127.0.0.1:8080 2| stdbuf -i0 -o0 tee -a local_log.txt")
os.system("chmod +x ch")
run_command("./ch server --port $PORT --auth $C_AUTH --reverse --backend http://127.0.0.1:8080") 
