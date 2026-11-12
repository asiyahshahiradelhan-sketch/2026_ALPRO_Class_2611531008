# Name: <Asiyah Shahira Delhan>
# NIM: 2611531008
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())


full_name = " Siti Aisyah "
nim = "2610511023"

# Hapus spasi di awal dan akhir
clean = full_name.strip()

# Cari posisi spasi pertama
space = clean.find(" ")

# Ambil nama depan saja lalu ubah ke huruf kecil
if space == -1:
  first_name = clean.lower()
else:
  first_name = clean[:space].lower()

# Gabungkan nama depan dengan 3 digit terakhir NIM
username = first_name + nim[-3:]

print(username)