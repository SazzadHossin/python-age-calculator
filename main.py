from datetime import date

name = input("Please enter your name: ")
birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

# Today's date
today = date.today()
birth_date = date(birth_year, birth_month, birth_day)

# Calculate age in years
age_years = today.year - birth_year
if (today.month, today.day) < (birth_month, birth_day):
    age_years -= 1

# Calculate total days lived
total_days = (today - birth_date).days

# Calculate days after last birthday
last_birthday = date(today.year, birth_month, birth_day)
if today < last_birthday:
    last_birthday = date(today.year - 1, birth_month, birth_day)

extra_days = (today - last_birthday).days

print("\n" + "="*40)
print(f" Age Details for {name}")
print("="*40)
print(f" {name} is {age_years} years and {extra_days} days old.")
print(f" Total days lived: {total_days} days")
print("="*40)