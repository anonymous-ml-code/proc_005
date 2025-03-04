# Dictionary of Australian state abbreviations and names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all states and names neatly lined up
print("All states and names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

# Ask the user for their 'short' state and print the full state name
# Convert input to uppercase
state_code = input("\nEnter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    # Convert input to uppercase
    state_code = input("Enter short state: ").upper()
