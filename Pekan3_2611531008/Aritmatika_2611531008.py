# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhhir contoh: angka1_1008
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1008 = int(input("Input angka-1: "))
angka2_1008 = int(input("Input angka-2:" ))

# Penjumlahan
hasil = angka1_1008 + angka2_1008
print("\nOperator Penjumlahan")
print("Hasil =", hasil)

# Pengurangan
hasil = angka1_1008 - angka2_1008
print("\nOperator Pengurangan")
print("Hasil =", hasil)

# Perkalian
hasil = angka1_1008 * angka2_1008
print("\nOperator Perkalian")
print("Hasil =", hasil)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1008 != 0:
    hasil = angka1_1008 / angka2_1008
    print("\nOperator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1_1008 // angka2_1008
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_1008 % angka2_1008
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil = angka1_1008 ** angka2_1008
print("\nOperator Pangkat")
print("Hasil =", hasil)