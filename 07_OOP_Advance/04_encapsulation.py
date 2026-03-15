# Encapsulation: Core OOP priciple that bundles data attributes and methods into a single unit
# called class. Python does not use strict public, protected and private members, instead, it 
# uses naming convension to denote those attribute.

# public - Does not start with underscore (_). This can be accessed ourside the class, 
# using object.
# protected - starts with a underscore (_). This can be accessed in class and subclass only.
# private - starts with double underscore (__). Python's interpreter automatically performs 
# a process called name mangling, where it changes the name of the member 
# to _ClassName__private_member 

class UserProfile:
    def __init__(self, username, password, token, credit_card_number):
        # Public member.
        self.username = username

        # Protected member.
        self._password = password

        # Private member.
        self.__access_token = token
        self.__credit_card_number = credit_card_number

    # This shows the public member.
    def show_user(self):
        print(f'\nUser Name: {self.username}')

    # This returns the protected member.
    def get_password_hash(self):
        return hash(self._password)
    
    def login(self, password_entered):
        if self._password == password_entered:
            print(f'\nLogin successful. You can use access token - {self.__access_token}')
        else:
            print(f'\nPlease login with correct creadentials.')

if __name__ == '__main__':

    user1 = UserProfile('bittu@email.com', 'my_secret_pass', 'abc-1234', '8876-2234-1123')

    user1.show_user()
    user1.get_password_hash()
    user1.login('Wrong_password')
    user1.login('my_secret_pass')

    try:
        print(f'Credit Card No.: {user1.__credit_card_number}')
    except AttributeError as e:
        print(f'\nPrivate member access error! {e}')

    # Bad convension.
    print(f'Credit Card No.: {user1._UserProfile__credit_card_number}')
