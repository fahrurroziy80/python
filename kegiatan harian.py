
# Membuat kamus (dictionary) untuk menyimpan jadwal harian
jadwal_harian = {}


# Fungsi untuk menambahkan kegiatan ke jadwal
def tambah_kegiatan():
    jam = input("Masukkan jam (format 24 jam): ")
    kegiatan = input("Masukkan kegiatan: ")
    jadwal_harian[jam] = kegiatan


# Fungsi untuk mencetak jadwal harian
def cetak_jadwal():
    print("\nJadwal Harian Anda:")
    for jam, kegiatan in jadwal_harian.items():
        print(f"{jam}: {kegiatan}")


# Menu utama program
while True:
    print("\nMenu:")
    print("1. Tambah Kegiatan")
    print("2. Cetak Jadwal Harian")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tambah_kegiatan()
    elif pilihan == "2":
        cetak_jadwal()
    elif pilihan == "3":
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai (1/2/3).")