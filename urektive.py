import subprocess
import os

print("""
\033[38;5;27m
██╗   ██╗██████╗ ███████╗██╗  ██╗████████╗██╗██╗   ██╗███████╗
██║   ██║██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██║██║   ██║██╔════╝
██║   ██║██████╔╝█████╗  █████╔╝    ██║   ██║██║   ██║█████╗  
██║   ██║██╔══██╗██╔══╝  ██╔═██╗    ██║   ██║╚██╗ ██╔╝██╔══╝  
╚██████╔╝██║  ██║███████╗██║  ██╗   ██║   ██║ ╚████╔╝ ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝
\033[0m
""")

print("\033[38;5;21mFlame44 & GPT 3.5 the goat\033[0m")

def play_alert_sound():
    if os.name == 'posix':  # Pour les systèmes de type Unix (comme Linux)
        os.system('aplay /home/kali/Downloads/LenaOrsa_ALittleChristmasMusic.mp3')  # Remplacez "alert.wav" par le chemin de votre fichier audio
    elif os.name == 'nt':  # Pour les systèmes Windows
        os.system('powershell -c (New-Object Media.SoundPlayer "/home/kali/Downloads/LenaOrsa_ALittleChristmasMusic.mp3").PlaySync()')  # Remplacez "alert.wav" par le chemin de votre fichier audio

def ping_and_alert(address):
    command = ['ping', '-c', '1', address]
    while True:
        result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result == 0:
            # Émettre un bruit d'alerte
            play_alert_sound()

# Demander à l'utilisateur d'entrer l'adresse cible
address_to_ping = input("Entrez l'adresse à cibler : ")
ping_and_alert(address_to_ping)
