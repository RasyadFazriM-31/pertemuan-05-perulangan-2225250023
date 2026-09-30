# Latihan 2 - Jumlah 1 sampai n
# Input          : bilangan bulat positif n
# Proses         : total dimulai dari 0 (di luar loop), lalu setiap iterasi
#                  ditambah nilai i untuk i = 1, 2, ..., n
# Kondisi berhenti: i sudah melewati n (range(1, n + 1) berhenti sebelum n + 1)
# Output         : jumlah 1 + 2 + ... + n

n = int(input("n: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")
