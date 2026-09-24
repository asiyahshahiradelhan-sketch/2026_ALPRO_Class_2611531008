# Buat file dengan nama if2_nim.py
# Buat program untuk kondisional if
# Buat nama variabel ditambah 4 digit terakhir contoh: ipk_1008
# Program ini menggunakan fungsi input()

ipk_1008 = float(input("Input IPK anda"))

if ipk_1008 > 2.75:
    print("Anda Lulus Sangat memuaskan dengan IPK " + str(ipk_1008))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")