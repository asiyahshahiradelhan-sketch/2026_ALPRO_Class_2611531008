# Name: <Asiyah Shahira Delhan>
# NIM: 2611531008
# Question 5

username = input("username: ")
 
# Check the rules in a safe order and print the first rule that fails.
if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

# B
nim = input("NIM: ")

if len(nim) == 10 and nim.isdigit():
    tahun = nim[:2]
    print(f"Valid: year 20{tahun}")
else:
    print("Invalid NIM")