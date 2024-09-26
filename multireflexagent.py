class DynamicArray:
    def __init__(self):
        self.array = []
    
    def append(self, value):
        self.array.append(value)      
    
    def insert(self, index, value):
        if 0 <= index <= len(self.array):
            self.array.insert(index, value)
        else:
            print("Index out of bounds.")
    
    def remove(self, value):
        if value in self.array:
            self.array.remove(value)
        else:
            print("Value not found in the array.")
    
    def display(self):
        print("Current array contents:")
        for item in self.array:    
            print(item)


def menu():
    array = DynamicArray()

    def agent1():
        value = input("Enter the value to append:")
        array.append(value)
    def agent2():
        index = int(input("Enter the index to insert: "))
        value = input("Enter the value to insert: ")
        array.insert(index, value)
    def agent3():
        value = input("Enter the value toremove: ")
        array.remove(value)
    def agent4():
        array.display()

    while True:
        print("\nDynamic Array Menu:")
        print("1. Apend value ")
        print("2. Insert value ")
        print("3. Remove value ")
        print("4. Display arry")
        print("5.quit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            agent1()
        elif choice == '2':
            agent2()
        elif choice == '3':
            agent3()
        elif choice == '4':
            agent4()
        elif choice == '5':
            print("Quiting Program....")
            break
        else:
            print("Invalid choice..")

menu()
