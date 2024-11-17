print("Mass of Ages")

x = 10
y = 20
def boolean():
    if not x or y < 20:
        print("less than 20")
    else:
        print("Not working")


boolean()

def channel(chan):
    if chan >= 1 and chan < 50:
        print("basic cable")
    elif chan == 50 or chan > 51:
        print("dish cable")
    else:
        print("streamin'")

channel(-2)

user_age = 18
if user_age >= 18 and user_age <= 25:
    print('Eligible')
else:
    print('Ineligible')