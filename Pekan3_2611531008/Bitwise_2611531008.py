# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1008
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_1008 = int(input("Masukkan angka bitwise-1: "))
angka2_1008 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_1008,"| biner =",bin(angka1_1008))
print("angka1 =",angka2_1008,"| biner =",bin(angka2_1008))

# Bitwise AND
hasil_1008 = angka1_1008 & angka2_1008
print("\nBitwise AND (&)")
print(angka1_1008,"&",angka2_1008,hasil_1008)
print("Biner hasil =",bin(hasil_1008))
print("Biner hasil (8 bit) =",format(hasil_1008,"08b"))

# Bitwise OR
hasil_1008 = angka1_1008 | angka2_1008
print("\nBitwise OR (|)")
print(angka1_1008,"|",angka2_1008,hasil_1008)
print("Biner hasil =",bin(hasil_1008))
print("Biner hasil (8 bit) =",format(hasil_1008,"08b"))

# Bitwise XOR
hasil_1008 = angka1_1008 ^ angka2_1008
print("\nBitwise XOR (^)")
print(angka1_1008,"^",angka2_1008,hasil_1008)
print("Biner hasil =",bin(hasil_1008))
print("Biner hasil (8 bit) =",format(hasil_1008,"08b"))

# Bitwise NOT
hasil_1008 = ~angka1_1008
print("\nBitwise NOT (~)")
print(angka1_1008,"~",angka2_1008,hasil_1008)
print("Biner hasil =",bin(hasil_1008))
print("Biner hasil (8 bit) =",format(hasil_1008,"08b"))

# Bitwise geser kiri
jumlah_geser_1008 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1008 = angka1_1008 << jumlah_geser_1008
print("\nBitwise geser kiri (<<)")
print(angka1_1008,"<<",jumlah_geser_1008,"=",hasil_1008)
print("Biner hasil =",bin(hasil_1008))
print("Biner hasil (8 bit) =",format(hasil_1008,"08b"))

# Bitwise geser kanan
hasil_1008 = angka1_1008 >> jumlah_geser_1008
print("\nBitwise geser kanan (>>)")
print(angka1_1008,">>",jumlah_geser_1008,"=",hasil_1008)
print("Biner hasil =",bin(hasil_1008))
print("Biner hasil (8 bit) =",format(hasil_1008,"08b"))