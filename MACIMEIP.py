import requests
import os
from termcolor import colored

def ip_geolocation(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Informazioni di geolocalizzazione:")
        print(f"Paese: {data['country_name']}")
        print(f"Città: {data['city']}")
        print(f"Latitudine: {data['latitude']}")
        print(f"Longitudine: {data['longitude']}")
        print(f"Organizzazione: {data['org']}")
    else:
        print("Impossibile ottenere informazioni di geolocalizzazione.")

def mac_lookup(mac):
    url = f"https://api.macvendors.com/{mac}"
    response = requests.get(url)

    if response.status_code == 200:
        vendor = response.text.strip()
        print("Informazioni MAC Address:")
        print(f"Fornitore: {vendor}")
    else:
        print("Impossibile ottenere informazioni MAC Address.")

# Funzione per ottenere le informazioni sul proprio indirizzo IP e MAC Address
def get_my_info():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            my_ip = data["ip"]
            os.system('cls' if os.name == 'nt' else 'clear')  # Pulisci lo schermo
            print(logo)
            print("Questo è il tuo indirizzo IP e le relative informazioni:")
            print(f"Il tuo indirizzo IP: {my_ip}")
            ip_geolocation(my_ip)
        else:
            print("Impossibile ottenere il tuo indirizzo IP.")
    except:
        print("Si è verificato un errore durante la connessione all'API.")

# Logo MACIMEIP in ASCII Art (colore: azzurro)
logo = colored('''
888b     d888          d8888    .d8888b.    8888888   888b     d888   8888888888   8888888   8888888b.  
8888b   d8888         d88888   d88P  Y88b     888     8888b   d8888   888            888     888   Y88b 
88888b.d88888        d88P888   888    888     888     88888b.d88888   888            888     888    888 
888Y88888P888       d88P 888   888            888     888Y88888P888   8888888        888     888   d88P 
888 Y888P 888      d88P  888   888            888     888 Y888P 888   888            888     8888888P"  
888  Y8P  888     d88P   888   888    888     888     888  Y8P  888   888            888     888        
888   "   888    d8888888888   Y88b  d88P     888     888   "   888   888            888     888        
888       888   d88P     888    "Y8888P"    8888888   888       888   8888888888   8888888   888      
''', 'cyan')

# Messaggio di benvenuto con logo MACIMEIP
print(logo)
print("Benvenuto a MAC IMEI IP di UnammedGit!")
print("Questo tool ti consente di ottenere informazioni su un indirizzo IP, IMEI o MAC Address.")
print("Opzioni disponibili: 1. IP, 2. MAC, 3. IMEI, 4. Le Mie Informazioni, 5. Esci")

# Selezione opzione
while True:
    option = input("Seleziona l'opzione da controllare: ")

    if option == "1":
        ip_address = input("Inserisci l'indirizzo IP: ")
        print(f"Informazioni per l'indirizzo IP: {ip_address}")
        ip_geolocation(ip_address)
    elif option == "2":
        mac_address = input("Inserisci il MAC Address: ")
        print(f"Informazioni per il MAC Address: {mac_address}")
        mac_lookup(mac_address)
    elif option == "3":
        imei_number = input("Inserisci l'IMEI: ")
        print(f"Informazioni per l'IMEI: {imei_number}")
        imei_lookup(imei_number)
    elif option == "4":
        get_my_info()
        input("Premi Enter per tornare al menu principale.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Pulisci lo schermo
        print(logo)
        print("Benvenuto a MACIMEIP di UnammedGit!")
        print("Questo tool ti consente di ottenere informazioni su un indirizzo IP, IMEI o MAC Address.")
        print("Opzioni disponibili: 1. IP, 2. MAC, 3. IMEI, 4. Le Mie Informazioni, 5. Esci")
    elif option == "5":
        break
    else:
        print("Opzione non valida. Riprova.")