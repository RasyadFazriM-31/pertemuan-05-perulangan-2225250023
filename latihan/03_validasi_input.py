# Latihan 3 - Validasi Input Berulang
# Input          : nilai ujian (float), harus berada pada rentang 0 sampai 100
# Proses         : selama nilai < 0 atau nilai > 100, tampilkan pesan salah
#                  lalu baca ulang nilai (pembaruan variabel kontrol)
# Kondisi berhenti: nilai berada di rentang 0 <= nilai <= 100
# Output         : nilai yang diterima

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")
