import os
import time
from termcolor import cprint

os.system('cls')

def animasi_bendera():
    lebar = 25  
    pola_gelombang = [0, 1, 2, 3, 2, 1]  # Pola gelombang lebih dinamis
    tinggi_bendera = 3  

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

            time.sleep(0.15)  # Memberikan efek berkibar lebih alami

animasi_bendera()
