# Groups
import re
phone = "415-555-1234"
search = re.search(r"(\d{3})-(\d{3}-\d{4})", phone)

print(search.group())
print(search.group(0))
print(search.group(1))
print(search.group(2))

print("----------------------------------")
date = "27-05-2021"
search = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)

day = search.group(1)
month = search.group(2)
year = search.group(3)
print(f"the day is: {day}, the month is: {month}, the year is: {year}")

day, month, year = search.groups()
print(f"the day is: {day}, the month is: {month}, the year is: {year}")

