import math
c_meters_per_sec = 299792458

mass_kg = float(input("Enter the mass kg: "))

energy_per_joules = mass_kg * (c_meters_per_sec ** 2)

print("Energy per joules: ", f'{energy_per_joules:.5f}')


print(f'{math.pi:.110}')