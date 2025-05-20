#data pelanggan beserta total benjaan mereka
data_pelanggan = {
    {"nama": "Andi", "total_belnja": 250},
    {"nama": "Budi", "total_belnja": 400},
    {"nama": "Cindy", "total_belnja": 700},
    {"nama": "Deni", "total_belnja": 550},
    {"nama": "Eva", "total_belnja": 300},

}

#inisialisasi variabel untuk menyimpan informasi pelanggan dengan total
pelanggan_tertinggi = ""
total_tertinggi = 0

#melakukan  interansi pada setiap data pelanggan untuk menemukan total belanja
for pelanggan in data_pelanggan:
    nama_pelanggan = pelanggan("nama")
    total_belanja = pelanggan("total_belanja")

#memeriksa apakah total belanja pelanggan saat ini lebih tinggi dari total_tertinggi yang sudah di temukan

    if total_belanja > total_tertinggi:
        total_tertinggi = total_belanja
        pelanggan_tertinggi = nama_pelanggan

#menampilkan pelanggan dengan total belanja tertinggi

print(f"Pelanggan dengan total belanja tertinggi adalah {pelanggan_tertinggi} dengan total belanja sebesar {total_tertinggi}")

