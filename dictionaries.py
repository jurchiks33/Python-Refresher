

# Book_0 = {'Cover': 'Hardcover', 'pages': '735'}
# print(Book_0['Cover'])
# print(Book_0['pages'])


# Book_0 = {'Cover': 'Hardcover', 'pages': '735'}

# book_pages = Book_0['pages']
# print(f"This book have {book_pages} pages!")


# Book_0 = {'Cover': 'Hardcover', 'pages': '735'}
# print(Book_0)

# Book_0['Shelf'] = 7
# Book_0['row'] = 4
# print(Book_0) 


# Book_0 = {}

# Book_0['cover'] = 'Hardcover'
# Book_0['pages'] = '735'
# Book_0['shelf'] = '7'
# Book_0['row'] = '4'

# print(Book_0)

#===============================================================

# book_0 = {'cover': 'hardcover'}
# print(f"books current cover is {book_0['cover']}")
# book_0['cover'] = 'softcover'
# print(f"New cover for the book is {book_0['cover']}")

#==============================================================

# car_0 = {'x_position': 10, 'y_position': 50, 'speed': 20}
# print(f"original position is {car_0 ['x_position']}")

# if car_0['speed'] == 15:
#     x_increment = 1
# elif car_0['speed'] == 20:
#     x_increment = 5
# else:
#     x_increment = 10

# car_0['x_position'] = car_0['x_position'] + x_increment
# print(f"New cars position is: {car_0['x_position']}")

#=============================================================

# car_0 = {'color': 'green', 'model': 'bmw', 'speed': 'fast'}
# print(car_0)

# del car_0['speed']
# print(car_0)

#============================================================

# car_colors = {
#     'audi': 'silver',
#     'BMW': 'black',
#     'toyota': 'white',
#     'tesla': 'red'
# }

# print(car_colors)

# color = car_colors['tesla'].title()
# print(f"Most common color for the tesla is {color}")

#============================================================

# patient_0 = {
#     'name': 'unknown',
#     'location': 'Milky Way Galaxy',
#     'origin': 'Andromeda' 
#     }

# for key, value in patient_0.items():
#     print(f"\nKey: {key}")
#     print(f"\nValue: {value}")

#===========================================================

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'javaScript'
# }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

#==========================================================

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'javaScript'
# }

# for name in favorite_languages.keys():
#     print(name.title())

# for name in favorite_languages.values():
#     print(name.title())

#=========================================================

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# alien_3 = {'color': 'rainbow', 'points': 50}

# aliens = [alien_0, alien_1, alien_2, alien_3]
# for alien in aliens:
#     print(alien)

#========================================================

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

#=======================================================

