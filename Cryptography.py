message = input("Enter the message: ")

encrypted_message = ""
for char in message:
    if char.isalpha():
        ascii_val = ord(char)
        shifted_ascii = ascii_val + 4
        if char.islower():
            if shifted_ascii > ord('z'):
                shifted_ascii -= 26
            encrypted_message += chr(shifted_ascii)
        else:
            if shifted_ascii > ord('Z'):
                shifted_ascii -= 26
            encrypted_message += chr(shifted_ascii)
    else:
        encrypted_message += char

print("Encrypted Message:", encrypted_message)