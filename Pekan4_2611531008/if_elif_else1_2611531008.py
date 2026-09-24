# Buat file dengan nama multi_if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit terakhir contok: ipk_1008
# Programi ini menggunakan fungsi input()

umur_1008 = int(input("Input umur anda: "))
sim_1008 = input("Apakah Anda Sudah Punya Sim C: ")[0]

if umur_1008 >= 17 and sim_1008 == 'y':
    print("Anda Sudah Dewasa dan boleh bawa motor")
elif umur_1008 >=17 and sim_1008 != 'y':
    print("Anda sudah dewasa tetapi tidak bole bawa motor")
elif umur_1008 < 17 and sim_1008 == 'y':
      print("Anda Belum Cukup umur punya SIM")
else:
     print("Anda Belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")