print("SELAMAT DATANG DI KONSER BTS")
#tata letak kursi
baris = 6
kolom = 5
total_kursi = baris * kolom
#harga tiket
harga_tiket ={
    "VVIP" : 1000000,
    "VIP" : 500000,
    "Reguler" : 250000,
    "Ekonomi" :100000
}
#kategori kursi
kursi_per_kategori = total_kursi //4
#tempat duduk
tempat_duduk = [[(i * kolom + j + 1) for j in range(kolom)] for i in range(baris)]
#data pemesanan
pemesanan =[]
print("\n Selamat datang di reservasi tiket konser!\n")
print(f"Kami menyediakan tempat duduk dengan ukuran {baris} x {kolom}\n")
print("Tata Letak Tempat Duduk:\n")
for i in range (baris):
    for j in range (kolom):
        print(tempat_duduk[i][j],end="\t")
    print()

print("\n===== Harga Tiket =====")
for kategori in harga_tiket:
    print(f"{kategori}: Rp{harga_tiket[kategori]:,}")

jumlah_tiket = int(input(" Masukkan jumlah tiket yang ingin dipesan: "))

for i in range(jumlah_tiket):
    print(f" Pemesanan ke-{i+1}:")
    nama = input("Masukkan nama Anda :")
    nomor_kursi = int(input("Masukkan nomor kursi yang ingin dipesan :"))
    tanggal = input("Masukkan tanggal pemesanan :")
    metode_pembayaran = input("Metode pembayaran (contoh: GoPay,OVO,Transfer Bank) :")
    password = input("Password akses masuk konser :")
#menentukan kategori berdasarkan nomor kursi
    kategori = ""
    if 1 <= nomor_kursi <= kursi_per_kategori :
        kategori = "VVIP"
    elif nomor_kursi <= 2 * kursi_per_kategori :
        kategori = "VIP"
    elif nomor_kursi <= 3 * kursi_per_kategori :
        kategori = "Reguler"
    else:
        kategori = "Ekonomi"

    harga = harga_tiket[kategori]
    pemesanan += [{"nama":nama , "kursi":nomor_kursi , "kategori":kategori , "harga":harga , "password":password , "tanggal":tanggal , "metode_pembayaran":metode_pembayaran }]

#menandai kursi yang terisi 
    for b in range(baris):
        for k in range(kolom):
            if tempat_duduk[b][k] == nomor_kursi :
                tempat_duduk[b][k] = 0
                break

    print("\n====== Struk Pemesanan Tiket ======")
    print(f"Nama:{nama}")
    print(f"Nomor Kursi:{nomor_kursi}")
    print(f"Kategori:{kategori}")
    print(f"Harga: Rp{harga :,}")
    print(f"Tanggal Pemesanan:{tanggal}")
    print(f"Metode Pembayaran:{metode_pembayaran}")
    print(f"Password:{password}")

print("...................................")

#menghitung sisa kursi
sisa_kursi = {kategori : kursi_per_kategori for kategori in harga_tiket}
for data in pemesanan :
    sisa_kursi[data["kategori"]] -= 1

print("\nSisa Kursi Per Kategori :")
for kategori in sisa_kursi:
    print(f"{kategori}:{sisa_kursi[kategori]}")

print("\nTata Letak Tempat Duduk Setelah Pemesanan:")
for i in range(baris):
    for j in range(kolom):
        print(tempat_duduk[i][j],end = "\t" )
    print()

print("\n===== TERIMA KASIH TELAH MELAKUKAN RESERVASI!! =====")



