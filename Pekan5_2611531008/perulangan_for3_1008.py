# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1008
# Program ini menggunakan fungsi input()

ulang_1008 = int(input("Masukkan jumlah perulangan: "))

jumlah_1008 = 0
for i_1008 in range(1, ulang_1008 + 1):
    print(i_1008, end= " ")
    jumlah_1008 = jumlah_1008 + i_1008

    if i_1008 < ulang_1008:
        print("+", end=" ")
    else:
        print("=", jumlah_1008, end=" ")
print()
print("jumlah =", jumlah_1008)