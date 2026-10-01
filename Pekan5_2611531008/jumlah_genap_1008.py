# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk menghitung jumlah bilangan genap dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1008
# Program ini menggunakan fungsi input()


ulang_1008 = int(input("Masukkan nilai batas: "))

jumlah_genap_1008 = 0
for i_1008 in range(1, ulang_1008 + 1):
    if i_1008 % 2 == 0:
        print(i_1008, end=" ")
        jumlah_genap_1008 = jumlah_genap_1008 + i_1008

        if i_1008 < ulang_1008:
            print(" + ", end="")
        else:
            print(" = ", jumlah_genap_1008, end="")
print()
print("Jumlah =", jumlah_genap_1008)