# Name: <Asiyah Shahira Delhan>
# NIM: <2611531008>
# Question 7

name = "asiyah shahira delhan"
nim = "2611531008"
username = "asiyah008"

intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)