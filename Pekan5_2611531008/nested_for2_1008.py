# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terkahir contoh: ulang_1008
# Program ini menggunakan fungsi input()

batas_1008 = int(input("Masukkan nilai batas: "))
for i_1008 in range(1, batas_1008 + 1):
    for j_1008 in range(1, batas_1008 + 1):
        print("*", end=" ")
    print() # pindah ke baris berikutnya