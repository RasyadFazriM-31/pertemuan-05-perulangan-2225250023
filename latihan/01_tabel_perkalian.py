# Latihan 1 - Tabel Perkalian
# Input          : satu bilangan bulat n
# Proses         : for mengulang i dari 1 sampai 10, hitung n * i
# Kondisi berhenti: i sudah melewati 10 (range(1, 11) berhenti sebelum 11)
# Output         : 10 baris "n x i = hasil"

n = int(input("Bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")
