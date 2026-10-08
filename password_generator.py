import secrets
import string
min_length, max_length, default_length = 8, 128, 16 #minimum and maximum length of password user can ask , deafault length  is set to 16
look_alikes = set("Il1O0o") #confusing letters and numbers for users to read are excluded
symbols = "!@#$%^&*()-_=+[]{};:,.?/" #all the symbols that the password contains
pools = [
    "".join(c for c in chars if c not in look_alikes)#keep character only if it is not in lool_alikes
    for chars in (string.ascii_uppercase, string.ascii_lowercase, string.digits, symbols)
]
all_chars = "".join(pools)#all characters in pools joined together


def generate(length):
    """Build and return one password with the given number of characters."""
    chars = [secrets.choice(pool) for pool in pools] #ensures it contains at least 1 from each pools(uppercase lowercase digits and symbols)
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))] #now it fills the remaining places by selecting random character from characters
    secrets.SystemRandom().shuffle(chars)#randomly shuffles the password
    return "".join(chars)#join the character and returns the passwords


def ask_length():
    """Ask the user for the password length until a valid one is given."""
    # Keep asking until a valid length is returned
    while True:
        raw = input(f"Password length ({min_length}-{max_length}) [{default_length}]: ").strip() #ask to input the length of password and show max min and dafault
        if not raw:
            return default_length   #if nothing entered the deafult length is returned
        if raw.isdecimal() and min_length <= int(raw) <= max_length:
            return int(raw)   #checks if the input is a number or not and within the range of max and minimum length
        print(f"  Enter a whole number from {min_length} to {max_length}.")  #incase of invalid input asks again

while True:
    try:
        print(f"{generate(ask_length())}",end="\n\n")
        again= input(f"Type 'again' to generate another : ")
        if again.upper()!= "AGAIN":
            print("Program ended")
            break
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled.")