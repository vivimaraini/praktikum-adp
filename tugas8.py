import os
import time
from termcolor import cprint

# Bersihkan layar sebelum animasi dimulai
os.system('cls')

def animasi_bendera(lebar=25, tinggi_bendera=3, delay=0.15):
    """
    Animasi bendera berkibar dengan efek gelombang.
    
    Args:
    - lebar (int): Lebar bendera.
    - tinggi_bendera (int): Jumlah baris setiap warna bendera.
    - delay (float): Kecepatan animasi dalam detik.
    """
    pola_gelombang = [0, 1, 2, 3, 2, 1]  

    while True:
        for gerakan in range(len(pola_gelombang)):
            os.system("cls")

            # Bagian Merah
            for i in range(tinggi_bendera):
                gelombang = " " * pola_gelombang[(gerakan + i) % len(pola_gelombang)]
                cprint("│", 'white', 'on_black', end='')
                cprint(gelombang + " " + " " * lebar, 'red', 'on_red')

            # Bagian Putih
            for i in range(tinggi_bendera):
                gelombang = " " * pola_gelombang[(gerakan + i + 1) % len(pola_gelombang)]
                cprint("│", 'white', 'on_black', end='')
                cprint(gelombang + " " + " " * lebar, 'white', 'on_white')

            # Tiang Bendera
            for _ in range(8):
                cprint("│", 'white', 'on_black', end='')

            time.sleep(delay)  

# Jalankan animasi
animasi_bendera()
