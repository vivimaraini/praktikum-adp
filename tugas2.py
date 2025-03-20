#misalkan n(t) adalah variabel acak poisson dengan parameter lamda t besar dari 0
print("=============== Menghitung P(N(T) = n) ===============")
lambda_t = float(input("masukan nilai lamda*t :"))
M = int(input("masukan nilai parameter:"))
e = 2.71828
n = 0
faktorial = 1
hasil =  (e**(-lambda_t)) * ((lambda_t ** n) / faktorial)
while n <= M :
    if hasil < 1e-10:
        print(f"Nilai untuk n = {n} = 0")
    else :
        print(f"Nilai untuk n ={n}:{hasil:.6f}")
    n += 1
    if n > M :
        break  
    faktorial *= n
    hasil *= lambda_t / n
