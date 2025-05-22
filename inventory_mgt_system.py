print('''
    ----------------------------------
    Welcome to Multipliers supermarket
    ----------------------------------
    1. View Items
    2. Buy items
    3. Exit
''')

option = int(input("Enter your option = "))

if option == 1:
    fruits = ['apple', 'banana', 'cherry', 'pineapple', 'watermelon']
for fruit in fruits:
    print(fruit)


