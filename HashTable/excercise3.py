data = []
with open("./poem.txt", "r") as f:
    for line in f.readlines():
        temp = line.strip()
        if temp != "":
            data.append(temp)

from HashTable import HashTable

obj = HashTable()
for line in data:
    line = line.split()
    for word in line:
        if word in obj:
            obj[word] += 1
            continue
        obj[word] = 1

print ("diverged:", obj["diverged"])
print ("in:", obj["in"])
print ("I:", obj["I"])