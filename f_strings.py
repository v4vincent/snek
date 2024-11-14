wife = "Nicole"
husband = "Vincent"
daughter = "Natalie"
wife_age = 25
husband_age = 30
daughter_age = 2/12

def string_manipulation(p1,p2,p3):
    print(f"{p1} is the wife.")
    print(f"{p2} is the husband.")
    print(f"{p3} is their daughter.")

string_manipulation(wife,husband,daughter)

def f_strings(string):
    if isinstance(string, str):
        print(f"{string:s}")
    elif isinstance(string, int):
        print(f"{string:.2f}")


f_strings(1)
f_strings("Vincent")

phone_number = 5052596330
print(f"({phone_number // 10000000}) {int((phone_number % 10000000)/10000)}-{phone_number % 10000}")