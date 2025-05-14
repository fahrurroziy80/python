import random
import time
import os
import sys

# Cek sistem operasi untuk input keyboard
if os.name == 'nt':  # Windows
    import msvcrt
else:  # Unix/Linux/MacOS
    from getch import getch  # Perlu alternatif, tapi kita buat sederhana dulu

# Ukuran papan
width = 20
height = 10

# Posisi awal ular
snake = [[height//2, width//2]]
direction = [0, 1]  # Mulai ke kanan

# Posisi makanan
food = [random.randint(0, height-1), random.randint(0, width-1)]

# Skor
score = 0

# Fungsi untuk menampilkan papan
def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
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

# Fungsi untuk mendapatkan input (khusus Windows dengan msvcrt)
def get_key():
    if os.name == 'nt' and msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').lower()
        return key
    return None

# Main game loop
def game_loop():
    global direction
    while True:
        print_board()
        time.sleep(0.2)  # Kecepatan game

        # Cek input keyboard
        key = get_key()
        if key == 'w' and direction != [1, 0]:  # Atas
            direction = [-1, 0]
        elif key == 's' and direction != [-1, 0]:  # Bawah
            direction = [1, 0]
        elif key == 'a' and direction != [0, 1]:  # Kiri
            direction = [0, -1]
        elif key == 'd' and direction != [0, -1]:  # Kanan
            direction = [0, 1]
        elif key == 'q':  # Keluar
            break

        # Hitung posisi baru kepala
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        # Cek tabrakan
        if (new_head[0] < 0 or new_head[0] >= height or 
            new_head[1] <