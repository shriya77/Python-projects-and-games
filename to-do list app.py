Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
user_input = 'random'
data = []

def show_menu():
    print('Menu')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View items')
    print('4. Exit')

while user_input != '4':

    show_menu()
    user_input = input('Enter your choice: ')
  
    if user_input == '1':
      item = input('What is to be done? ')
      data.append(item)
      print('Added item', item)
    elif user_input == '2':
        item = input('What is to be marked as done? ' )
        if item in data:
            data.remove(item)
            print('Removed item:', item)
        else:
            print('Item does not exist in list')
    elif user_input == '3':
      print('List of to do items:')
      for item in data:
       print(item)
    elif user_input == '4':
      print('Goodbye')
    else:
     print('Please enter one of 1, 2, 3 or 4')
