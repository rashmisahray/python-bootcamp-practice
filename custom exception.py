
class PalindromeError(Exception):
    pass

def is_palindrome(input_str):
    if not isinstance(input_str, str):
        raise PalindromeError("Input must be a string")

    # Remove spaces and convert to lowercase
    clean_str = input_str.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if clean_str == clean_str[::-1]:
        return True
    else:
        return False

# Example usage
try:
    print(is_palindrome("racecar"))  
    print(is_palindrome("A man a plan a canal Panama"))  
    print(is_palindrome(123))  
except PalindromeError as e:
    print(e)