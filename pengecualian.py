# angka1 = '2'
# angka2 = 2
#
# print(angka2  * angka1)


#
# list_nama = ["lala", "blablabla", "lulul"]
#
# print(list_nama[1])
#
# print("======dictonary======")
# list_data =  {
    # "kay" : "value"
#     "la": "lala",
#     "bla": "blablabla",
#     "lu": "lulul",
#     "number": 1000,
#     "list": list_nama
# }
#
# print(list_data["bla"])
# print(list_data["number"])
# print(list_data["list"])
#

#
# data_diri = {
#     "nama": "blabla",
#     "negara": "indonesia",
#     "kota": "mataram ",
#     "hobi": "main bulu tangkis ",
#     "profesi": "mahasiswa"
#
# }
#
#
#
# data_diri1 = {
#     "nama": "blabla",
#     "negara": "indonesia",
#     "kota": "mataram ",
#     "hobi": "main bulu tangkis ",
#     "profesi": "mahasiswa"
#
# }
# print(data_diri,data_diri1)
#



# Soal 1
teman = {
    "nama": "Budi",
    "usia": 25,
    "kota": "Jakarta",
    "hobi": ["membaca", "berenang"]
}
print("Soal 1:")
print(teman)

# Soal 2
print("\nSoal 2:")
teman["profesi"] = "Programmer"
print(teman)

# Soal 3
print("\nSoal 3:")
del teman["usia"]
print(teman)

# Soal 4
print("\nSoal 4:")
if "negara" not in teman:
    teman["negara"] = "Indonesia"
print(teman)

# Soal 5
teman2 = {
    "nama": "Ani",
    "usia": 22,
    "kota": "Surabaya",
    "hobi": ["menulis", "memasak"]
}

teman_gabungan = teman.copy()
teman_gabungan.update(teman2)

print("\nSoal 5:")
print(teman_gabungan)