
exp = [2503, 5602, 4563, 2468, 8570, 6490, 4785]

total = 0

for item in exp:
    total = total + item

print(total)

for i in range(1, 11):
    print(i**2)


for i in range(len(exp)):
    print("Month: ", (i+1), "Expense: ", exp[i])
    total = total + exp[i]

print('Total expense is: ', total)

key_location = 'chair'

locations = ['garage', 'living room', 'chair', 'closet']
for i in locations:
    if i == key_location:
        print('key is found in ', i)
        break
    else:
        print('key is not found in ', i)

    