import json
from os import write


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
    output = ""  # define an empty string
    for animal in animals_data:
        # append information to each string
        name = animal.get("name")
        diet = animal["characteristics"].get("diet")
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type")
        if name is not None:
            output += f"Name: {name}\n"
        if diet is not None:
            output += f"Diet: {diet}\n"
        if location is not None:
            output += f"Lokation: {location}\n"
        if animal_type is not None:
            output += f"Type: {animal_type}\n"
        output += "\n"  # Empty print for spacing
    print(output)
    return output

def read_template(template_path):
    with open(template_path, "r") as fileobj:
        template = fileobj.read()
        return template

def add_animals_to_template(template, output):
    animals_text = template.replace("__REPLACE_ANIMALS_INFO__", output)
    return animals_text

def write_animals_file(animals_text):
    with open("animals.html", "w") as fileobj:
        fileobj.write(animals_text)


def main():
    animals_data = load_data('animals_data.json')
    output = get_animal_data(animals_data)
    template = read_template('animals_template.html')
    animals_text = add_animals_to_template(template, output)
    write_animals_file(animals_text)




if __name__ == '__main__':
    main()