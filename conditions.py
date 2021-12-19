age = 70
ismale = True
Is_Superman = True

# ==, >, >=, <, <=, !=
if ((age >= 18 and age < 30) and ismale) or Is_Superman:
    print("Serve army")
elif (age >= 30 and age < 60) and ismale:
    print("Work")
elif (age >= 60) and ismale:
    print("Retire")
else:
    print("Study")