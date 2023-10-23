# credit: Nathan Padriga
def encode(raw_password):
    encoded_password = ""

    for raw_digit in raw_password:
        # Adds 3 to each digit of the new pass
        # Ex. 9 -> 12
        buffer = str(int(raw_digit) + 3)

        # Strip the tens place if adding 3 results in a non-single digit number
        # Ex. 12 -> 2
        encoded_digit = buffer[-1]
        encoded_password += encoded_digit

    return encoded_password

if __name__ == '__main__':

    stored_password = ""

    while True:
        print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
              """)

        option = input("Please enter an option: ")

        match option:
            case "1": # Encode
                stored_password = encode(input("Please enter your password to encode: "))
                print("Your password has been encoded and stored!")
            case "2": # Decode
                print("Unimplemented!")
            case "3": # Quit
                exit()
