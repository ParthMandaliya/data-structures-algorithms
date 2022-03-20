from HashTable import HashTable

data = []
with open("./nyc_weather.csv", "r") as f:
    for line in f.readlines():
        data.append(line.strip().split(","))

obj = HashTable()

for key, value in data:
    obj[key] = value
    # obj.add(key, value)

week1 = []
for day in range(8):
    day_ = f"Jan {day}"
    temp = obj[day_]
    if temp != None:
        week1.append(int(temp))

print ("Average temprature of Jan first week:", sum(week1)/len(week1))
print ("January week 1 maximum temprature:", max(week1))

print ("Temprature on January 9:", obj["Jan 9"])
print ("Temprature on January 4:", obj["Jan 4"])