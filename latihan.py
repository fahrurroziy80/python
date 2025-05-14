import random
import time
import os

# Ukuran papan permainan
width = 20
height = 10

# Posisi awal ular
snake = [[height//2, width//2]]
direction = [0, 1]  # [y, x] awalnya ke kanan

# Posisi makanan
food = [random.randint(0, height-1), random.randint(0, width-1)]

# Skor
score = 0

# Fungsi untuk menampilkan papan
def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar
    for y in range(height):
        for x in range(width):
            if [y, x] in snake:
                print('O', end=' ')
            elif [y, x] == food:
                print('*', end=' ')
            else:
                print('.', end=' ')
        print()
    print(f"Skor: {score}")

# Game loop
while True:
    print_board()
    time.sleep(0.2)  # Kontrol kecepatan

    # Input sederhana (hanya untuk demo, bisa dimodifikasi)
    # Untuk versi ini, ular bergerak otomatis ke arah terakhir
    # Untuk kontrol manual, uncomment baris berikut dan sesuaikan:
    # move = input("Arah (w/a/s/d): ")
    # if move == 'w': direction = [-1, 0]
    # elif move == 's': direction = [1, 0]
    # elif move == 'a': direction = [0, -1]
    # elif move == 'd': direction = [0, 1]

    # Hitung posisi baru kepala
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

    # Cek batas
    if (new_head[0] < 0 or new_head[0] >= height or
        new_head[1] < 0 or new_head[1] >= width or
        new_head in snake):
        print(f"Game Over! Skor akhir: {score}")
        break

    # Tambah kepala
    snake.insert(0, new_head)

    # Cek makanan
    if new_head == food:
        score += 1
        food = [random.randint(0, height-1), random.randint(0, width-1)]
    else:
        snake.pop()  # Hapus ekor jika tidak makan
