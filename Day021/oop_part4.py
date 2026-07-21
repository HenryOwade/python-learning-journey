class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email #Use underscores to make the attributes protected
    
    def set_email(self, new_email):
        self._email = new_email
    
    
user1 = User("Danthem", "dan@gmail.com", "123")

print(user1.get_email()) #getter method

user1.set_email("danny@outlook.com") #setter method

print(user1.get_email())