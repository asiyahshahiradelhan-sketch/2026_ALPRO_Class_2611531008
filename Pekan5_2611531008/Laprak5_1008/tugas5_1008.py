# File : tugas5_1008.py

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

N_1008 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Menghitung lebar border
lebar_1008 = (4 * N_1008) + 5

# Border atas
print("#", end="")
for i_1008 in range(lebar_1008):
    print("=", end="")
print("#")

# Fase 1 : Jam Pasir Atas (N turun sampai 1)
for baris_1008 in range(N_1008, 0, -1):

    print("|", end=" ")

    # Spasi kiri
    for spasi_1008 in range(2 * (N_1008 - baris_1008)):
        print(" ", end="")

    # Angka menurun
    for angka_1008 in range(baris_1008, 0, -1):
        print(angka_1008, end=" ")

    # Kristal tengah
    print("<*>", end=" ")

    # Angka menaik
    for angka_1008 in range(1, baris_1008 + 1):
        print(angka_1008, end=" ")

    # Spasi kanan
    for spasi_1008 in range(2 * (N_1008 - baris_1008)):
        print(" ", end="")

    print("|")

# Fase 2 : Titik Pusat Jam Pasir
print("|", end=" ")

for spasi_1008 in range(2 * N_1008):
    print(" ", end="")

print("<*>", end="")

for spasi_1008 in range(2 * N_1008):
    print(" ", end="")

print(" |")

# Fase 3 : Jam Pasir Bawah (1 naik sampai N)
for baris_1008 in range(1, N_1008 + 1):

    print("|", end=" ")

    # Spasi kiri
    for spasi_1008 in range(2 * (N_1008 - baris_1008)):
        print(" ", end="")

    # Angka menurun
    for angka_1008 in range(baris_1008, 0, -1):
        print(angka_1008, end=" ")

    # Kristal tengah
    print("<*>", end=" ")

    # Angka menaik
    for angka_1008 in range(1, baris_1008 + 1):
        print(angka_1008, end=" ")

    # Spasi kanan
    for spasi_1008 in range(2 * (N_1008 - baris_1008)):
        print(" ", end="")

    print("|")

# Border bawah
print("#", end="")
for i_1008 in range(lebar_1008):
    print("=", end="")
print("#")