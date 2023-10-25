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

def decoder(encoded_pass): # decoder function 
    decoded_pass = ""

    for char in encoded_pass:

        char = int(char)

        if char <= 2:
            if char == 2:
                char = 9
            elif char == 1:
                char = 8
            elif char == 0:
                char = 7
        else:
            char = char - 3

        make_string = str(char)
        decoded_pass += make_string

    return decoded_pass


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
                decoded_pass = decoder(stored_password)
                print(f"The encoded password is {stored_password}, and the original password is {decoded_pass}.\n")
            case "3": # Quit
                exit()
