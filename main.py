country_capital = {
    "Slovakia": "Bratislava",
    "Austria" : "Vienna",
    "Hungary" : "Budapest",
    "Czech Republic" : "Brno"
}
print(country_capital.items())
print(country_capital.keys())
print(country_capital.values())

country_capital["Italy"] = "Rome"
country_capital["France"] = "Paris"

print("Country Capitals Dictionary:")
for country, capital in country_capital.items():
    print(f"{country}: {capital}")

delete_country = "France"
if delete_country in country_capital:
    del country_capital[delete_country]
    print(f"Deleted {delete_country} from the dictionary.")
else:
    print(f"{delete_country} not found in the dictionary.")

# state = "Czech Republic"
# new_capital = country_capital.get(state, "Capital")
# country_capital["Czech Republic"] = "Praha"
# print("")
#
import json

# Save to a file
with open('capitals.json', 'w') as file:
    json.dump(country_capital, file)

# Load from the file
with open('capitals.json', 'r') as file:
    loaded_capitals = json.load(file)

