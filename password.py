import pyperclip

class Password:
    password_list = []

    def __init__(self, first_name, last_name, phone_number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    
    def save_password(self):
        Password.password_list.append(self)

    def delete_password(self):
        Password.password_list.remove(self)
        
        
    @classmethod
    def find_by_number(cls,number):
        for password in cls.password_list:
            if password.phone_number == number:
                return password

    @classmethod
    def password_exist(cls,number):
        for password in cls.password_list:
            if password.phone_number == number:
                return True
        return False

    @classmethod
    def display_passwords(cls):
        return cls.password_list

    @classmethod
    def copy_emails(cls,number):
        password_found = Password.find_by_number(number)
        pyperclip.copy(password_found.email)
