import re

# sub
string = """Hello my Number is 415-555-1011 and 
             my friend's number is 658-984-2165"""

replace = re.sub(r"\d{3}-\d{3}-\d{4}", "415 555 1011", string, 1)

print(replace)

print("--------------------------------------------")

txt = "I am a student at Hsoub Academy"
replace = re.sub(r"Hsoub Academy", "Hsoub-Academy", txt)
print(replace)

print("--------------------------------------------")
#split
txt = "I am a student at Hsoub Academy"
search = re.split(r"\s", txt)
print(search)

search = re.split(r"\s", txt, 4)
print(search)

print("--------------------------------------------")
#practice
test = "استئناف-رفع-الملفات-بعد-فقدان-الاتصال-في-جافاسكربت"

search_one = re.sub("-", " ", test)
print(search_one)

print("--------------------------------------------")

search_two = re.split(r"-", test)
print(search_two)
print(" ".join(search_two))





