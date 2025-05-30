def hitung_nilai_akhir(pretest,postest,tugas,bonus):
    return (0.25 * pretest) + (0.25 * postest) + (0.50 * tugas) + bonus

def input_praktikan(jumlah_praktikan):
    praktikan = []
    for i in range(jumlah_praktikan):
        print(f"\nMasukkan data untuk praktikan {i+1}:")
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai pretest: "))
        posttest = float(input("Nilai posttest: "))
        tugas = float(input("Nilai tugas: "))
        bonus = float(input("Nilai bonus: "))
        
        nilai_akhir = hitung_nilai_akhir(pretest, posttest, tugas, bonus)
        praktikan.append([nama, nim, nilai_akhir])
    
    return praktikan

def urutkan_praktikan(praktikan):
    for i in range(len(praktikan)):
        for j in range(i + 1, len(praktikan)):
            if praktikan[i][2] < praktikan[j][2]:
                praktikan[i], praktikan[j] = praktikan[j], praktikan[i]

def hitung_rata_rata(praktikan):
    total = 0
    jumlah = len(praktikan)
    for i in range(jumlah):
        total += praktikan[i][2]
    return total / jumlah

def tampilkan_peringkat(praktikan):
    rata_rata = hitung_rata_rata(praktikan)

    print("\nTabel Peringkat Praktikan:")
    print("=" * 50)  
    print(f"{'Nama':<15} {'NIM':<12} {'Nilai Akhir':<12} {'Peringkat':<8}")
    print("=" * 50)

    peringkat = 1
    for i in range(len(praktikan)):
        print(f"{praktikan[i][0]:<15} {praktikan[i][1]:<12} {praktikan[i][2]:<12.2f} {peringkat:<8}")
        peringkat += 1

    print("=" * 50)
    print(f"\nRata-rata nilai akhir: {rata_rata:.2f}")

jumlah_praktikan = int(input("Masukkan jumlah praktikan: "))
data_praktikan = input_praktikan(jumlah_praktikan)
urutkan_praktikan(data_praktikan)
tampilkan_peringkat(data_praktikan)
