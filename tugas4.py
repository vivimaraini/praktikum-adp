print("Manajemen Nilai Mahasiswa Sederhana")

data = []
while True:
    print("\nMENU:")
    print("1. TAMBAH DATA")
    print("2. HAPUS DATA")
    print("3. TAMPILKAN DATA")
    print("4. KELUAR")
    pilihan = input("Pilih menu (1-4):")

    if pilihan == '1':
        print("\nTAMBAH DATA")
        nim = input("Masukkan NIM : ")
        nama = input("Masukkan Nama : ")
        nilai = float (input("Masukkan Nilai :"))
        data.append([nim,nama,nilai])
        print("\nDATA BERHASIL DITAMBAHKAN!!")

    elif pilihan == '2':
        print("\nHAPUS DATA")
        nim_hapus = input("Masukkan NIM Yang Mau Dihapus : ")
        ditemukan = False
        for i in range (len(data)):
            if data[i][0] == nim_hapus:
                del data[i]
                print("\nDATA BERHASIL DIHAPUS!!")
                ditemukan = True
                break
        else:
            print("DATA TIDAK DITEMUKAN.!\n")
            
    elif pilihan == '3':
        print("\nTAMPILKAN DATA")
        if len(data) == 0:
            print("BELUM ADA DATA.\n")
        else:
           n = len (data)
           for i in range (n):
               for j in range(0,n-i-1):
                   if data[j][2]< data[j+1][2]:
                       data[j],data[j+1] = data[j+1],data[j]
                       print("\nData Mahasiswa(Urut Nilai Tertinggi):")
        for mhs in data:
               print(f"NIM: {mhs[0]},Nama:{mhs[1]},Nilai:{mhs[2]}")
                       
    elif pilihan == '4':
        print("PROGRAM SELESAI.TERIMA KASIH!!")   
        break

    else:
        print("PILIHAN TIDAK VALID.SILAHKAN COBA LAGI.\n")    
    









        
