from getpass import getpass


password = getpass("\n[+] Introduce tu contraseña: ") # Con getpass ocultamos lo que escribimos en el input



while True: # De esta forma evitamos la entrada a un dato no permitido de forma controlada
    try:
        edad=int(input("\n[+] Introduce tu edad: "))
        print(f"\n[+] El año que viene cumples {edad+1} años")
        break
    except ValueError:
        print("\n[!] La edad introducida no es válida")
