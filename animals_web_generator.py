import json


def load_data(file_path):
    """Loads JSON data from a file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal's information to HTML format."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj["characteristics"].get("diet", "Unknown")}<br/>\n'

    # Add the first location if available
    if animal_obj.get('locations'):
        output += f'    <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    # Add 'Type' only if it exists
    if 'type' in animal_obj:
        output += f'    <strong>Type:</strong> {animal_obj["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_animal_html(animals):
    """Generates the full HTML string for all animals."""
    html_output = ''  # Renamed variable to avoid shadowing
    for animal_obj in animals:
        html_output += serialize_animal(animal_obj)
    return html_output


def create_html_file(template_path, output_path, animals_html):
    """Reads the HTML template, replaces the placeholder, and writes the result to a new file."""
    with open(template_path, 'r') as template_file:
        html_template = template_file.read()

    # Replace the placeholder with the generated animal data
    final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_html)

    with open(output_path, 'w') as output_file:
        output_file.write(final_html)

    print("HTML file generated successfully.")


# Main execution flow
if __name__ == '__main__':
    animal_data = load_data('animals_data.json')  # Renamed to avoid shadowing
    animals_html_content = generate_animal_html(animal_data)  # Renamed to avoid shadowing
    create_html_file('animals_template.html', 'animals.html', animals_html_content)
