import random  # Import library untuk angka acak

print("Tebak angka dalam kurungan ini [] (antara 1-10)")
angka_rahasia = random.randint(1, 10)  # Generate angka acak
percobaan = 3  # Maksimal percobaan

while percobaan > 0:
    angka = int(input("Masukkan angka: "))

    if angka == angka_rahasia:
        print("Jawaban Anda BENAR! 🎉")
        break
    elif angka < angka_rahasia:
        print("Terlalu kecil! Coba lagi.")
    else:
        print("Terlalu besar! Coba lagi.")

    percobaan -= 1

if angka != angka_rahasia:
    print(f"Yah, kesempatan habis! Jawabannya adalah {angka_rahasia}.")
