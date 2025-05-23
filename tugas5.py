print("-"*38)
print("\nPROGRAM MENGHITUNG JARAK ANTAR TITIK\n")
print("-"*38)

n = int(input("masukkan jumlah titik: "))
point = []
for i in range (n):
    print(f" masukkan koordinat titik ke {i+1}: ")
    x = float(input(" x: "))
    y = float(input(" y: "))
    point.append([x, y])
    
print("\nKumpulan titik:", point)
print("\nJarak Antar titik:")

for i in range(len(point)):
    for j in range(i+1,len(point)) :
        dx = point[j][0]-point[i][0]
        dy = point[j][1]-point[i][1]
        jarak = (dx**2 + dy**2)**0.5
        print(f"jarak antara {point[i]} dan {point[j]} : {jarak:.2f}")