import string, random, time

letters = string.ascii_letters + " "

result = ""

target = "Natalie Rosemarie"

for letter in target:
    while True:
        l = random.choice(letters)
        print(result + l)
        if (l == letter):
            result += l
            break
        time.sleep(0.001)