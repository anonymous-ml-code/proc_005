# Dictionary of color names and their hexadecimal codes
COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


# Print all color names and codes neatly lined up
print("Color names and codes:")
for name, code in COLOR_CODES.items():
    print(f"{name:20} {code}")


# def capitalize_each_word(text):
#     return ''.join(word[0].upper() + word[1:] for word in text.split())

# Ask the user for a color name and display the corresponding hex code
color_name = input("\nEnter a color name (or blank to quit): ").strip().title()  # Normalize input
# print(color_name)
# color_name = capitalize_each_word(color_name)
while color_name != "":
    try:
        print(f"The hex code for {color_name} is {COLOR_CODES[color_name]}")
    except KeyError:
        print(f"Invalid color name: {color_name}")
    color_name = input("Enter a color name (or blank to quit): ").strip().title()  # Normalize input
    # color_name = capitalize_each_word(color_name)