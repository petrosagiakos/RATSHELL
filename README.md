# RATSHELL

## Description
Ratshell is a lightweight, Python-based remote access shell (RAT) designed for educational and ethical testing purposes. It provides remote command execution capabilities with a simple client-server model.

## Disclaimer
This tool is intended only for legal and ethical use. Always obtain proper authorization before using it in any environment. The developer is not responsible for misuse.

## Prerequisites
- Python 3 installed on your system
- Windows or Linux machine

## Example of Use
### 1. Clone this repository
```git clone https://github.com/petrosagiakos/RATSHELL``` 

### 2. Start the Rat server

Windows:
```python RatServer.py```

Linux:
```python3 RatServer.py``` 
### 3. Start the Rat server
On an other computer or in an other terminal run:

Windows:
```python RatClient.py```

Linux:
```python3 RatClient.py```

remember to change the ip in the client IP variable to the ip of the attacker (the machine the server is running on)

### 4. Connect to Client

In the Rat server type ```LC``` to list available clients.
then type ```CLIENT [n]``` where n is the id of the client.
Now you have a shell connection with your client. Type ```help``` to list available commands in client side. 


