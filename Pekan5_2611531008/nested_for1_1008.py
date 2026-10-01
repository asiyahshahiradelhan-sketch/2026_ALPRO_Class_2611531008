# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1008
# Program ini menggunakan fungsi input()

batas_1008 = int(input("Masukkan nilai batas: "))
for line_1008 in range(1, batas_1008 + 1):
    for j_1008 in range(1, (-1 * line_1008 + batas_1008) + 1):
        print(".", end="")
    print(line_1008)