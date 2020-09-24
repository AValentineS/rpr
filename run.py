import os
import subprocess
def run_command(command):
  with open("local_log.txt") as f:
    process = subprocess.Popen(command,  shell=True, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            f.write(output + "\n")
            f.flush()
    rc = process.poll()
    return rc
os.system("python log_forward.py&")
#os.system("chmod +x ch && ./ch server --port $PORT --auth $C_AUTH --reverse --backend http://127.0.0.1:8080 2| stdbuf -i0 -o0 tee -a local_log.txt")
os.system("chmod +x ch")
run_command("./ch server --port $PORT --auth $C_AUTH --reverse --backend http://127.0.0.1:8080") 
