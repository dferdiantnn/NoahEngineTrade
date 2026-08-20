# ⚡ NOAH ENGINE TRADE (NET) V5.0
> **High-Performance Quantitative Trading System, Interactive 2D Chart Navigation & Multi-Layer Money Management for MetaTrader 5 (MT5)**

![Version](https://img.shields.io/badge/version-5.00-gold.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-MetaTrader%205%20(MT5)-navy.svg?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Cryptographic%20SHA--256-green.svg?style=for-the-badge)
![OS Support](https://img.shields.io/badge/OS-Windows%20%7C%20macOS%20%7C%20Linux-purple.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-Commercial%20Proprietary-red.svg?style=for-the-badge)

---

## 🌟 Tentang Noah Engine Trade (NET)

**Noah Engine Trade (NET)** adalah sistem trading kuantitatif mutakhir yang dirancang khusus untuk platform **MetaTrader 5 (MT5)**. Sistem ini menggabungkan eksekusi algoritma berkecepatan tinggi, manajemen risiko split-layer dinamis, navigasi grafik 2D bebas, serta perlindungan lisensi kriptografi tingkat tinggi.

---

## ✨ Fitur Utama Sistem

```
┌──────────────────────────────────────────────────────────┐
│  # NOAH TRADING ENGINE V5.0                  [ LIFETIME ]│
├──────────────────────────────────────────────────────────┤
│  STATUS       : # BUY  (0.06 Lot / 6 Layers)             │
│  ENTRY AVG    : [AUTO] 4487.44  │  QUANT: 4487.69        │
│  FLOATING PnL : +$1.68 USD  (+27 Pips)                   │
│  EQUITY LIVE  : $388.79 USD  (Bal: $387.11)              │
├──────────────────────────────────────────────────────────┤
│  LAYER BREAKDOWN:                                        │
│  #1 [A] SL:605p TP:RUN(MAX) Profit: +$0.27 USD           │
│  #2 [A] SL:605p TP:994p     Profit: +$0.27 USD           │
│  #3 [A] SL:605p TP:794p     Profit: +$0.27 USD           │
│  #4 [A] SL:605p TP:594p     Profit: +$0.27 USD           │
│  #5 [A] SL:605p TP:394p     Profit: +$0.27 USD           │
│  #6 [A] SL:600p TP:200p     Profit: +$0.27 USD           │
├──────────────────────────────────────────────────────────┤
│  AUTO-BE: [ON] │ MAN: 0  │ AUT: 6  │ NEXT: 06:51         │
└──────────────────────────────────────────────────────────┘
```

### 1. 🖱️ Dynamic 2D Free Chart Drag Navigation
- **Geser Bebas 4 Arah**: Anda dapat mengklik dan menggeser grafik chart ke **Atas, Bawah, Kiri, dan Kanan** secara bebas layaknya pengalaman modern di TradingView.
- **Auto-Fit Reset**: Tekan tombol **Spasi (`Space`)** atau huruf **`R`** untuk mengembalikan skala vertikal chart ke standar otomatis.

### 2. 🎮 4-Way Arrow Precision Controls
- ⬆️ **Panah Atas**: Eksekusi Instant Buy Manual (Split Layers).
- ⬇️ **Panah Bawah**: Eksekusi Instant Sell Manual (Split Layers).
- ⬅️ **Panah Kiri**: Menutup semua posisi Manual (`[M]`).
- ➡️ **Panah Kanan**: Menutup semua posisi Auto Engine (`[A]`).

### 3. 📊 Real-Time Account & Risk HUD
- **`EQUITY LIVE`**: Memantau perkembangan modal ekuiti dan balance secara real-time.
- **`NEXT: mm:ss`**: Hitung mundur penutupan candlestick aktif langsung di dalam footer HUD.
- **`LAST CLOSED`**: Rekapitulasi profit/loss transaksi terakhir saat mode Standby.

### 4. 🔐 Cryptographic License Security
- Sistem diamankan dengan algoritma enkripsi SHA-256 yang dikunci khusus ke Nomor Akun MT5 pengguna dan masa aktif lisensi.

---

## 📖 Panduan Penginstalan & Penggunaan

### 1. Pemasangan Expert Advisor di MT5
1. Salin file `mql5/Manager.ex5` ke folder `MQL5/Experts/manager/` di MetaTrader 5 Anda.
2. Buka MT5 $\rightarrow$ buka chart pair pilihan Anda (misal **XAUUSD / Gold M15**).
3. Drag `Manager` dari panel *Navigator* ke chart.
4. Pada tab **Umum (Common)**, centang **Izinkan Trading Algo (Allow Algo Trading)**.
5. Pada tab **Masukan (Inputs)**, masukkan **Serial Key Lisensi** resmi Anda di baris `InpLicenseKey`.
6. Klik **OK**.

### 2. Menjalankan Engine Runtime
1. Buka Terminal / CMD:
   ```bash
   python3 engine/noah_runtime.py
   ```
   *(Pengguna macOS cukup klik 2x file `RunNoahEngine.command`)*.
2. Engine kuantitatif akan otomatis terhubung ke MT5 dan melakukan sinkronisasi data secara real-time.

---

## 👥 Pengembang & Kontak Lisensi

| Identitas | Keterangan |
| :---: | :--- |
| **Author** | **Ferr - Noah Trading System** ([@dferdiantnn](https://github.com/dferdiantnn)) |
| **Lisensi & Layanan** | Untuk aktivasi serial key akun MT5, hubungi Admin: [@dferdiantnn](https://t.me/dferdiantnn) |

---

## ⚠️ Disclaimer
*Trading derivatif dan instrumen valuta asing memiliki risiko modal yang tinggi. Selalu uji coba strategi pada akun demo dan pastikan Anda menerapkan manajemen risiko yang bijak.*

**Copyright © 2026 Ferr - Noah Trading System. All Rights Reserved.**
