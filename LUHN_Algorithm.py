
list1 = [1,3,3,0,1,1,3,4,9,3,1,8,3,1,5,7]
limit = 16
#for i in range (limit - len(list1)):
    #e = int(input("Enter value: "))
    #list1.append(e)
print("\nAccount Number: ",list1)
x= list1.pop()

list1.reverse()
print("reverse:", list1)
for i,j in enumerate(list1):
    if i % 2 == 0:
        list1[i] = j*2
print("Double Values on Even:", list1)
for i,j in enumerate(list1):       
    if j > 9:
        list1[i] = j- 9
print("Minus by 9:", list1)
sum= 0
for i,j in enumerate(list1):
    sum += j
sum = sum + j
print("SUM: ",sum)
if sum % 10 == 0:
    print(f"The account number is valid")
else:
    print(f"The account number is invalid")