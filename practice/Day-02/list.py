fruits = ["apple", "banana", "cherry"]
fruits.append("orange") #add orange to the list
fruits.insert(1, "kiwi") #add kiwi to the second position
fruits.remove("banana") #remove banana from the list
last_fruit = fruits.pop() #remove the last item from the list
fruits.sort() #sort the list in ascending order

print(fruits) #print the modified list
print(fruits[0])
print(fruits[1])
print(fruits[1:3]) #print the second and third items in the list
print(len(fruits)) #print the number of items in the list
print(fruits.index("kiwi")) #print the index of kiwi in the list