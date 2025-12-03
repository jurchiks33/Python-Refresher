

#===============================================================================

# message = input("Tell me something, and i will repeat it back to you:....")
# print(message)

#===============================================================================

# message = input("Hey whats your name?")
# print(f"Hey {message}, nice to meet you!")

#===============================================================================

# name = input("Please enter your name:")
# print(f"\nHello {name}!")

#===============================================================================

# name = input("Whats your name?")
# print(f"\nHello {name}!")

#===============================================================================

# prompt = " If you share your name, we can personalise message you see."
# prompt += "\nWhat is your name?"

# name = input(prompt)
# print(f"\nHello, {name}!")

#===============================================================================

# height = input("How tall are you, in cm?")
# height = int(height)

# if height >= 185:
#     print("\n Wow... you are one tall lad")
# else:
#     print("\nNice! you still have room to grow")

#===============================================================================

# number = input("Enter a number and i will tell you if it is odd:")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even")
# else:
#     print(f"\nThe number {number} is odd")

#===============================================================================

# current_number = 1
# while current_number <= 10:
#     print(current_number)
#     current_number += 1

#===============================================================================

# prompt = "\nTell me something and i will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

#===============================================================================

# prompt = "\nTell me something and i will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program."

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

#===============================================================================

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

#===============================================================================

# x = 1
# while x <= 5:
#     print(x)
#     x +=1

#===============================================================================

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

#===============================================================================

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

#===============================================================================

# responses = {}

# pooling_active = True

# while pooling_active:
#     name = input("\nWhat is your name? ")
#     response = input(f"{name} Which mountain would you like to climb someday?")

#     responses[name] = response

#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         pooling_active = False

# print("\n--- Pool Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")

#===============================================================================

