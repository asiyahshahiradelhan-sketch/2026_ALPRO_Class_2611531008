# Buat file dengan nama Boolean_NIM.py
# Nama variable ditambah 4  digit nim terakhir contoh: nilai_1008
# Deklarasi variable dengan tipe data Boolean
is_lulus_1008 = True
is_cumlaude_1008 = True

# Menggunakan Boolean
nilai = 85
batas_lulus = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai >= batas_lulus # Hasilnya akan True

print("=== Check kelulusan ===")
print("Nilai:", nilai)
print("Apakah Lulus?:", status_kelulusan)
if is_lulus_1008 and is_cumlaude_1008:
    print("Selamat anda lulus dengan prediket Cum Laude!")