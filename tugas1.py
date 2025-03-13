print("=============== Daftar Menu ===============")
print("Paket A: Nasi Goreng + Es Teh","Harga : Rp 30.000") 
print("Paket B: Ayam Bakar + Nasi Putih + Es Jeruk","Harga : Rp 50.000")
print("Paket C: Sate Ayam + Es Pelangi","Harga : Rp 35.000")
print("Paket D: Ayam Goreng + Nasi Putih + Es Milo","Harga : Rp 40.000")   
print("Paket E: Ikan Gulai + Nasi Putih + Es Cincau","Harga : Rp 45.000")
print("-"*45)

# input informasi pelanggan
nama = input("Masukkan nama anda:")
telepon = int(input("Masukkan nomor telepon:"))
alamat = input("Masukkan alamat anda:")

# input pemesanan
pilihan_paket = input("Masukkan pilihan anda(Paket A / Paket B / Paket C / Paket D / Paket E):")
jumlah_paket = int(input("Masukkan jumlah yang diinginkan: "))

if pilihan_paket == "Paket A":
    harga_paket = 30000
    isi_paket = "Nasi Goreng + Es Teh"
    print("Paket A")
elif pilihan_paket == "Paket B":
    harga_paket = 50000
    isi_paket =  "Ayam Bakar + Nasi Putih + Es Jeruk"
    print("Paket B")
elif pilihan_paket == "Paket C":
    harga_paket = 35000
    isi_paket = "Sate Ayam + Es Pelangi"
    print("Paket C")
elif pilihan_paket == "Paket D":
    harga_paket = 40000
    isi_paket = "Ayam Goreng + Nasi Putih + Es Milo"
    print("Paket D")
elif pilihan_paket == "Paket E":
    harga_paket = 45000
    isi_paket = "Ikan Gulai + Nasi Putih + Es Cincau"
    print("Paket E")
else:
    print("paket tidak tersedia")
    exit()

total_harga = harga_paket * jumlah_paket 
pajak = total_harga * 0.10
biaya_antar = "biaya antar:"
if total_harga < 150000 :
    biaya_antar = 25000
else :
    biaya_antar = 0
jumlah_semua = total_harga + pajak + biaya_antar

print("-"*45)

print("=============== Struk Pemesanan ===============")
print(f"Nama: {nama}")
print(f"Nomor Telepon: {telepon}")
print(f"Alamat Pengiriman: {alamat}")

print("-"*45)

print("=============== Detail Pesanan ===============")
print(f"Paket : {pilihan_paket}")
print(f"Isi Paket : {isi_paket}")
print(f"Jumlah : {jumlah_paket}")
print(f"Total Harga : Rp {total_harga}")
print(f"Pajak(10%) : Rp {pajak}")
print(f"Biaya Antar : Rp {biaya_antar}")

print("_"*45)
print(f"Jumlah Semua : Rp {jumlah_semua}")

print("_"*45)
print("TERIMA KASIH SUDAH MEMESAN MAKANAN KAMI \nSemangat Menikmati \nJangan lupa baca bismillah sebelum makan")