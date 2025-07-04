import string
import getpass
import pyfiglet

banner = pyfiglet.figlet_format("PWD Checker")
print(banner)
 
def evaluate_password(password):
    """Evaluate the password and return stats and strength level."""
    counts = {
        "lowercase": 0,
        "uppercase": 0,
        "digits": 0,
        "whitespace": 0,
        "special": 0
    }

    for char in password:
        if char in string.ascii_lowercase:
            counts["lowercase"] += 1
        elif char in string.ascii_uppercase:
            counts["uppercase"] += 1
        elif char in string.digits:
            counts["digits"] += 1
        elif char.isspace():
            counts["whitespace"] += 1
        else:
            counts["special"] += 1

    # Calculate strength level (max 5)
    strength = sum(1 for value in counts.values() if value > 0)

    return counts, strength

def get_strength_remark(strength):
    """Return a remark based on strength value."""
    remarks = {
        1: "Very Bad Password! Change ASAP.",
        2: "Weak Password! Consider changing.",
        3: "Average Password. Can be improved.",
        4: "Strong Password!",
        5: "Excellent! Very strong password."
    }
    return remarks.get(strength, "Invalid strength level.")

def print_results(counts, strength):
    print("\nYour password contains:")
    for key, value in counts.items():
        print(f"- {value} {key} character(s)")
    print(f"\nPassword Strength: {strength}/5")
    print(f"Verdict: {get_strength_remark(strength)}")

def ask_retry():
    while True:
        choice = input("\nDo you want to test another password? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def main():
    print("+++ Welcome to Password Strength Checker +++")
    while True:
        password = getpass.getpass("Enter a password to check: ")

        if len(password) < 6:
            print(" Warning: Password too short. Use at least 6 characters.")
        counts, strength = evaluate_password(password)
        print_results(counts, strength)

        if not ask_retry():
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
