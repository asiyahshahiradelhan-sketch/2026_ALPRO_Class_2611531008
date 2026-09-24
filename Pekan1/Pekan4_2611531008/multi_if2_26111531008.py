# Buat file dengan nama multi_if2_nim.py
# buat program untuk kondisional if
# Nama Variabel ditambah 4 digit terakhir contoh: ipk_1008
# Programi ini menggunakan fungsi input()
# Program menghitung diskon Belanja

# Input dan user
total_belanja_1008 = float(input("Input Total Belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y atau 't')
input_member_1008 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_1008 = input_member_1008 in ["y", "t"]

# Input status kode promo (mengecek apakah user mengetik 'y atau 't')
input_promo_1008 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1008 = input_promo_1008 in ["y", "t"]

total_diskon_persen_1008 = 0

# Multi-if terpisah: Setiap kondisi diperiksa secara independen 
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_1008 > 1000000:
    total_diskon_persen_1008 += 10 # Diskon total besar

if is_member_1008:
    total_diskon_persen_1008 += 5 # Diskon member

if kode_promo_valid_1008:
    total_diskon_persen_1008 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_1008 = total_belanja_1008 * (total_diskon_persen_1008 / 100)
total_bayar_1008 = total_belanja_1008 - nominal_diskon_1008

# Output hasil
print("\n--- Rincian pembayaran ---")
print(f"Total diskon  : {total_diskon_persen_1008} (Rp {nominal_diskon_1008:.0f})")
print(f"Total bayar : Rp {total_bayar_1008:.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_1008}%")
# output : Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid