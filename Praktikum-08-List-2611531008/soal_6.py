LAST_DIGIT = 8
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for i in range(7):
    angka = int(input("Day " + str(i + 1) + ": "))
    expenses.append(angka)

total = 0

for i in range(7):
    total = total + expenses[i]

average = total / 7

highest = expenses[0]
hari = 1
jumlah = 0

for i in range(7):
    if expenses[i] > highest:
        highest = expenses[i]
        hari = i + 1

    if expenses[i] > daily_limit:
        jumlah = jumlah + 1

print("Daily limit:", daily_limit)
print("Total:", total)
print("Average: {:.1f}".format(average))
print("Highest: day", hari, "(" + str(highest) + ")")
print("Days above limit:", jumlah)