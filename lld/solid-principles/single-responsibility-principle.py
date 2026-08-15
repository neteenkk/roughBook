class User:
    def __init__(self, username: str, email: str, password: str):
        self._username = username
        self._email = email
        self._password = password


    def get_username(self) -> str:
        return self._username

    def get_email(self) -> str:
        return self._email



user1 = User("nitin", "nitin@gmail.com", "pass1")
print(user1.get_username())
print(user1.get_email())
