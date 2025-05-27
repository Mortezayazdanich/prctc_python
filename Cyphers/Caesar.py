def caesar(message, shift):
    """
    Encrypts a message using the Caesar cipher algorithm.
    
    Args:
        message (str): The text to encrypt
        shift (int): The number of positions to shift each letter
    
    Returns:
        str: The encrypted text
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        elif char in alphabet:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char  # Keep non-alphabet characters unchanged
    
    return encrypted_text

def main():
    # Get input from user
    message = input("Enter the message to encrypt: ")
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            print("Shift value must be between 1 and 25")
        except ValueError:
            print("Please enter a valid number")
    
    # Encrypt the message
    encrypted = caesar(message, shift)
    
    # Display results
    print("\nResults:")
    print("-" * 40)
    print(f"Original message: {message}")
    print(f"Shift value: {shift}")
    print(f"Encrypted message: {encrypted}")
    print("-" * 40)

if __name__ == "__main__":
    main()
