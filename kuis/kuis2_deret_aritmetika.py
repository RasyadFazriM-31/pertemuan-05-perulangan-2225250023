# Kuis 2 - Deret Aritmetika
# Input           : suku pertama a (float), beda d (float), banyak suku n (int > 0)
# Proses          : 1) while: ulangi input n selama n <= 0 (validasi)
#                   2) total dimulai dari 0 di luar loop
#                   3) for i dari 0 sampai n - 1: suku = a + i * d,
#                      tampilkan suku, lalu tambahkan ke total
# Kondisi berhenti: while berhenti saat n > 0; for berhenti setelah tepat n iterasi
# Output          : n suku pertama dan jumlah deret (dua angka di belakang koma)
# Catatan         : jumlah dihitung dengan akumulasi, bukan rumus jumlah deret

print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi berulang: n harus bilangan bulat positif
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

total = 0
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Jumlah = {total:.2f}")
