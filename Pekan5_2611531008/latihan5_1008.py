# Program perulangan for untuk membuat segitiga

tinggi_1008 = int(input("Masukkan tinggi segitiga: "))
for i_1008 in range(1, tinggi_1008 + 1):
    for j_1008 in range(1, tinggi_1008 - i_1008 + 1):
        print(" ", end="")
    for k_1008 in range(1, 2 * i_1008):
        print("*", end="")
    print()