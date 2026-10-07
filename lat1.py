# Ini komentar, tidak dijalankan
print("Halo, Dunia")

nama= "Python"
if nama== "Python":
    print("indentasin= blok kode")
    print("gunakan 4 spasi")

# BAB 2 VARIABEL & TIPE DATA
# Variabel: wadah penyimpanan nilai
nama = "budi"       #str
umur = 20           #int
tinggi = 170.5      #float
aktif = True        #bool

#nilai bisa di ganti kapan saja
umur = umur + 1

#multipe assignment
x, y, z =1, 2, 3
print(nama, umur, x + y + z )

#konversi tipe data
angka = int("25")
print(angka + 5)
harga = float("12500.75")
print(type(harga))

umur = 20
print("umur: " + str(umur))
print(bool(0), bool("hai"))

#bekerja dengan string
nama = "python dasar"
print(len(nama))
print(nama.upper())
print(nama[0:6])
print(nama.split(" "))

bab = 2
print(f"belajar {nama} bab {bab}")

#BAB 3 INPUT & OUTPUT
#Menampilkan output  dengan print()

print("halo", "dunia")
print("A", "B", "C", sep="-")
print("loading", end="...")
print("selesai")

harga = 15000 / 7
print(f"harga: rp{harga:.2f}")
print(f"total: {1500000:,}")


nama = input("siapa namamu? ")
umur = int(input("berapa umurmu? "))

tahun_depan = umur + 1
print(f"Halo {nama}!")
print(f"Tahun depan kamu {tahun_depan} tahun")

#BAB 4 OPERATOR
#Operator perbandingan
umur = 20
punya_ktp = True

print(umur >=20 and punya_ktp)
print(umur <22 or umur > 30)
print(not punya_ktp)

#operator penugasan & keanggotaan
skor =10
skor+= 5        #skor = skor +5
skor*= 2        #skor = skor *2
print(skor)

buah = ["apel", "jeruk", "mangga"]
print("apel" in buah)
print("anggur" not in buah)
print("th" in "python")

#BAB 5 PERCABANGAN
#if &velse: mengambil keputusan
nilai = 80

if nilai >= 75:
    print("selamat, kamu lulus!")
else:
    print("ayo remedial dulu")
print("program selesai")

 #if-elif: banyak kondisi
nilai = 78

if nilai >= 85:
   grade = "A"
elif nilai >= 70:
   grade = "B"
elif nilai >= 55:
   grade = "c"
else: 
   grade = "D"

print(f"nilai {nilai}  → grade {grade}")

#nested if, ternary & match-case
umur, ktp = 20, True
if umur >=17:
   if ktp:
      print("boleh memilih")
   else:
      print("buat ktp dulu")

umur = 16
s = "dewasa" if umur>= 17 else "anak"
print(s)        #anak

hari = "sabtu"

match hari:
    case "sabtu"| "minggu":
      print("libur!")
    case "senin":
      print("semangat!")
    case  _:
        print("hari kerja")

#BAB 6 PERULANGAN
#for: mengulang setiap item
for i in range(1,4):
    print(f"putaran ke-{i}")

buah = ["apel", "jeruk", "mangga"]
for b in buah:
   print(b.upper())

hitung = 3

while hitung > 0:
   print(f"hitung mundur: {hitung}")
   hitung -= 1

   print("meluncur")

for n in range(1, 10):
   if n == 3:
      continue      #lewat 3
   if n == 6:
      break         #berhenti di 6
   print(n)
for i in range(3):
   pass             #todo: isi nanti

#BAB 7 TUPLE, SET & DICTIONARY
#List: koleksi serbaguna
nilai = [80, 65, 90]
nilai.append(75)
nilai.remove(65)
nilai[0] = 85

print(nilai)
print(nilai[-1], len(nilai))
print(sorted(nilai))

titik = [3, 7]
warna = (255, 128, 0)

x, y = titik         #unpacking
print(f"x={x}, y={y}")
print(warna[0], len(warna))

titik[0] = 10        #typeeorror!

angka = {1, 2, 2, 3, 3, 3}
print(angka)

ipa = {"ani", "budi", "citra"}
ips = {"budi", "dodi"}

print(ipa | ips)
print(ipa & ips)
print(ipa - ips)

siswa = {"nama ": "sari", "umur": 19}
siswa["kota"] = "bandung"
siswa["umur"] = 20
print(siswa["nama "])
print(siswa.get("hobi", "_"))

for k, v in siswa.items():
   print(f"{k}: {v}")

#BAB 8 FUNCTION
#anatomi sebuah function
def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    luas = panjang * lebar
    return luas

hasil = hitung_luas(5, 3)
print(hasil)
print(hitung_luas(10, 2))

def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))

def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))

kuadrat = lambda x: x ** 2
print(kuadrat(4))  # 16

siswa = [("Ani", 80), ("Budi", 95)]
print(max(siswa, key=lambda s: s[1]))


x = "global"

def tes():
    x = "lokal"     # hanya di dalam tes()
    print(x)        # lokal

tes()
print(x)            # global

#BAB 9 EROR HADLING
#TRY-EXCEPT-ELS-FINALILLY
try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
else:
    print(f"Hasil: {hasil}")
finally:
    print("Selesai.")

#RAISE: MEMUNCULKAN EROR SENDIRI
def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak valid")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"Error: {e}")

#BAB 10 MODULE & PACKAGE
#MENGGUNAKAN MODULE
import math
from random import randint
import datetime as dt

print(math.sqrt(16))
print(math.pi)
print(randint(1, 6))
print(dt.date.today().year)

#MEMBUAT MODULE & PACKAGE SENDIRI
# Tulis fungsi rata_rata langsung di file ini
def rata_rata(data):
    return sum(data) / len(data)

# Langsung panggil fungsinya tanpa import
nilai = [80, 90, 70]
print(rata_rata(nilai))

#BAB 11 PENGOLAHAN DATA SEDERHANA
import csv

data = []
with open(r"C:\Laragon\python_dasar\nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")
print(data[0])\

# Asumsi 'data' didapat dari proses baca_data.py sebelumnya

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")

import pandas as pd

df = pd.read_csv("nilai.csv")

# Rekap rata-rata per kelas
print(df.groupby("kelas")["nilai"].mean())

# Filter nama yang nilainya >= 75
print(df[df["nilai"] >= 75]["nama"].tolist())

# Ambil data siswa dengan nilai tertinggi
print(df.sort_values("nilai").tail(1))