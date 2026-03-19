class User:

    users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

        for user in User.users:
            if user.email == email:
                raise ValueError('Bu email allaqachon mavjud!')

        User.users.append(self)

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}."

    @classmethod
    def find_user(cls, email):
        for user in cls.users:
            if user.email == email:
                return user
            return None


    @classmethod
    def delete_user(cls, email):
        for user in  User.users:
            if user.email == email:
                cls.users.remove(user)
                return None
            raise ValueError("User topilmadi")


user1 = User("Ali", "ali@gmail.com")
user2 = User("Salima", "salima@gamil.com")
user3 = User("Vali", "vali12@gamil.com")
user4 = User("Bob", "bob7@gamil.com")
user5 = User("Alica", "alicaxon@gamil.com")


user5.find_user("alicaxon@gamil.com")
print(user5)


user1.delete_user("ali@gmail.com")
print(user1)
