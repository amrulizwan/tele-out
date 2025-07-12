# Telegram Group Leave Script

A Python script to leave all Telegram groups at once with per-group confirmation system. This script uses the Telethon library and provides interactive controls to choose which groups to leave.

## 🚀 Features

- ✅ Leave all Telegram groups at once
- ✅ Per-group confirmation with keyboard controls
- ✅ Automatic detection of groups and channels
- ✅ User-friendly interface
- ✅ Robust error handling
- ✅ Session management for quick login

## 📋 Requirements

- Python 3.7 or higher
- Valid Telegram account
- Telegram API credentials

## 🛠️ Installation

### 1. Clone or Download Project

```bash
git clone https://github.com/amrulizwan/tele-out.git
cd tele-out
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Configuration

### 1. Get API Credentials

1. Go to <https://my.telegram.org>
2. Login with your Telegram phone number
3. Select "API Development Tools"
4. Create a new application:
   - **App title:** Enter app name (example: "Leave Groups Bot")
   - **Short name:** Enter short name (example: "leavebot")
   - **Platform:** Select "Desktop"
5. Note down the `api_id` and `api_hash` provided

### 2. Edit Script Configuration

Open `leave_groups.py` file and replace the following lines:

```python
api_id = 'YOUR_API_ID'           # Replace with your API ID
api_hash = 'YOUR_API_HASH'       # Replace with your API Hash
phone_number = 'YOUR_PHONE'      # Replace with your phone number (format: +6281234567890)
```

**Example:**

```python
api_id = '12345678'
api_hash = 'abcdef1234567890abcdef1234567890'
phone_number = '+6281234567890'
```

## 🎮 How to Use

### 1. Run the Script

```bash
python leave_groups.py
```

### 2. First Time Login

- Enter the verification code sent to your Telegram
- If using 2FA, enter your password
- Session will be saved for future logins

### 3. Interactive Controls

For each group found:

- **Press ENTER** → Leave the group
- **Press ESC** → Cancel (don't leave the group)

### 4. Script Output

```
Retrieving group list...
Found 15 groups.

Leave group: Work Team Group
Press ENTER to leave, ESC to cancel: LEAVE
Successfully left group: Work Team Group

Leave group: News Channel
Press ENTER to leave, ESC to cancel: CANCEL
Cancelled leaving group: News Channel

...

Finished processing all groups.
```

## 📁 File Structure

```
tele-out/
├── leave_groups.py          # Main script
├── requirements.txt         # Dependencies
├── README.md               # Documentation
├── .venv/                  # Virtual environment
└── session_name.session    # Telegram session file (auto-created)
```

## ⚠️ Important Warnings

1. **Backup Data:** This script will delete group dialogs, make sure you're certain
2. **Rate Limiting:** Telegram has API limits, don't spam
3. **Terms of Service:** Follow Telegram ToS to avoid account bans
4. **Session File:** Keep session file secure, don't share with others

## 🐛 Troubleshooting

### Error: 'Chat' object has no attribute 'megagroup'

**Solution:** Update to the latest script version that fixes this bug.

### Error: Invalid phone number

**Solution:** Make sure phone number format is correct with country code (+62 for Indonesia).

### Error: API credentials invalid

**Solution:**

1. Double-check `api_id` and `api_hash`
2. Make sure there are no typos
3. Recreate API credentials if necessary

### Script doesn't respond to keyboard input

**Solution:**

- Make sure terminal supports interactive input
- Try running in Command Prompt/Git Bash
- Make sure no other program is using keyboard

## 📝 Logs and Session

- **Session File:** `session_name.session` - Stores login information
- **Log Output:** Displayed directly in terminal
- **Error Handling:** All errors will be displayed with clear messages

## 🔧 Customization

You can modify the script to:

- Change session file name
- Add specific group filters
- Modify output format
- Add file logging

## 📞 Support

If you encounter issues:

1. Make sure all requirements are met
2. Check API credentials configuration
3. Try restarting the script
4. Check internet connection

## 📄 License

This script is created for personal use. Use wisely and follow Telegram Terms of Service.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Konfigurasi API

### 1. Dapatkan API Credentials

1. Buka <https://my.telegram.org>
2. Login dengan nomor telepon Telegram Anda
3. Pilih "API Development Tools"
4. Buat aplikasi baru:
   - **App title:** Masukkan nama aplikasi (contoh: "Leave Groups Bot")
   - **Short name:** Masukkan nama pendek (contoh: "leavebot")
   - **Platform:** Pilih "Desktop"
5. Catat `api_id` dan `api_hash` yang diberikan

### 2. Edit Konfigurasi Script

Buka file `leave_groups.py` dan ganti baris berikut:

```python
api_id = 'YOUR_API_ID'           # Ganti dengan API ID Anda
api_hash = 'YOUR_API_HASH'       # Ganti dengan API Hash Anda
phone_number = 'YOUR_PHONE'      # Ganti dengan nomor telepon Anda (format: +6281234567890)
```

**Contoh:**

```python
api_id = '12345678'
api_hash = 'abcdef1234567890abcdef1234567890'
phone_number = '+6281234567890'
```

## 🎮 Cara Penggunaan

### 1. Jalankan Script

```bash
python leave_groups.py
```

### 2. Login Pertama Kali

- Masukkan kode verifikasi yang dikirim ke Telegram Anda
- Jika menggunakan 2FA, masukkan password
- Session akan disimpan untuk login berikutnya

### 3. Kontrol Interaktif

Untuk setiap grup yang ditemukan:

- **Tekan ENTER** → Keluar dari grup
- **Tekan ESC** → Batalkan (tidak keluar dari grup)

### 4. Output Script

```
Mengambil daftar grup...
Ditemukan 15 grup.

Keluar dari grup: Grup Kerja Tim
Tekan ENTER untuk keluar, ESC untuk batal: KELUAR
Berhasil keluar dari grup: Grup Kerja Tim

Keluar dari grup: Channel Berita
Tekan ENTER untuk keluar, ESC untuk batal: BATAL
Membatalkan keluar dari grup: Channel Berita

...

Selesai memproses semua grup.
```

## 📁 Struktur File

```
tele-out/
├── leave_groups.py          # Script utama
├── requirements.txt         # Dependencies
├── README.md               # Dokumentasi
├── .venv/                  # Virtual environment
└── session_name.session    # File session Telegram (dibuat otomatis)
```

## ⚠️ Peringatan Penting

1. **Backup Data:** Script ini akan menghapus dialog grup, pastikan Anda yakin
2. **Rate Limiting:** Telegram memiliki batas API, jangan spam
3. **Terms of Service:** Patuhi ToS Telegram untuk menghindari banned
4. **Session File:** Jaga keamanan file session, jangan bagikan ke orang lain

## 🐛 Troubleshooting

### Error: 'Chat' object has no attribute 'megagroup'

**Solusi:** Update ke versi terbaru script yang sudah memperbaiki bug ini.

### Error: Invalid phone number

**Solusi:** Pastikan format nomor telepon benar dengan kode negara (+62 untuk Indonesia).

### Error: API credentials invalid

**Solusi:**

1. Periksa kembali `api_id` dan `api_hash`
2. Pastikan tidak ada typo
3. Buat ulang API credentials jika perlu

### Script tidak merespons input keyboard

**Solusi:**

- Pastikan terminal mendukung input interaktif
- Coba jalankan di Command Prompt/Git Bash
- Pastikan tidak ada program lain yang menggunakan keyboard

## 📝 Log dan Session

- **File Session:** `session_name.session` - Menyimpan informasi login
- **Log Output:** Ditampilkan langsung di terminal
- **Error Handling:** Semua error akan ditampilkan dengan pesan yang jelas

## 🔧 Customization

Anda dapat memodifikasi script untuk:

- Mengubah nama file session
- Menambah filter grup tertentu
- Mengubah format output
- Menambah logging ke file

## 📞 Support

Jika mengalami masalah:

1. Pastikan semua persyaratan terpenuhi
2. Periksa konfigurasi API credentials
3. Coba restart script
4. Periksa koneksi internet

## 📄 License

Script ini dibuat untuk keperluan personal. Gunakan dengan bijak dan patuhi Terms of Service Telegram.
