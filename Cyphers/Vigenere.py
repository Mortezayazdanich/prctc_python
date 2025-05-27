# Vigenère Cipher Implementation
# This implementation uses a simple Vigenère cipher algorithm
# which encrypts and decrypts messages using a key.
# The key is repeated to match the length of the message.
# The direction parameter determines whether to encrypt (1) or decrypt (-1).

class VigenereCipher:
    """A class to perform Vigenère cipher encryption and decryption."""
    
    def __init__(self):
        """Initialize the cipher with the alphabet."""
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def validate_inputs(self, message: str, key: str) -> None:
        """
        Validate the input message and key.
        
        Args:
            message (str): The message to be processed
            key (str): The encryption/decryption key
            
        Raises:
            ValueError: If inputs are invalid
        """
        if not message:
            raise ValueError("Message cannot be empty.")
        if not key or not key.isalpha():
            raise ValueError("Key must contain only alphabetic characters.")

    def process_text(self, message: str, key: str, direction: int = 1) -> str:
        """
        Process the text using Vigenère cipher.
        
        Args:
            message (str): The text to process
            key (str): The encryption/decryption key
            direction (int): 1 for encryption, -1 for decryption
            
        Returns:
            str: The processed text
        """
        if direction not in [1, -1]:
            raise ValueError("Direction must be 1 for encryption or -1 for decryption.")
        
        self.validate_inputs(message, key)
        key = key.lower()
        processed_text = ''
        key_index = 0
        
        for char in message.lower():
            if not char.isalpha():
                processed_text += char
                continue
                
            key_char = key[key_index % len(key)]
            key_index += 1
            
            char_index = self.alphabet.find(char)
            key_offset = self.alphabet.find(key_char)
            new_index = (char_index + key_offset * direction) % len(self.alphabet)
            processed_text += self.alphabet[new_index]
        
        return processed_text
    
    def encrypt(self, message: str, key: str) -> str:
        """Encrypt the message using the provided key."""
        return self.process_text(message, key, 1)
    
    def decrypt(self, message: str, key: str) -> str:
        """Decrypt the message using the provided key."""
        return self.process_text(message, key, -1)


def main():
    """Main function to run the Vigenère cipher program."""
    cipher = VigenereCipher()
    
    try:
        print("\n=== Vigenère Cipher ===")
        message = input("Enter text to process: ").strip()
        key = input("Enter encryption key: ").strip()
        
        while True:
            choice = input("Choose operation (1 for encrypt, 2 for decrypt): ").strip()
            if choice in ['1', '2']:
                break
            print("Invalid choice. Please enter 1 or 2.")
        
        if choice == '1':
            result = cipher.encrypt(message, key)
            operation = "Encrypted"
        else:
            result = cipher.decrypt(message, key)
            operation = "Decrypted"
        
        print("\nResults:")
        print("-" * 40)
        print(f"Original text: {message}")
        print(f"Key: {key}")
        print(f"{operation} text: {result}")
        print("-" * 40)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
# End of Vigenère Cipher Implementation
# Note: The key is expected to be in lowercase and only alphabetic characters.
# The text can contain any characters, and they will be preserved in the output.
# This implementation is case-insensitive and ignores non-alphabetic characters.
# The key is expected to be in lowercase and only alphabetic characters.
# The text can contain any characters, and they will be preserved in the output.
