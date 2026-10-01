# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1008
# Program ini menggunakan fungsi input()

tinggi_1008 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1008 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1008 = tinggi_1008
    c_1008 = a_1008
    lebar_1008 = (2 * tinggi_1008 + 1)

    for i_1008 in range(1, tinggi_1008 + 1):
        b_1008 = c_1008 + 1

        for j_1008 in range(1, lebar_1008 + 1):

            
            # Baris atas dan bawah
            if i_1008 == 1 or i_1008 == tinggi_1008:
                if j_1008 == 1 or j_1008 == lebar_1008:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_1008 == 1 or j_1008 == lebar_1008:
                    print("|", end="")
                else:
                    if j_1008 == c_1008:
                        print("<", end="")
                    elif j_1008 == b_1008:
                        print(">", end="")
                    elif j_1008 == (lebar_1008 - c_1008):
                        print("<", end="")
                    elif j_1008 == (lebar_1008  - c_1008 + 1):
                        print(">", end="")
                    elif j_1008 > b_1008 and j_1008 < (lebar_1008 - c_1008):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_1008 -= 2

        if a_1008 <= 0:
            c_1008 = (-a_1008) + 2
        else:
            c_1008 = a_1008