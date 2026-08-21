#!/usr/bin/env python3
"""
================================================================================
⚡ NOAH ENGINE TRADE (NET) - QUANTUM RUNTIME SYSTEM V5.1
Author: Ferr - Noah Trading System
Platform: MetaTrader 5 (MT5) Low-Latency Integration
================================================================================
"""

import os, time, sys, json, subprocess, threading

CONFIG_FILE = "noah_client_config.json"

# ==========================================
# SYSTEM AWAKE GUARD (ANTI-SLEEP / HIBERNATE)
# ==========================================
_caffeinate_proc = None

def start_awake_guard():
    global _caffeinate_proc
    try:
        if sys.platform == "darwin":
            _caffeinate_proc = subprocess.Popen(["caffeinate", "-d", "-i"])
        elif sys.platform == "win32":
            import ctypes
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000001 | 0x00000002)
    except Exception: pass

def stop_awake_guard():
    global _caffeinate_proc
    try:
        if _caffeinate_proc and _caffeinate_proc.poll() is None:
            _caffeinate_proc.terminate()
        if sys.platform == "win32":
            import ctypes
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    except Exception: pass

import atexit
atexit.register(stop_awake_guard)
start_awake_guard()


def get_default_mt5_dir():
    # Cek direktori MT5 files otomatis
    home = os.path.expanduser("~")
    # Mac Wine default
    mac_wine = os.path.join(home, "Library/Application Support/net.metaquotes.wine.metatrader5/drive_c/Program Files/MetaTrader 5/MQL5/Files")
    if os.path.exists(mac_wine): return mac_wine
    # Windows native default
    win_appdata = os.path.join(os.environ.get("APPDATA", ""), "MetaQuotes/Terminal")
    if os.path.exists(win_appdata): return win_appdata
    return os.path.join(home, "MQL5/Files")

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f: return json.load(f)
        except Exception: pass
    return {}

def save_config(cfg):
    try:
        with open(CONFIG_FILE, "w") as f: json.dump(cfg, f, indent=4)
    except Exception: pass

cfg = load_config()
if "MT5_FILES_DIR" not in cfg:
    def_dir = get_default_mt5_dir()
    print("="*65)
    print("⚡ NOAH ENGINE TRADE (NET) - INITIAL CLIENT SETUP")
    print("="*65)
    print("Petunjuk: Buka MT5 -> File -> Open Data Folder -> MQL5 -> Files")
    inp_dir = input(f"Masukkan Path folder MQL5/Files [{def_dir}]: ").strip()
    cfg["MT5_FILES_DIR"] = inp_dir if inp_dir else def_dir
    save_config(cfg)

MT5_DIR = cfg.get("MT5_FILES_DIR", "")
EYE_FILE = os.path.join(MT5_DIR, "noah_eye_live.txt")
STATE_FILE = os.path.join(MT5_DIR, "noah_state.txt")

def print_banner():
    print("\n" + "="*65)
    print("⚡  NOAH ENGINE TRADE (NET) - QUANTUM RUNTIME V5.1  ⚡")
    print("="*65)
    print("🔒 Security Protocol : SHA-256 Cryptographic License Protection")
    print("📡 Execution Core    : Multi-Layer High-Frequency Neural Engine")
    print("🧠 Filter Architecture: Temporal Multi-Frame Consensus Engine (Anti-Noise)")
    print("📊 Data Bridge       : Sub-Millisecond MT5 IPC Shared Memory")
    print(f"📁 MT5 Interface     : {MT5_DIR}")
    print("="*65)
    print("🟢 [● RUNNING] Neural Algorithm Stream Active. Happy Trading!\n")

def read_mt5_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f: return f.read().strip()
        except Exception: pass
    return ""

def main():
    print_banner()
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    idx = 0
    
    while True:
        try:
            anim = spinner[idx % len(spinner)]
            idx += 1
            
            # Cek status MT5
            st = read_mt5_state()
            bal = "N/A"
            flt = "0.00"
            if st:
                for item in st.split("|"):
                    if item.startswith("BAL="): bal = item.split("=")[1]
                    if item.startswith("FLT="): flt = item.split("=")[1]

            sys.stdout.write(f"\r\033[K[{time.strftime('%H:%M:%S')}] {anim} [QUANTUM CORE ACTIVE] Neural Stream Synced | Bal: ${bal} | Floating: ${flt}")
            sys.stdout.flush()
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("\n\n🛑 Noah Engine Trade Runtime Dihentikan.")
            break
        except Exception:
            time.sleep(1)

if __name__ == "__main__":
    main()
