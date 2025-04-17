# main.py

from pet import Pet

# Create a new pet
my_pet = Pet("Buddy")

# Interact with the pet
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.train("sit")
my_pet.train("fetch")

# Display tricks and status
print(f"{my_pet.name} knows these tricks: {my_pet.show_tricks()}")
status = my_pet.get_status()
print(f"Status: Hunger={status['Hunger']}, Energy={status['Energy']}, Happiness={status['Happiness']}")
