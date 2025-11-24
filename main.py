import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    """
    Generate a random password based on given options.
    """
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        chars = string.ascii_letters  # default to letters if nothing selected
    return ''.join(random.choice(chars) for _ in range(length))

def get_boolean_input(prompt, default=True):
    """
    Ask user yes/no question and return True/False.
    Repeat until valid input is provided.
    """
    default_char = 'y' if default else 'n'
    while True:
        user_input = input(f"{prompt} (y/n, default {default_char}): ").strip().lower()
        if user_input == '':
            return default
        elif user_input in ('y', 'n'):
            return user_input == 'y'
        
        else:
            print("Invalid input. Please enter 'y' or 'n'.")



def get_length_input(prompt, default=12):
    """
    Ask for password length.
    - Return an integer > 0
    - Return 0 if user wants to quit
    - Repeat until valid input is provided
    """
    while True:
        user_input = input(f"{prompt} (0 to quit, default {default}): ").strip()
        if user_input == '0':
            return 0
        if user_input == '':
            return default
        try:
            length = int(user_input)
            if length > 0:
                return length
            else:
                print("Length must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== Password Generator ===")

    while True:
        # Ask which characters to include
        use_letters = get_boolean_input("Include letters?", default=True)
        use_digits = get_boolean_input("Include numbers?", default=True)
        use_symbols = get_boolean_input("Include symbols?", default=True)

        # Ask for password length
        length = get_length_input("Enter password length")
        
        # Exit if 0
        if length == 0:
            print("Exiting. Goodbye!")
            break

        # Generate password
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"\nGenerated Password ({length} chars): {password}\n")

if __name__ == "__main__":
    main()

