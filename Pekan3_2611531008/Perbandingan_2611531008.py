# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah dengan 4 digit nim terakhir contoh: angka1_1008
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_1008 = int(input("Input angka-1: "))
angka2_1008 = int(input("Input angka-2: "))

# Lebih besar dari
hasil = angka1_1008 > angka2_1008
print("\nOperator lebih besar dari")
print("angka1_1008 > angka2_1008 =", hasil)

# Lebih kecil dari
hasil = angka1_1008 < angka2_1008
print("\nOperator lebih kecil dari")
print("angka1_1008 < angka2_1008 =", hasil)

# lebih besar dari atau sama dengan
hasil = angka1_1008 >= angka2_1008
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_1008 >= angka2_1008 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_1008 <= angka2_1008
print("\nOperator Lebih kecil dari atau sama dengan")
print("angka1_1008 <= angka2_1008 =", hasil)

# Sama dengan
hasil = angka1_1008 == angka2_1008
print("\nOperator Sama dengan")
print("angka1_1008 == angka2_1008 =", hasil)

# Tidak sama dengan
hasil = angka1_1008 != angka2_1008
print("\nOperator Tidak sama dengan")
print("angka1_1008 != angka2_1008 =", hasil)

# Tambahan perbandingan berantai dalam Python
hasil = 0 < angka1_1008 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil)

hasil = 0 < angka2_1008 < 100
print("0 < angka2 < 100 =", hasil)