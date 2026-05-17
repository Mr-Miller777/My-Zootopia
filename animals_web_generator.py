import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def get_animal_data(animals_data):
    """
    Iterate through the animals_data and get
    the following information for each one:
    - Name
    - Diet
    - The first location from the list of locations
    - Type
    """
    for animal in animals_data:
        name = animal.get("name")
        diet = animal["characteristics"].get("diet")
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type")
        if name is not None:
            print(f"Name: {name}")
        if diet is not None:
            print(f"Diet: {diet}")
        if location is not None:
            print(f"Lokation: {location}")
        if animal_type is not None:
            print(f"Type: {animal_type}")
        print("") #Empty print for spacing


def main():
    animals_data = load_data('animals_data.json')
    get_animal_data(animals_data)


if __name__ == '__main__':
    main()