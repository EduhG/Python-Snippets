import json

with open("data.json") as json_file:
    json_data = json.load(json_file)

userId = int(input("Enter your id: ")) - 1

if int(json_data[userId]["id"]) - 1 == userId:
    print(
        "User ID:\t" + str(json_data[userId]["id"]) + "\n" +
        "First Name:\t" + json_data[userId]["first_name"] + "\n" +
        "Last Name:\t" + json_data[userId]["last_name"] + "\n" +
        "Email:\t\t" + json_data[userId]["email"] + "\n" +
        "Gender:\t\t" + json_data[userId]["gender"])

else:
    print("User not found")

count = 0
for i in range(len(json_data)):
    if json_data[i]["gender"] == "Male":
        count += 1

print("\nData Summary ..........................................")
print("\tNumber of Females: \t" + str(len(json_data) - count))
print("\tNumber of Males: \t" + str(count))