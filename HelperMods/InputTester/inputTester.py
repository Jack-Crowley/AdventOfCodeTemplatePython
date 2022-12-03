# Make sure the session ID is gathering the correct input
# Make sure to delete the extra line in generated input

with open("./HelperMods/InputTester/a.txt") as data1: data1 = [i.strip() for i in data1]
with open("./HelperMods/InputTester/b.txt") as data2: data2 = [i.strip() for i in data2]

a=0
for i in range(len(data1)):
    if (data1[i]==data2[i]):
        a+=1
print(f"{a}/{len(data1)} Correct")