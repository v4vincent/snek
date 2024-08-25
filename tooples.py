from collections import namedtuple

Friends = namedtuple("Friends",["Name", "Age", "Location"])

friend1 = Friends("Vincent Vermillion", 30, "Tacoma, Washington")

print(friend1)