import json

with open("json_data.json") as json_file:
    json_data = json.load(json_file)

userId = int(input("Enter your id: ")) - 1

if int(json_data[userId]["id"]) - 1 == userId:
    print(json_data[userId]["id"])
    print(json_data[userId]["first_name"])
    print(json_data[userId]["last_name"])
    print(json_data[userId]["email"])
    print(json_data[userId]["gender"])
else:
    print("User not found")

count = 0
for i in range(len(json_data)):
    if json_data[i]["gender"] == "Male":
        count += 1

print("\nData Summary ..........................................\n")
print("Number of Females: \t" + str(len(json_data) - count))
print("Number of Males: \t" + str(count))