#EXERCISE 1
#a list with 5 items (names of people) and a program to output the 2nd item.
names = ["Bahati", "Brenda", "Kizito", "Christian", "Paul"]
print(names[1])

#program to change the value of the first item to a new value
names[0] = "Stella"
print(names[0])
print(names)

#program to add a sixth item to the list
names.append("Latigi")
print(names)

#program to add “Bathel” as the 3rd item in your list
names.insert(2, "Bathel")
print(names)

#program to remove the 4th item from the list
del names[4]
print(names)

#Using negative indexing to print the last item in the list
print(names[-1])

#a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items
food = ["pizza", "burger", "lamb chops", "rabbit pie", "shawarma", "bacon", "steak"]
print(food[2:5])

#a list of countries and making a copy of it.
countries = ["uganda", "kenya", "tanzania", "burundi", "rwanda"]
print(countries)
print(countries.copy())

#program to loop through the list of countries
for x in countries:
    print(x)

#a list of animal names sorted in both descending and ascending order.
animals = ["cat", "dog", "pig", "goat", "cow"]
animals.sort()
print(animals) #ascending
animals.sort(reverse=True)
print(animals) #descending

#program to output only animal names with the letter ‘a’ in them
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print(animals_with_a) 

#two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ['Jane', 'John', 'Jack']
second_names = ['Doe', 'Deer', 'Black']
full_names = [f"{first} {second}" for first, second in zip(first_names, second_names)]
print(full_names) 

#EXERCISE 2
#program to output favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone = x[1]  
print(favorite_phone)

#Using negative indexing to print the 2nd last item in your tuple. 
print(x[-2])

#program to update “iphone” to “itel”
list_x = list(x)
list_x[1] = "itel"
x = tuple(list_x)
print(x) 

#python program to add “Huawei” to your 
list_x = list(x)
list_x.append("Huawei")
x = tuple(list_x)
print(x)

#a python program to loop through the tuple above
for phone in x:
       print(phone)
       
#program to remove/delete the first item in tuple
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print(x) 

#Using the tuple() constructor, create a tuple of the cities in Uganda
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print(uganda_cities) 

#program to unpack your tuple
kampala, entebbe, jinja, mbarara, gulu = uganda_cities
print(kampala, entebbe, jinja, mbarara, gulu)

#Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above
print(uganda_cities[1:4])

#two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Jane", "Alice")
second_names = ("Doe", "Smith", "Johnson")
full_names = first_names + second_names
print(full_names)

#Create a tuple of colors and multiply it by 3
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

#Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_eight = thistuple.count(8)
print(count_of_eight) 

#EXERCISE 3
#Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print(beverages)

#Use the correct method to add 2 more items to the beverages set.
beverages.add("soda")
beverages.add("water")
print(beverages)

#Given the set below;
#mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
#Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
is_microwave_present = "microwave" in mySet
print(is_microwave_present) 

#Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print(mySet) 

#Write a python program to loop through the set above.
for item in mySet:
       print(item)

#Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["elderberry", "fig"]
my_set.update(my_list)
print(my_set)

#Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35}
first_names = {"John", "Jane", "Alice"}
combined_set = ages.union(first_names)
print(combined_set) 

#EXERCISE 4
#Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
age = 10
fruit = " apples"
concatenated_result = str(age) + fruit
print(concatenated_result)

#Consider the example below;
#txt = “      Hello,       Uganda!       ”
#Output the string without spaces at the beginning, in the middle and at the end.
txt = "      Hello,       Uganda!       "
trimmed_txt = ' '.join(txt.split())
print(trimmed_txt)

#Write a python program to convert the value of ‘txt’ to uppercase.
upper_txt = txt.upper()
print(upper_txt)

#Write a python program to replace character ‘U’ with ‘V’ in the string above.
replaced_txt = txt.replace('U', 'V')
print(replaced_txt)

#Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
#y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
substring = y[1:4]  
print(substring)

#The piece of code below will give an error when output;
#x = “All “Data Scientists” are cool!” 
#Write a python program to correct it.
x = 'All "Data Scientists" are cool!'  
print(x)

#EXERCISE 5
#With reference to the dictionary below, write a python program to print the value of the shoe size. 
#Add this dictionary to your .py file
#Shoes = {
	#“brand” : “Nick”,
	#“color” : “black”,
	#“size” : 40
	#}
Shoes = {
       "brand": "Nick",
       "color": "black",
       "size": 40
   }
print(Shoes["size"])
 
#Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)

#Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)

#Write a python program to return a list of all the keys in the dictionary above.
keys_list = list(Shoes.keys())
print(keys_list)

#Write a python program to return a list of all the values in the dictionary above.
values_list = list(Shoes.values())
print(values_list)

#Check if the key “size” exists in the dictionary above.
key_exists = "size" in Shoes
print(key_exists)

#Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
       print(f"{key}: {value}")

#Write a python program to remove “color” from the dictionary.
del Shoes["color"]
print(Shoes) 

#Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)

#Write a dictionary of your choice and make a copy of it.
original_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
copied_dict = original_dict.copy()
print(copied_dict) 

#Write a python program to show nested dictionaries
nested_dict = {
        "person": {
            "name": "Bob",
            "age": 25,
            "address": {
                "street": "123 Main St",
                "city": "Los Angeles"
            }
        },
        "job": {
            "title": "Engineer",
            "company": "Tech Corp"
        }
    }
print(nested_dict) 


