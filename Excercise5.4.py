cities = []

for _ in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("Names of cities you entered:")
for city in cities:
    print(city)