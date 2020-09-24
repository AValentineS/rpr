import os
os.system("python log_forward.py&")
os.system("chmod +x ch && ./ch server --port $PORT --auth $C_AUTH --reverse --backend http://127.0.0.1:8080 2| stdbuf -i0 -o0 tee -a local_log.txt")
