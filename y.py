# # Buatlah sebuah program Python yang meminta pengguna untuk 
# # memasukkan jari-jari lingkaran dan kemudian menghitung serta mencetak
# # luas lingkaran tersebut.

# import math

# def hitung_luas_lingkaran(jari_jari):
#     return math.pi * jari_jari ** 2

# def main():
#     jari_jari = float(input("masukan panjang jari jari ="))
#     luas = hitung_luas_lingkaran(jari_jari)
    
#     print("luas lingkaran dengan jari jari ", jari_jari, "adalah :", luas)
    
# if __name__ == "__main__"
#     main()
#     main
# import math

# def hitung_luas_lingkaran(jari_jari):
#     return math.pi * jari_jari ** 2

# def main():
#     jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
#     luas = hitung_luas_lingkaran(jari_jari)
#     print("Luas lingkaran dengan jari-jari", jari_jari, "adalah:", luas)

# if __name__ == "__main__":
#     main()

"""progrm 1"""
print("\nPROGRAM KOMVERSI TEMPERATURn/")

Fahrenheit = float(input("masukan suhu dalam Fahranheit:"))
print("suhu dalam fahrenheit adalah ", Fahrenheit)

celcius = (5/9) * (Fahrenheit - 32)
print("suhu dalam calvin adlah ", celcius)

calvin = celcius + 273
print("suhu dalam calvin adalah ", calvin)


"""program 2"""
Kalvin = float(input("masukan suhu dalam kalvin :"))
print("suhu dalam kalvin adalah ", Kalvin)

Celcius = Kalvin - 273
print("suhu dalam Celcius adalah ", Celcius)

fahrenheit = (9/3) * (Celcius) + 32
print("suhu dalam Fahrenheit adalah ", fahrenheit)