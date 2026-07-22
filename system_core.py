import os
import time
import shutil

def clear_screen():
    # Pulisce lo schermo del terminale per un effetto console pulito
    os.system('cls' if os.name == 'nt' else 'clear')

def check_system():
    # Recupera i dati reali del tuo hard disk (Spazio totale, usato, libero)
    total, used, free = shutil.disk_usage("/")
    
    # Calcola la percentuale di utilizzo
    used_percentage = (used / total) * 100
    
    clear_screen()
    print("=== VOID CORE SYSTEM MONITOR ===")
    print(f"Status: OPERATIONAL")
    print("-" * 32)
    print(f"Spazio Totale Disco: {total // (2**30)} GB")
    print(f"Spazio Utilizzato:   {used // (2**30)} GB ({used_percentage:.2f}%)")
    print(f"Spazio Libero:       {free // (2**30)} GB")
    print("-" * 32)
    
    # Logica di controllo del sistema
    if used_percentage > 90:
        print("CRITICAL: Sovraccarico memoria. Avviare pulizia moduli.")
    else:
        print("SYSTEM: Flusso dati stabile. Nessuna anomalia rilevata.")

# Avvia il monitoraggio continuo ogni 5 secondi
try:
    while True:
        check_system()
        time.sleep(5)
except KeyboardInterrupt:
    print("\nMonitoraggio interrotto dall'operatore. Standby.")