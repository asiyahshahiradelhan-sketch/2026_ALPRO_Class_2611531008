# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka_1008
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_1008 = int(input("Input angka-1: "))
angka2_1008 = int(input("Input angka-2: "))

print("\nNilai awal angka =", angka1_1008)
print("\nNilai awal angka =", angka2_1008)

# Assigment biasa
hasil = angka1_1008
print("\nAssigment biasa (=)")
print("Hasil =", hasil)

# Assigment penambahan
hasil = angka1_1008
hasil += angka2_1008
print("\nAssigment penambahan (+=)")
print("Hasil =", hasil)

# Assigment pengurangan
hasil = angka1_1008
hasil -= angka2_1008
print("\nAssigment pengurangan (-=)")
print("Hasil =", hasil)

# Assigment perkalian
hasil = angka1_1008
hasil *= angka2_1008
print("\nAssigment perkalian (*=)")
print("Hasil =", hasil)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_1008 != 0:
    hasil = angka1_1008
    hasil /= angka2_1008
    print("\nAssigment pembagian bulat (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_1008
    hasil //= angka2_1008
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_1008
    hasil %= angka2_1008
    print("\nAssigment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan ")
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assigment perpangkatan
hasil = angka1_1008
hasil **= angka2_1008
print("\nAssigment perpangkatan (**=)")
print("Hasil =", hasil)