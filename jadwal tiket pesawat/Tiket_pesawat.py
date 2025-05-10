import csv
from datetime import datetime, timedelta

FILE = 'jadwal.csv'
HEADER = ['No', 'Maskapai', 'Asal', 'Tujuan', 'Tanggal', 'Berangkat', 'Tiba']

def muat_data():
    try:
        with open(FILE, 'r') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def simpan_data(data):
    with open(FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(data)

def hitung_durasi(berangkat, tiba):
    try:
        waktu_berangkat = datetime.strptime(berangkat, "%Y-%m-%d %H:%M")
        waktu_tiba = datetime.strptime(tiba, "%Y-%m-%d %H:%M")
        if waktu_tiba < waktu_berangkat:
            waktu_tiba += timedelta(days=1)
        selisih = waktu_tiba - waktu_berangkat
        return f"{selisih.seconds // 3600} jam {selisih.seconds % 3600 // 60} menit"
    except Exception as e:
        return f"Error: {e}"

def tampilkan():
    data = muat_data()
    if not data:
        print("\nTidak ada data jadwal penerbangan.")
        return

    print("\nDaftar Penerbangan:")
    print("No  | Maskapai        | Asal  | Tujuan | Tanggal     | Berangkat | Tiba   | Durasi")
    for row in data:
        durasi = hitung_durasi(
            f"{row['Tanggal']} {row['Berangkat']}",
            f"{row['Tanggal']} {row['Tiba']}"
        )
        print(f"{row['No']:4}| {row['Maskapai'][:15]:15} | {row['Asal'][:5]:5} | {row['Tujuan'][:6]:6} | {row['Tanggal']:10} | {row['Berangkat']:9} | {row['Tiba']:6} | {durasi}")

def validasi_tanggal(teks):
    try:
        datetime.strptime(teks, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validasi_waktu(teks):
    try:
        datetime.strptime(teks, "%H:%M")
        return True
    except ValueError:
        return False

def tambah():
    data = muat_data()
    no = input("No Penerbangan: ")
    if any(row['No'] == no for row in data):
        print("No penerbangan sudah ada!")
        return

    maskapai = input("Nama Maskapai: ")
    asal = input("Bandara Asal: ")
    tujuan = input("Bandara Tujuan: ")

    tanggal = input("Tanggal (YYYY-MM-DD): ")
    if not validasi_tanggal(tanggal):
        print("Format tanggal salah!")
        return

    berangkat = input("Waktu Berangkat (HH:MM): ")
    if not validasi_waktu(berangkat):
        print("Format waktu berangkat salah!")
        return

    tiba = input("Waktu Tiba (HH:MM): ")
    if not validasi_waktu(tiba):
        print("Format waktu tiba salah!")
        return

    baru = {
        'No': no,
        'Maskapai': maskapai,
        'Asal': asal,
        'Tujuan': tujuan,
        'Tanggal': tanggal,
        'Berangkat': berangkat,
        'Tiba': tiba
    }
    data.append(baru)
    simpan_data(data)
    print("Data berhasil ditambahkan!")

def edit():
    data = muat_data()
    no = input("Masukkan No Penerbangan yang akan diedit: ")
    for row in data:
        if row['No'] == no:
            print("Kosongkan jika tidak ingin mengubah:")
            for key in HEADER:
                if key != 'No':
                    val_lama = row[key]
                    val_baru = input(f"{key} ({val_lama}): ").strip()
                    if val_baru:
                        if key == 'Tanggal' and not validasi_tanggal(val_baru):
                            print("Format tanggal salah. Lewati perubahan.")
                        elif key in ['Berangkat', 'Tiba'] and not validasi_waktu(val_baru):
                            print("Format waktu salah. Lewati perubahan.")
                        else:
                            row[key] = val_baru
            simpan_data(data)
            print("Data berhasil diperbarui.")
            return
    print("Data tidak ditemukan.")

def hapus():
    data = muat_data()
    no = input("Masukkan No Penerbangan yang akan dihapus: ")
    for row in data:
        if row['No'] == no:
            konfirmasi = input(f"Yakin ingin menghapus penerbangan {no}? (y/n): ").lower()
            if konfirmasi == 'y':
                data = [r for r in data if r['No'] != no]
                simpan_data(data)
                print("Data berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            return
    print("Data tidak ditemukan.")

# Program utama
def main():
    while True:
        print("\nAPLIKASI JADWAL PENERBANGAN")
        print("1. Lihat Jadwal")
        print("2. Tambah Jadwal")
        print("3. Edit Jadwal")
        print("4. Hapus Jadwal")
        print("5. Keluar")

        pilih = input("Pilih menu (1-5): ").strip()
        if pilih == '1':
            tampilkan()
        elif pilih == '2':
            tambah()
        elif pilih == '3':
            edit()
        elif pilih == '4':
            hapus()
        elif pilih == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Input salah! Pilih angka 1-5.")

if __name__ == "__main__":
    main()
