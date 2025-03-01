"""
Wimbledon Champions
Estimate: 60 minutes
Actual:   75 minutes
"""

import csv

def read_wimbledon_data(filename):
    """Read the Wimbledon data from the CSV file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        data = [row for row in reader]
    return data

def count_champions(data):
    """Count how many times each champion has won Wimbledon."""
    champion_counts = {}
    for row in data:
        champion = row[2]  # Champion is in the 3rd column
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts

def get_champion_countries(data):
    """Get the set of countries that have produced Wimbledon champions."""
    countries = set()
    for row in data:
        countries.add(row[1])  # Country is in the 2nd column
    return sorted(countries)

def display_results(champion_counts, countries):
    """Display the champions and their win counts, and the countries in alphabetical order."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_counts.items()):
        print(f"{champion} {count}")

    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(countries))

def main():
    """Main function to read, process, and display Wimbledon data."""
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_counts = count_champions(data)
    countries = get_champion_countries(data)
    display_results(champion_counts, countries)


if __name__ == "__main__":
    main()