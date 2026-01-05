

#===============================================================================

# def greet_user():
#     """Display a simple greeting"""
#     print("Hello")

# greet_user()

#===============================================================================


# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")

# greet_user('juris')

#===============================================================================

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet('hamster', 'combat')

# def describe_human(first_name, last_name):
#     """Display information about the user."""
#     print(f"I have friend named {first_name}")
#     print(f"Mu friends full name is {first_name.title()} {last_name.title()}")

# describe_human('Paul', 'Anders')
# describe_human('John', 'Smith')

#===============================================================================

# def describe_animal(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"I have a {animal_type}!")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_animal('hamster', 'combat')
# describe_animal('dog', 'starky')

#===============================================================================

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='combat')

#===============================================================================

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='willie')

#===============================================================================

# def formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = formatted_name('jimi', 'hendrix')
# print(musician)

#===============================================================================

# def formatted_name(first_name, middle_name, last_name):
#     """Returning a full name"""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()

# musician = formatted_name('john', 'lee', 'hooker')
# print(musician)

#===============================================================================

# def formatted_name(first_name, last_name, middle_name=''):
#     """get formatted name"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = formatted_name('jimi', 'hendrix')
# print(musician)

# musician = formatted_name('john', 'hooker', 'lee')
# print(musician)

# def formatted_name(first_name, last_name, middle_name=''):
#     """Getting formated name"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# person = formatted_name('Paul', 'Anders', 'Andersen')
# print(person)

# person = formatted_name('Rosalinda', 'Smith')
# print(person)

#===============================================================================

# def build_person(first_name, last_name):
#     """Return information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

#===============================================================================

# def build_person(first_name, last_name, age=None):
#     """Dictionary about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=35)
# print=(musician)

#===============================================================================

# def get_formatted_name(first_name, last_name):
#     """Returning a full name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")

# def get_full_name(first_name, last_name):
#     """Getting a full name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("Frist name:")
#     if f_name == 'q':
#         break

#     l_name = input("Last name:")
#     if l_name == 'q':
#         break

#     full_name = get_full_name(f_name, l_name)
#     print(f"\nHello, {full_name}")


#===============================================================================

# def get_formatted_name(first_name, last_name):
#     """Return full and formatted name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")

#===============================================================================

# def city_country(city, country):
#     """Return a string in the format city, country"""
#     return f"{city.title()}, {country.title()}"

# print(city_country('Santiago', 'Chile'))
# print(city_country('Oslo', 'Norway'))
# print(city_country('Riga', 'Latvia'))

#===============================================================================

# def greet_users(names):
#     """Printin greeting message to user"""
#     for name in names:
#         msg = f"hello, {name.title()}"
#         print(msg)

# usernames = ['Juris', 'Andrea', 'George']
# greet_users(usernames)

#===============================================================================

# unprinted_designs = ['phonr case', 'robot pendant', 'flowers']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

#===============================================================================

# def print_models(unprinted_designs, completed_designs):
#     """Simulate printing designs until none is left"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all models that are printed"""
#     print("\nThe following models have beed printed: ")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'tree']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#===============================================================================
