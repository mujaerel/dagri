import csv

# Nama file CSV
FILE = 'jadwal.csv'

# Header kolom
HEADER = ['No', 'Maskapai', 'Asal', 'Tujuan', 'Tanggal', 'Berangkat', 'Tiba']

# Data awal
DATA = [
    ['001', 'Garuda Indonesia', 'Jakarta', 'Surabaya', '2025-05-10', '08:00', '09:30'],
    ['002', 'Lion Air', 'Surabaya', 'Bali', '2025-05-10', '11:00', '12:00'],
    ['003', 'Batik Air', 'Bali', 'Jakarta', '2025-05-11', '14:45', '16:30'],
    ['004', 'Citilink', 'Jakarta', 'Medan', '2025-05-12', '07:00', '09:45'],
    ['005', 'Sriwijaya Air', 'Medan', 'Bandung', '2025-05-12', '13:00', '15:15']
]

# Simpan ke file CSV
def buat_file_jadwal():
    with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(DATA)
    print(f"File '{FILE}' berhasil dibuat dengan data awal.")

# Jalankan
buat_file_jadwal()
