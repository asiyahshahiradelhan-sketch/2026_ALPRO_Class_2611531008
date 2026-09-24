# Buat file dengan nama multi_if_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit terakhir contok: ipk_1008
# Programi ini menggunakan fungsi input()

umur_1008 = int(input("Input umur anda: "))
sim_1008 = input("Apakah Anda Sudah Punya Sim C (y/t): ")

if umur_1008 >= 17 and sim_1008 == 'y':
    print("Anda Sudah Dewasa dan boleh bawa motor")

if umur_1008 >= 17 and sim_1008 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_1008 < 17 and sim_1008 == 'y':
    print("Anda Belum Cukup umur punya SIM")

if umur_1008 < 17 and sim_1008 != 'y':
    print("Anda Belum cukup umur bawa motor")