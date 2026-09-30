# Pertemuan 05 Perulangan Python

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A
Program Studi: Pendidikan Matematika 
Mata Kuliah: Algoritma dan Pemrograman

## Tujuan

Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif, meliputi:

- perulangan `for` dengan `range` untuk jumlah iterasi yang diketahui,
- perulangan `while` dengan kondisi berhenti dan validasi input berulang,
- seleksi `if` di dalam perulangan,
- akumulasi (penjumlahan berulang) dan pencacahan (penghitungan kejadian).

## Struktur Folder

```
pertemuan-05-perulangan-2225250023/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
└── kuis/
    └── kuis2_deret_aritmetika.py
```

## Cara Menjalankan

Jalankan dari root folder proyek. Pada Windows gunakan `python`, pada macOS/Linux gunakan `python3`.

```
python3 latihan/01_tabel_perkalian.py
python3 latihan/02_jumlah_bilangan.py
python3 latihan/03_validasi_input.py
python3 latihan/04_hitung_genap.py
python3 kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

Program menampilkan n suku pertama deret aritmetika dan menghitung jumlahnya dengan perulangan.

1. Baca suku pertama `a` dan beda `d` sebagai bilangan desimal (float).
2. Baca banyak suku `n` sebagai bilangan bulat.
3. Selama `n <= 0`, tampilkan pesan kesalahan dan baca `n` kembali (`while`). Perulangan ini berhenti saat `n` positif.
4. Set `total = 0` sebelum perulangan `for`.
5. Ulangi `i` dari 0 sampai `n - 1` (`for i in range(n)`, tepat n iterasi):
   - hitung `suku = a + i * d`,
   - tambahkan `suku` ke `total`,
   - tampilkan nomor suku (`i + 1`) dan nilainya.
6. Setelah perulangan selesai, tampilkan `total` dengan dua angka di belakang koma.

Pilihan struktur: `while` dipakai untuk validasi karena jumlah pengulangan input tidak diketahui di awal. `for` dipakai untuk menghasilkan suku karena jumlah iterasinya diketahui, yaitu n. Jumlah deret dihitung dengan akumulasi, bukan dengan rumus jumlah deret.

Tracing untuk a = 2, d = 3, n = 5:

| i | suku | total sebelum | total sesudah |
|---|------|---------------|---------------|
| 0 | 2    | 0             | 2             |
| 1 | 5    | 2             | 7             |
| 2 | 8    | 7             | 15            |
| 3 | 11   | 15            | 26            |
| 4 | 14   | 26            | 40            |

## Hasil Pengujian

### Latihan 1 - Tabel Perkalian

| Input n | Keluaran yang diharapkan | Keluaran aktual | Status |
|---------|--------------------------|-----------------|--------|
| 4       | 4 x 1 = 4 sampai 4 x 10 = 40 (10 baris) | 4 x 1 = 4 sampai 4 x 10 = 40 (10 baris) | Sesuai |
| -3      | -3 x 1 = -3 sampai -3 x 10 = -30 (10 baris) | -3 x 1 = -3 sampai -3 x 10 = -30 (10 baris) | Sesuai |

### Latihan 2 - Jumlah 1 sampai n

| Input n | Keluaran yang diharapkan | Keluaran aktual | Status |
|---------|--------------------------|-----------------|--------|
| 1       | Jumlah = 1               | Jumlah = 1      | Sesuai |
| 5       | Jumlah = 15              | Jumlah = 15     | Sesuai |
| 10      | Jumlah = 55              | Jumlah = 55     | Sesuai |

### Latihan 3 - Validasi Input

| Input (berurutan) | Keluaran yang diharapkan | Keluaran aktual | Status |
|-------------------|--------------------------|-----------------|--------|
| 120, -5, 75 | 120 dan -5 ditolak, 75 diterima | "Nilai tidak valid." dua kali, lalu "Nilai diterima: 75.0" | Sesuai |

### Latihan 4 - Menghitung Bilangan Genap

| Input n | Keluaran yang diharapkan | Keluaran aktual | Status |
|---------|--------------------------|-----------------|--------|
| 1       | 0                        | 0               | Sesuai |
| 2       | 1                        | 1               | Sesuai |
| 5       | 2                        | 2               | Sesuai |
| 10      | 5                        | 5               | Sesuai |

### Kuis 2 - Deret Aritmetika

| a, d, n | Keluaran yang diharapkan | Keluaran aktual | Status |
|---------|--------------------------|-----------------|--------|
| 2, 3, 5 | Suku 2, 5, 8, 11, 14; jumlah 40 | Suku 2.00, 5.00, 8.00, 11.00, 14.00; Jumlah = 40.00 | Sesuai |
| 10, -2, 4 | Suku 10, 8, 6, 4; jumlah 28 | Suku 10.00, 8.00, 6.00, 4.00; Jumlah = 28.00 | Sesuai |
| 1.5, 0.5, 3 | Suku 1.5, 2.0, 2.5; jumlah 6.0 | Suku 1.50, 2.00, 2.50; Jumlah = 6.00 | Sesuai |
| 1, 1, n = 0, -2, lalu 3 (uji validasi) | 0 dan -2 ditolak, lalu 3 suku dengan jumlah 6 | Dua pesan penolakan, lalu suku 1.00, 2.00, 3.00; Jumlah = 6.00 | Sesuai |
| 7, 4, 1 (uji batas bawah) | Satu suku: 7; jumlah 7 | Suku ke-1: 7.00; Jumlah = 7.00 | Sesuai |

Catatan: format keluaran memakai dua angka di belakang koma sesuai spesifikasi, sehingga jumlah 6.0 tampil sebagai 6.00.

## Refleksi

Dalam mengerjakan tugas Pertemuan 5, saya masih agak bingung menggunakan if, while, dan beberapa perintah pemrograman lainnya. Karena itu, saya masih dibantu AI yang disini saya menggunakan Claude untuk memahami alur dan menyusun kode.

## Sumber dan Bantuan

- Bahan ajar Pertemuan 05 Algoritma dan Pemrograman (Dr. Aan Hendrayana, S.Si., M.Pd.), Program Studi S1 Pendidikan Matematika FKIP Untirta.
- Dokumentasi Python 3: Control Flow Tools.
- Bantuan AI (Claude) digunakan untuk menyusun draf kode latihan, kode Kuis 2, dan kerangka README ini. Seluruh kode sudah dijalankan dan dipahami sebelum dikumpulkan. 
