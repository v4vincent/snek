my_string = "Natalie"

if ('N' and 'a' in my_string) and 'B' not in my_string:
    print("True")
else:
    print("False")

family_list = ["Vincent", "Nicole", "Natalie"]
family_list_cap = [i.capitalize() for i in family_list]

name = input("What's your name? ").capitalize()

if name in family_list_cap:
    print(f"Yep, {name}, you're a Vermillion")
else:
    print(f'{name}? Never heard of you.')

dict1 = {
    1: "Vincent",
    2: "Nicole",
    3: "Natalie"
}

if 1 in dict1:
    print("It's in da bag")