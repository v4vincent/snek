print("Here we go again")

set1 = set([1,"Natalie", True, 1, "natalie"])

set2 = {1,2,3}

for i in set2:
    print(i)

set1.add(2)
print(set1)
set1.pop()
print(set1)

person1_cities = {'Edmonton', 'Vancouver', 'Paris', 'Bangkok', 'Bend', 'Boise', 'Memphis', 'Zurich', 'Accra', 'Cairo'}
person2_cities = {'Accra', 'Orlando', 'Tokyo', 'Paris', 'Anaheim', 'Buenos Aires', 'London', 'Lima', 'Seoul', 'Bangkok'}

# Use set methods to create sets all_cities, same_cities, and different_cities.

all_cities = person1_cities.union(person2_cities)
same_cities = person1_cities.intersection(person2_cities)
different_cities = person1_cities.symmetric_difference(person2_cities)


print(sorted(all_cities))
print(sorted(same_cities))
print(sorted(different_cities))