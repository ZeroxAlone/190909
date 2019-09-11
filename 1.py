

#1
print("Ounces Grams")
for i in range(1,31):
    Grams = round(i*28.35)
    print(i, Grams)

#2
ucl = 0
dig = 0
UserID = input("Please input the user ID: ")
for i in UserID:
    if 65<=ord(i)<=90:
        ucl+=1
    elif 48<=ord(i)<=57:
        dig+=1
    else:
        continue
if len(UserID)!=7 or ucl!=3 or dig!=4:
    print("Invalid user ID")
else:
    print("Valid user ID")

#3a
Tally = [0 for i in range(5)]
#b
Choice = int(input("Please input the number: "))
while Choice != 0:
    Tally[Choice]+=1
for i in Tally:
    print(i)
#c
Choice = int(input("Please input the number: "))
while Choice != 0:
    Tally[Choice]+=1
Tally = Tally*2
Tally[0] = "Reading books"
Tally[2] = "Play computer games"
Tally[4] = "Sport"
Tally[6] = "Programming"
Tally[8] = "Watching TV"

for i in Tally:
    print(i)

#d
file = open("array1.txt","w")
Choice = int(input("Please input the number: "))
while Choice != 0:
    Tally[Choice]+=1
for i in Tally:
    file.write(i)
file.close()

#e
file = open("array1.txt","w")
Choice = int(input("Please input the number: "))
while Choice != 0:
    Tally[Choice]+=1
for i in range(len(Tally)):
    Tally[i] = 0
    file.write(Tally[i])
file.close()
