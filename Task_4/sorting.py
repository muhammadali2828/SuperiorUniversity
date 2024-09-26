#using bubbnle sort
list1 = []

limit = int(input("Enter Limit: "))

for i in range(limit - len(list1)):
    e = input("Enter word: ")  
    list1.append(e)
    print("Updated list: ", list1)

for j in range(len(list1) - 1):
    for k in range(len(list1) - 1):
        if list1[k] > list1[k+1]:
            list1[k], list1[k+1] = list1[k+1], list1[k]
            print("Updated list:", list1)

print("sorted list:", list1)
