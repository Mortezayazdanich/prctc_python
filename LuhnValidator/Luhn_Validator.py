def clean_card_number(card_number: str) -> str:
    """
    Remove any spaces or hyphens from the card number.
    
    Args:
        card_number (str): The credit card number with possible separators
        
    Returns:
        str: Cleaned card number containing only digits
        
    Raises:
        ValueError: If card number contains invalid characters
    """
    if not card_number:
        raise ValueError("Card number cannot be empty")
    
    cleaned = card_number.translate(str.maketrans({'-': '', ' ': ''}))
    if not cleaned.isdigit():
        raise ValueError("Card number must contain only digits, spaces, or hyphens")
    
    return cleaned

def verify_card_number(card_number: str) -> bool:
    """
    Verify a credit card number using the Luhn algorithm.
    
    Args:
        card_number (str): The credit card number to verify
        
    Returns:
        bool: True if the card number is valid, False otherwise
    """
    # Clean the card number first
    card_number = clean_card_number(card_number)
    
    # Check length is reasonable (most cards are 13-19 digits)
    if not (13 <= len(card_number) <= 19):
        return False
    
    # Calculate sum using Luhn algorithm
    card_digits = card_number[::-1]  # Reverse the string
    sum_of_digits = 0
    
    # Process odd positions (1-based index)
    sum_of_digits += sum(int(digit) for digit in card_digits[::2])
    
    # Process even positions (1-based index)
    for digit in card_digits[1::2]:
        doubled = int(digit) * 2
        sum_of_digits += doubled if doubled < 10 else doubled - 9
    
    return sum_of_digits % 10 == 0

def main():
    """Main function to run the credit card validation program."""
    print("\n=== Credit Card Number Validator ===")
    
    while True:
        try:
            card_number = input("\nEnter credit card number (or 'q' to quit): ")
            
            if card_number.lower() == 'q':
                print("Goodbye!")
                break
                
            if verify_card_number(card_number):
                print("Valid credit card number")
            else:
                print("Invalid credit card number")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
