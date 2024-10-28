import hashlib

class User:
    __users = {}

    def __init__(self, username, password, is_logged_in=False):
        self.username = username
        self.__password = password
        self.is_logged_in = is_logged_in

    @classmethod
    def display_users(cls):
        print(f"User list: ", list(cls.__users.keys()))

    @staticmethod
    def __hash_password(password):
        return hashlib.sha256(str(password).encode()).hexdigest()

    # @staticmethod
    def check_registered_user(self):
        if self.username in list(self.__users.keys()):
            return True
        else:
            print(f"User with this user name not registered")
            return False
    
    # @staticmethod
    def get_user(self):
        if self.check_registered_user():
            return self.__users[self.username]
        return False
        # return self.
        
    def register(self):
        if self.username and self.__password:
            if self.username not in list(self.__users.keys()):
                hashedPass = self.__hash_password(self.__password)
                new_user = {
                    "username": self.username,
                    "password": hashedPass,
                    "is_logged_in": True
                }
                self.__users[self.username] = new_user
                print(f"New User {self.username} created successfully")
                return True
            else:
                print(f"Ther user name you provide: {self.username} is already exist, pls try new one")
                return False
        else:
            print(f"Please provide username and password correctly")
    
    def login(self):
        user = self.get_user()
        if user:
            if user['is_logged_in'] != True:
                user['is_logged_in'] = True
                print(f"{user.username} is successfully logged in")
            else:
                print(f"{user['username']} user already logged in")



    def logout(self):
        user = self.get_user()
        if user['is_logged_in'] == True:
            user['is_logged_in'] = False
            print(f"{user['username']} is LogOut")
            return True
        else:
            print(f"{user['username']} is not logged in, Loggedin first then try again")


               
               




user1 = User('faradalam', 2345)
user2 = User('ahmod', 2345)

user1.register()
user2.register()
user1.login()
user1.logout()
user1.logout()

User.display_users()


    