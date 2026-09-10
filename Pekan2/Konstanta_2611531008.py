# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1008

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_1008 = float(input('Masukkan nilai jari-jari: '))
luas_1008 = PI * jari_1008 * jari_1008
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1008, luas_1008))