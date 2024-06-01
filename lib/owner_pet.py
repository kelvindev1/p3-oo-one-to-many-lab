class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        if not pet_type in Pet.PET_TYPES:
            raise Exception("Pet is not in the list")
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner.name == self.name]
    
    def add_pet(self, pet):
        if not isinstance (pet, Pet):
            raise TypeError("The value must be an instance of the pet class")
        else:
            pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet:pet.name)
