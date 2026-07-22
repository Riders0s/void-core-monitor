import os
import time
import shutil
import psutil  # La nuova libreria per CPU, RAM e Batteria

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_system():
    # 1. Calcolo Spazio Disco
    total, used, free = shutil.disk_usage("/")
    disk_used_pct = (used / total) * 100
    
    # 2. Calcolo Utilizzo CPU (controlla il carico nell'ultimo secondo)
    cpu_usage = psutil.cpu_percent(interval=None)
    
    # 3. Calcolo Memoria RAM
    ram = psutil.virtual_memory()
    ram_used_pct = ram.percent
    
    # 4. Controllo Stato Batteria
    battery = psutil.sensors_battery()
    if battery:
        bat_pct = battery.percent
        power_plugged = "In Carica" if battery.power_plugged else "Scarica"
    else:
        bat_pct = 100
        power_plugged = "N/D (Fisso)"

    clear_screen()
    print("=== VOID CORE SYSTEM MONITOR v2.0 ===")
    print("Status: OPERATIONAL")
    print("-" * 38)
    
    # Output CPU e RAM
    print(f"CPU Load:    [{cpu_usage:.1f}%]")
    print(f"RAM Usage:   [{ram_used_pct:.1f}%] ({ram.used // (2**20)} MB / {ram.total // (2**20)} MB)")
    print("-" * 38)
    
    # Output Disco e Batteria
    print(f"Storage:     [{disk_used_pct:.1f}%] Libero: {free // (2**30)} GB")
    print(f"Battery:     [{bat_pct}%] - {power_plugged}")
    print("-" * 38)
    
    # Logica di controllo anomalie avanzata
    if cpu_usage > 85 or ram_used_pct > 90:
        print("CRITICAL: Sovraccarico computazionale!")
    elif battery and bat_pct < 20 and not battery.power_plugged:
        print("WARNING: Alimentazione insufficiente. Collegare cavo.")
    else:
        print("SYSTEM: Flusso dati stabile. Nessuna anomalia.")

# Avvia il monitoraggio continuo
try:
    while True:
        check_system()
        time.sleep(2)  # Aggiorna ogni 2 secondi per maggiore reattività
except KeyboardInterrupt:
    print("\nMonitoraggio interrotto dall'operatore. Standby.")
