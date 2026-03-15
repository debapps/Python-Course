# This function checks if the given text is a palindrome.
def is_palindrome(text):
    if text == '' or text is None:
        print('An empty string isn\'t a palindrome')
        return None
    
    input_text = ''.join(text.upper().split())
    
    if input_text == input_text[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    text = input('Enter a text: ')
    if is_palindrome(text):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")