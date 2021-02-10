import os
import subprocess
import requests
import sys
import base64
import select

def log_exec(args, env = None, log = None):
  '''
  execute command and log process stdout and stderr
  to file-object 'log' while simultaneously logging to stdout
  '''
  exec_env = {}
  exec_env.update(os.environ)

  # copy the OS environment into our local environment
  if env is not None:
    exec_env.update(env)

  # create a pipe to receive stdout and stderr from process
  (pipe_r, pipe_w) = os.pipe()

  p = subprocess.Popen(args,
                       shell = True,
                       env = exec_env,
                       stdout = pipe_w,
                       stderr = pipe_w)

  # Loop while the process is executing
  while p.poll() is None:
    # Loop long as the selct mechanism indicates there
    # is data to be read from the buffer
    while len(select.select([pipe_r], [], [], 0)[0]) == 1:
      # Read up to a 1 KB chunk of data
      buf = os.read(pipe_r, 1024)
      # Stream data to our stdout's fd of 0
      os.write(0, buf)
      if log is not None:
        log.write(buf)

  # cleanup
  os.close(pipe_r)
  os.close(pipe_w)

  # return the result of the process
  return p.returncode

#os.system("python log_forward.py&")
os.system("chmod +x ch && ./ch server --port $PORT --auth $C_AUTH --key $C_KEY --reverse --backend http://127.0.0.1:8080")
# 2| stdbuf -i0 -o0 tee -a local_log.txt
#os.system("chmod +x ch")
#run_command("./ch server --port $PORT --auth $C_AUTH --reverse --backend http://127.0.0.1:8080") 
