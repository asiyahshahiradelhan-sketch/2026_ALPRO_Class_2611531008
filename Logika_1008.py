# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1008
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Masukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1008 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_1008 = input("Input nilai boolean-2 (ture/false): ").strip().lower() == "true"

print("\nA1 =", a1_1008)
print("\nA2 =", a2_1008)

# Konjugsi: bernilai True jika keduanya True
hasil = a1_1008 and a2_1008
print("\nKonjugsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1_1008 or a2_1008
print("\nDisjungsi (OR)")
print("not A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_1008
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_1008
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1_1008 != a2_1008
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)