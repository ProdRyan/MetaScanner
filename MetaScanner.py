################################################################
#                                                              #
#                        [Creditos ]                           #
#                                                              #
################################################################
#                                                              #
#                 Codigo hecho por xNetting                    #
#                                                              #
#                Dev: xNetting / Grupo: Craka Squad            #
#                                                              #
################################################################

# CodedByxNetting
# CrakaSquad

import socket 
import os
import sys
import re

os.system('color a')
print('''

    ███    ███ ███████ ████████  █████      ███████  ██████  █████  ███    ██ 
    ████  ████ ██         ██    ██   ██     ██      ██      ██   ██ ████   ██ 
    ██ ████ ██ █████      ██    ███████     ███████ ██      ███████ ██ ██  ██ 
    ██  ██  ██ ██         ██    ██   ██          ██ ██      ██   ██ ██  ██ ██ 
    ██      ██ ███████    ██    ██   ██     ███████  ██████ ██   ██ ██   ████ 
    
                   Dev: xNetting / Grupo: Craka Squad
                                                                                                                                                
    ''')

def portscan():
    open_ports = []
    port_min = 0
    port_max = 65535
    patrones_puertos = re.compile("([0-9]+)-([0-9]+)")

    while True:
        print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │           Ponga la IP que desea escanear            │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    
        ''')

        target_1 = str(input('''
    
    root@xnetting: ~# '''))
        break

    while True:
        print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │      Ponga el rango de Puertos para escanear        │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    
        ''')

        port_1 = str(input('''
    
    root@xnetting: ~# '''))

        port_validacion = patrones_puertos.search(port_1.replace(" ",""))
        if port_validacion:
            port_min = int(port_validacion.group(1))
            port_max = int(port_validacion.group(2))
        break

    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
                scan.settimeout(0.5)
                scan.connect((target_1, port))
                open_ports.append(port)
        except:
            pass
    for port in open_ports:
        print(f'''
        
    El puerto {port} esta abierto en {target_1}''')

def verificar(port):
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │       Ponga la IP que desea ver su Conexion         │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')
    target = str(input('''
    
    root@xnetting: ~# '''))
    try:
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks.connect((target, port))
        return True
    except:
        return False

def menu():
    print('''
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga el Scan que quiere hacer                    │                      
    │                                                     │
    │        1 - Verificar Conexion                       │
    │                                                     │
    │        2 - Port Scanner                             │                     
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    ''')

    opcion = input('''
    
    root@xnetting: ~# ''')

    if opcion == '1':
        print(verificar(80))
    if opcion == '2':
        portscan()
    else:
        sys.exit()

menu()
