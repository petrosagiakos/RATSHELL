# RATSHELL

## Description
Ratshell is a lightweight, Python-based remote access shell (RAT) designed for educational and ethical testing purposes. It provides remote command execution capabilities with a simple client-server model.

## Disclaimer
This tool is intended only for legal and ethical use. Always obtain proper authorization before using it in any environment. The developer is not responsible for misuse.

## Prerequisites
- Python 3 installed on your system
- Windows or Linux machine

## Example of Use
Clone this repository
```bash git clone https://github.com/petrosagiakos/RATSHELL``` 

Open a terminal and start the Rat server

Windows:
```bash python RatServer.py```

Linux:
```bash python3 RatServer.py``` 

On an other computer or in an other terminal run:

Windows:
```bash python RatClient.py```

Linux:
```bash python3 RatClient.py```

remember to change the ip in the client IP variable to the ip of the attacker (the machine the server is running on)

