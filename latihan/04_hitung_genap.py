# Latihan 4 - Menghitung Bilangan Genap
# Input          : bilangan bulat positif n
# Proses         : jumlah_genap dimulai dari 0 (di luar loop); untuk setiap i
#                  dari 1 sampai n, jika i habis dibagi 2 maka jumlah_genap + 1
# Kondisi berhenti: i sudah melewati n (range(1, n + 1))
# Output         : banyak bilangan genap dari 1 sampai n

n = int(input("n: "))

jumlah_genap = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print(f"Banyak bilangan genap = {jumlah_genap}")
