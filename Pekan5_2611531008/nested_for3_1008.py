# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1008
# Program ini menggunakan fungsi input()

batas_1008 = int(input("Masukkan nilai batas: "))
for i_1008 in range(batas_1008 + 1):
    for j_1008 in range(batas_1008 + 1):
        print(i_1008 + j_1008, end=" ")
    print() # pindah ke baris berikutnya