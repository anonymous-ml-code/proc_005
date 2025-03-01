"""
Emails
Estimate: 40 minutes
Actual:   55 minutes
"""

def extract_name_from_email(email):
    """Extract a name from an email address."""
    # Split the email at '@' and take the part before it
    username = email.split('@')[0]
    # Split the username at '.' and join with spaces
    name_parts = username.split('.')
    name = ' '.join(name_parts).title()
    return name

def main():
    """Main function to store emails and names, then print them."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    # Print all stored emails and names
    print("\nStored emails and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()