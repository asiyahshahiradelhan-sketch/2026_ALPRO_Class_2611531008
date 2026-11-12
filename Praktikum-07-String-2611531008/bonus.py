# <Asiyah Shahira Delhan>
# NIM: <2611531008>
# Bonus

kalimat = input("Masukkan kalimat: ")

teks_bersih = kalimat.replace(" ", "").lower()

if teks_bersih == teks_bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")